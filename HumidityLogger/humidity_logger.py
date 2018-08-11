#!/usr/bin/env python3
from sense_hat import SenseHat
import time
from datetime import datetime
import db_manager
import calibrate_temperature

dbpath='./db/sense_humidity.db'

s = SenseHat()

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
