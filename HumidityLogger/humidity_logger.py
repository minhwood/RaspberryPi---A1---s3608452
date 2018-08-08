from sense_hat import SenseHat
import time
from datetime import datetime

s = SenseHat()

while True:
    humidity = s.get_humidity()
    temperature = s.get_temperature()
    temp_of_humidity  = s.get_temperature_from_humidity()
    print(time.ctime(int(time.time())))
    print("Humidity: %s" % humidity)
    print("Temperature: %s" % temperature)
    print("Temperature of Humidity: %s" % temp_of_humidity)
    print("..............")
    time.sleep(4)
    
