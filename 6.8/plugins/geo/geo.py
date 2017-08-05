#By Storm Shadow http://techbliss.org
import icons.ico
import sys
import json
import os
import socket
import PyQt4
from PyQt4 import QtCore,  QtGui
import PyQt4.QtWebKit
import PyQt4.QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebView
import ctypes
CF_TEXT = 1

kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32

user32.OpenClipboard(0)
if user32.IsClipboardFormatAvailable(CF_TEXT):
    data = user32.GetClipboardData(CF_TEXT)
    data_locked = kernel32.GlobalLock(data)
    text = ctypes.c_char_p(data_locked)
    print("okay looking up "+text.value)
    kernel32.GlobalUnlock(data_locked)
else:
    print('no text in clipboard')
user32.CloseClipboard()
import pygeoip
import string

gi = pygeoip.GeoIP('GeoIPCity.dat')
try:
    ipadr = socket.gethostbyname(text.value)
    print socket.gethostbyname(text.value)
except AttributeError:
    ipadr = text.value
else:
    pass

j = gi.record_by_addr(ipadr)
latte = str(j[u'latitude'])
Lotte = str(j[u'longitude'])
foo = (latte +","+ Lotte)


YOURAPIKEY = "" #enter your Google Maps JavaScript API
java = '''
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple markers</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>

      function initMap() {
        var myLatLng = {lat: Pizza1, lng: Pizza2};

        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 15,
          center: myLatLng
        });

        var marker = new google.maps.Marker({
          position: myLatLng,
          map: map,
          title: 'There they are'
        });
      }
    </script>
    <script async defer
    src="http://maps.googleapis.com/maps/api/js?key=APIKEY&callback=initMap">
    </script>
  </body>
</html>
'''

new_str1 = string.replace(java, 'Pizza1', str(j[u'latitude']))
new_str2 = string.replace(new_str1, 'Pizza2', str(j[u'longitude']))
new_str3 = string.replace(new_str2, 'APIKEY', YOURAPIKEY)
maphtml = new_str3


class LookUp(QApplication):
    def __init__(self):
        QApplication.__init__(self, [])
        self.window = QWidget()
        self.window.setWindowTitle("IP Geolocator")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.setWindowFlags(PyQt4.QtCore.Qt.WindowStaysOnTopHint)
        self.window.setWindowIcon(icon)

        self.web = QWebView(self.window)
        self.web.setMinimumSize(1024,800)
        self.web.page().mainFrame().addToJavaScriptWindowObject('self', self)
        self.web.setHtml(maphtml)
        self.layout = QVBoxLayout(self.window)
        self.layout.addWidget(self.web)


        self.window.show()
        self.exec_()


LookUp()