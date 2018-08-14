#!/usr/bin/env python3
from sense_hat import SenseHat
import time
from datetime import datetime
import db_manager
import sys
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/CalibrateTemperature')
import calibrate_temperature

dbpath='/home/pi/RaspberryPi---A1---s3608452/HumidityLogger/db/sense_humidity.db'

s = SenseHat()
s.show_message("recording")
db = db_manager.SenseHatDatabase(dbpath)

humidity = round(s.get_humidity(),1)
temperature = calibrate_temperature.actual_temperature()
db.logData(temperature,humidity)
db.displayData()

print()
print(datetime.now().ctime())
print("..............")
print("Humidity: %s" % humidity)
print("Temperature: %s" % temperature)
print("..............")
