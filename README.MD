**Ida pro PyQt4 and Pyqt5 Geo locator http and IP Lookup**

****What it does****

look up web adress and resolve it to a ip and look it via google maps

or just lookup a ip adress

PyQt5 version street view also works.

****Dependencies****

ida 6.8 =<

*PyQt4 and the PyQt4 webkit*

ida 6.9 +

*PyQt5 and the PyQt5 QtWebEnginewidgets*

not needed but for more accurate results(1)

[GOOGLE JAVASCRIPT MAP API KEY](https://developers.google.com/maps/documentation/javascript/get-api-key)

**pygeoip**

`pip install pygeoip`

**Howto**

(1)not needed but Fill in your Java maps api key in line 47 in PyQt4 version and line 50 in PyQt5 version in geo.py for a more accurate result

Copy files to plugin folder and load via ALt+G

**right click a ip adress like 198.153.192.1 and press copy to clibboard**

**or a web adress without the http// or www like pypi.python.org and press copy to clibboard**

then hit shortcut ALT+G or load viq file menu in ida.

Remember it is the clipboard contents data it uses.

and remember that the program works without ida pro also.

**NB!**

Using MaxMind free GeoipCityData.dat(provided here in the package)

[MaxMind Site](https://www.maxmind.com/en/geoip2-city)



**Screenshot**

**PyQt4**

![maps](https://cloud.githubusercontent.com/assets/3592375/18419769/ff98ad24-7862-11e6-8423-808f7a973dd5.png)

**PyQt5**

![1](https://user-images.githubusercontent.com/3592375/28998155-aea2a2ca-7a24-11e7-92bb-b15ca10e10aa.png)

![2](https://user-images.githubusercontent.com/3592375/28998153-aea2532e-7a24-11e7-8c9b-be8424698bd2.png)

![3](https://user-images.githubusercontent.com/3592375/28998154-aea28d1c-7a24-11e7-8bd9-f2a5a3f57fd9.png)






