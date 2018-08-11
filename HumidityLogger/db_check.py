import db_manager
import datetime

db = db_manager.SenseHatDatabase("./db/sense_humidity.db")

data = db.getAllData()

print(data)
for i in range(0,len(data['time'])):
    print(data['time'][i])
    print("..............")
    print("Humidity: %s" % data['humid'][i])
    print("Temperature: %s" % data['temp'][i])
    print("..............")
