import sqlite3 as lite
import sys

connection = lite.connect('/home/pi/RaspberryPi---A1---s3608452/BluetoothDetection/RegisteredDevicesDB/registered_devices.db')
with connection: 
    cur = connection.cursor() 
    cur.execute("DROP TABLE IF EXISTS REGISTERED_DEVICES_data")
    cur.execute("CREATE TABLE REGISTERED_DEVICES_data(name TEXT, mac_address TEXT)")
