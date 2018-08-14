#!/usr/bin/env python3
import sys
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/CalibrateTemperature')
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/HumidityLogger/db')

from sense_hat import SenseHat
import time
from datetime import datetime
import db_manager
import calibrate_temperature
#route to database
dbpath='/home/pi/RaspberryPi---A1---s3608452/HumidityLogger/db/sense_humidity.db'

s = SenseHat()
s.show_message("recording...")
#create an SenseHatDatabase object to manage the SENSEHAT_data database
db = db_manager.SenseHatDatabase(dbpath)
humidity = round(s.get_humidity(),1)
temperature = calibrate_temperature.actual_temperature()

#Save the data to the database
db.logData(temperature,humidity)

print(datetime.now().ctime())
print("..............")
print("Humidity: %s" % humidity)
print("Temperature: %s" % temperature)
print("..............")
