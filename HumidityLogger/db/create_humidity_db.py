import sqlite3 as lite
import sys

connection = lite.connect('/home/pi/A1/RaspberryPi---A1---s3608452/HumidityLogger/db/sense_humidity.db')
with connection: 
    cur = connection.cursor() 
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")
