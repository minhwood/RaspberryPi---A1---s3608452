import db_manager
import datetime

db = db_manager.SenseHatDatabase("./db/sense_humidity.db")

data = db.getAllData()

print(data)
for row in data:
    time = datetime.datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S")
    print(time.ctime())
    print("..............")
    print("Humidity: %s" % row[2])
    print("Temperature: %s" % row[1])
    print("..............")
