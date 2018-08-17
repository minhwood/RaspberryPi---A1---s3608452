#!/usr/bin/env python3
import sys
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/BluetoothDetection/RegisteredDevicesDB')
import regisdevice_db_manager

#route to the database
db_path = '/home/pi/RaspberryPi---A1---s3608452/BluetoothDetection/RegisteredDevicesDB/registered_devices.db'
db = regisdevice_db_manager.RegisteredDevicesDatabase(db_path)
#promp user for device details and add to database
def add_device():
    name = input("Please input the name of the device:")
    mac = input("Please input the mac address:")
    db.logData(name,mac)

#execute function
add_device()
