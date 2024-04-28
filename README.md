# SAMM MAP PROJECT

leaflet.js ile sayfaya bir harita eklenmesi ve belirli aksiyonların sayfa içerisinde sağlanması

## Getting Started

Bu talimatlar, geliştirme ve test amacıyla projenin bir kopyasını yerel makinenizde çalışır duruma getirecektir.

### Prerequisites

Yazılımı yüklemek için gerekenler
```
* [Repo](https://github.com/Murathanucar/samm.tech) 'nun indirilmesi
```
```
Python3 kurulumu
```
```
Flask kurulumu
```
```
flask-cors kurulumu
```
Docker tercih edilirse:
```
Docker kurulumu
```

### Installing

Kurulum aşamaları

Python3

```
https://www.python.org/downloads/ sitesinden indirip kuralım
```
Flask

```
pip install Flask
```
Docker

```
https://docs.docker.com/desktop/install/windows-install/ sitesinden "Docker Desktop for Windows"
butonuna tıklayarak .exe dosyasını indirelim.
Dosyayı çalıştırdıktan sonra ekrandaki iki tane checkbox seçili olarak kalsın ve devam edelim ve
kurulumu tamamlayalım.
Kurulum tamamlandıktan sonra uygulamayı çalıştıralım, hesap oluşturmadan devam edelim.
Biraz uzun sürebilir.
Docker engine uygulama tarafından başlatılacaktır.
Docker Desktop içerisinde docker-compose yükleniyor o yüzden ayrıca yüklemeye gerek kalmıyor.
```

## To run in Local

```
backend klasörüne girip main.py dosyasını python ile çalıştıralım.
Server olarak çalışacaktır. 
```
```
Browser da gizli sekme açıp, frontend klasöründeki girip index.html dosyasını
browsera sürükleyip bırakalım.
Gizli sekme açmammızın sebebi cache den kaynaklı sorunlarla uğraşmamaktır.
```

## To run in Docker

```
Başlat menüsünden yönetici olarak çalıştır diyerek "Windows PowerShell"
yada "Command Promt" açalım.
Projeyi dizinine gidelim.
docker-compose up --build komutunu çalıştıralım.Biraz uzun sürebilir image indirirken.
flask ve nginx konteynırları çalıştıktan sonra browser gizli sekme açıp localhost yazalım.
```

## Authors

* [Murathan Uçar](https://github.com/Murathanucar)
