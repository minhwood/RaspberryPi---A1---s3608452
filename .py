from sense_hat import SenseHat
import time
from datetime import datetime
import sqlite3

dbname='sensehat.db'

s = SenseHat()

def logData(temp,humidity):
    connection = sqlite3.connect(dbname)
    curs = connection.cursor
    curs.execute("INSERT INTO SENSEHAT_data value(datetime('now'),(?),(?))",(temp),(humidity))
    curs.commit()
    curs.close()

def displayData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SenseHat_data"):
        print (row)
    conn.close()


while True:
    humidity = round(s.get_humidity(),1)
    temperature = round(s.get_temperature(),1)
    temp_of_humidity  = s.get_temperature_from_humidity()
    logData(temperature,humidity)
    displayData
    print(datetime.now())
    print("Humidity: %s" % humidity)
    print("Temperature: %s" % temperature)
    print("Temperature of Humidity: %s" % temp_of_humidity)
    print("..............")
    time.sleep(4)



