#!/usr/bin/env python3
import sqlite3
import datetime

#function use to convert datetime value in database to datetime value in python
def convertStrToTime(string_time): 
    time = datetime.datetime.strptime(string_time, "%Y-%m-%d %H:%M:%S")
    return time

#class use to manage the database
class SenseHatDatabase:
    def __init__(self, dbpath):
        self.dbpath = dbpath
    
    #save data to the database
    def logData(self,temp,humidity):
        connection = sqlite3.connect(self.dbpath)
        curs = connection.cursor()
        curs.execute("INSERT INTO SENSEHAT_data values(datetime('now','localtime'),(?),(?))",(temp,humidity))
        connection.commit()
        connection.close()

    #return all data in a dictionary type
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
