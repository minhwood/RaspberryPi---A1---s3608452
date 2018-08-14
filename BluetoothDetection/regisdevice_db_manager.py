import sqlite3
import datetime

class RegisteredDevicesDatabase:
    def __init__(self, dbpath):
        self.dbpath = dbpath
    
    def logData(self, name, mac_address):
        connection = sqlite3.connect(self.dbpath)
        curs = connection.cursor()
        curs.execute("INSERT INTO REGISTERED_DEVICES_data values((?),(?))",(name,mac_address))
        connection.commit()
        connection.close()

    def displayData(self):
        connection=sqlite3.connect(self.dbpath)
        curs=connection.cursor()
        print ("\nEntire database contents:\n")
        for row in curs.execute("SELECT * FROM REGISTERED_DEVICES_data"):
            print (row)
        connection.close()

    def getAllDevices(self):
        name = []
        mac_address = []
        connection=sqlite3.connect(self.dbpath)
        curs= connection.cursor()
        curs.execute("SELECT * FROM REGISTERED_DEVICES_data")
        data = curs.fetchall()
        connection.close()
        return data

