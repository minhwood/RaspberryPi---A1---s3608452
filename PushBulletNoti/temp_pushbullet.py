from sense_hat import SenseHat
import os
import pushbullet
import core_temp

s = SenseHat()

avg_temp = s.get_temperature()
cpu_temp = core_temp.cpu_temp()
print(round(avg_temp,2))
print(cpu_temp)

cali_temp = avg_temp - (float(cpu_temp - avg_temp) / 5.466)
cali_temp = round(cali_temp,1)
if cali_temp < 20:
    pushbullet.push_notification("Raspberry Pi",
    "Current room temparature is "+str(cali_temp)+"'C, It kind of cold so your might want to bring your jacket")
else:
    pushbullet.push_notification("Ras[berry Pi",
    "Current room temparature is "+str(cali_temp)+"'C, The weather is very nice")
