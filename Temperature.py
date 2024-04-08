import requests
import time
import json
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

url = "https://openweathermap.org/data/2.5/weather?id=4709796&appid=439d4b804bc8187953eb36d2a8c26a02"
url2 = "https://openweathermap.org/data/2.5/onecall?lat=26.2034&lon=-98.23&units=metric&appid=439d4b804bc8187953eb36d2a8c26a02"

def get_current_temp():
    #Gets and prints the current temperature at Edingburg
    currentRequest = requests.get(url)
    currentresponse_json = currentRequest.json()
    currentTemp = currentresponse_json['main']
    currentTemperature = float(currentTemp['temp'])
    return currentTemperature

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(100,100,200,50)
    w.setWindowTitle("Weather App")

    c=QLabel(w)
    c.move(100,0)

    l1=QLabel(w)
    l1.setText("Todays Temp")
    

    c.setText(str(round(get_current_temp()*1.8 +32))+"F")
    
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   window()

