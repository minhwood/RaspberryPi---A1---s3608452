#!/usr/bin/env python3
import sys
sys.path.insert( 0,'/home/pi/RaspberryPi---A1---s3608452/CalibrateTemperature')
sys.path.insert( 0,'/home/pi/RaspberryPi---A1---s3608452/BluetoothDetection/RegisteredDevicesDB')

from sense_hat import SenseHat
import bluetooth
import regisdevice_db_manager
import calibrate_temperature
from datetime import datetime
#route to the database
db_path = '/home/pi/RaspberryPi---A1---s3608452/BluetoothDetection/RegisteredDevicesDB/registered_devices.db'
#create an object to manage RegisteredDevicesDatabase
db = regisdevice_db_manager.RegisteredDevicesDatabase(db_path)

#detect nearby device that registered to Pi
def detect_nearby_registered_devices():
    s=SenseHat()
    registered_devices = db.getAllDevices()
    while True:
        s.show_message("Scanning")
        nearby_devices = bluetooth.discover_devices()
        for mac_address in nearby_devices:
            #each mac address detect check if is match to any in the database
            for row in registered_devices:
                if mac_address == row[1]:
                    print("Detect {}, Mac address {}...".format(row[0],row[1]))
                    temp = round(calibrate_temperature.actual_temperature(),1)
                    s.show_message("Hi {}! Current Temperature is {}'C".format(row[0],temp),scroll_speed = 0.08)

detect_nearby_registered_devices()

