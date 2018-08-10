import sqlite3

class SenseHatDatabase:
    def __init__(self, dbpath):
        self.dbpath = dbpath
    
    def logData(self,temp,humidity):
        connection = sqlite3.connect(self.dbpath)
        curs = connection.cursor()
        curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'),(?),(?))",(temp,humidity))
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
        connection=sqlite3.connect(self.dbpath)
        curs= connection.cursor()
        curs.execute("SELECT * FROM SENSEHAT_data")
        data = curs.fetchall()
        connection.close()
        return data
        
