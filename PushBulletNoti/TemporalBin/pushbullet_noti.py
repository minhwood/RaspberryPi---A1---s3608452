from sense_hat import SenseHat
import os
import pushbullet
import core_temp

s = SenseHat()


avg_temperature = round(s.get_temperature(),1)
cpu_temperature = core_temp.cpu_temp()

cali_temp  = avg_temperature - ((cpu_temperature - avg_temperature)/5.446)

if temperature < 20:
    pushbullet.push_notification("Rasberry Pi","Current weather:"+str(temperature)+"C, It kind of cold so you might want to bring your jacket")
else:
    pushbullet.push_notification("Rasberry Pi","Current weather:"+str(temperature)+"C, The weather is very nice")
