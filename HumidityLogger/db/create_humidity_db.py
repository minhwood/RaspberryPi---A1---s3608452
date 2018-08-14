import sqlite3 as lite
import sys

#create connection to database
connection = lite.connect('/home/pi/RaspberryPi---A1---s3608452/HumidityLogger/db/sense_humidity.db')
with connection: 
    cur = connection.cursor() 
    # if the table al ready exist then delete and create new table
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")
