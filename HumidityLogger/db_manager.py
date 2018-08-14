#!/usr/bin/env python3
import sqlite3
import datetime

def convertStrToTime(string_time): 
    time = datetime.datetime.strptime(string_time, "%Y-%m-%d %H:%M:%S")
    return time

class SenseHatDatabase:
    def __init__(self, dbpath):
        self.dbpath = dbpath
    
    def logData(self,temp,humidity):
        connection = sqlite3.connect(self.dbpath)
        curs = connection.cursor()
        curs.execute("INSERT INTO SENSEHAT_data values(datetime('now','localtime'),(?),(?))",(temp,humidity))
        connection.commit()
        connection.close()

    def displayData(self):
        connection=sqlite3.connect(self.dbpath)
        curs=connection.cursor()
        print ("\nEntire database contents:\n")
        for row in curs.execute("SELECT * FROM SENSEHAT_data"):
            print (row)
        connection.close()

    def getAllData(self):
        time = []
        temp = []
        humid = []

        connection=sqlite3.connect(self.dbpath)
        curs= connection.cursor()
        curs.execute("SELECT * FROM SENSEHAT_data")
        data = curs.fetchall()
        connection.close()
        for row in data:
            time.append(convertStrToTime(row[0]))
            temp.append(row[1])
            humid.append(row[2])
        data_return = {'time':time, 'temp':temp, 'humid':humid }
        return data_return
