from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json

POINTS_FILE = "points.json"
    
app = Flask(__name__)
# CORS policy
CORS(app)

@app.route('/points', methods=['GET'])
def get_points():
    """
    API GET endpoint

    Returns: 
    response (json)
    """
    points = load_points()
    return jsonify({"message": "Points retrieved successfully", "points": points})

@app.route('/point', methods=['POST'])
def save_point():
    """
    API POST endpoint

    Returns: 
    response (json)
    """
    data = request.json
    lat = str(data.get('lat'))
    lng = str(data.get('lng'))
    datetime_now = datetime.now().isoformat()
    new_point = {'lat': lat, 'lng': lng, 'datetime': datetime_now}
    points = add_point(new_point)
    return jsonify({"message": "Point added successfully", "points": points})

@app.route('/point/<int:point_id>', methods=['DELETE'])
def delete_point(point_id):
    """
    API DELETE endpoint

    Parameters:
    point_id (int): Point id to be deleted

    Returns: 
    response (json)
    """
    points = load_points()
    updated_points = [point for point in points if point["id"] != point_id]
    points = reorder_points(point_id, points)
    update_points(updated_points)
    return jsonify({'message': 'Point deleted successfully', 'points': updated_points}), 200

def load_points():
    """
    Loads data from points.json file

    Returns:
    list: Points list
    """
    try:
        with open(POINTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def update_points(points):
    """
    Updates the points.json file
    """
    with open(POINTS_FILE, "w") as file:
        json.dump(points, file)

def add_point(new_point):
    """
    Adds the new point to the points.json file

    Parameters:
    new_point (dict): New point information

    Returns: 
    points (list): Updated point list
    """
    points = load_points()
    new_point['id'] = len(points) + 1
    points.append(new_point)
    update_points(points)
    return points

def reorder_points(removed_point_id, points):
    """
    After deleting a point in the point list,
    it reorders the ids of the points in the list 
    by decreasing the ids of the points after the deleted id by one.

    Parameters:
    removed_point_id (int): Removed point id
    points (list): Points list

    Returns: 
    points (list): Updated point list
    """
    for i in range(removed_point_id-1, len(points)):
        points[i]["id"] -= 1
    return points

if __name__ == '__main__':
    app.run(debug=True)