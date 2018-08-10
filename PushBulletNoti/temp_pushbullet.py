#!/usr/bin/env python3
from sense_hat import SenseHat
import os
import pushbullet
import calibrate_temperature

def room_temp_check():
    cali_temp = calibrate_temperature.actual_temperature()
    if cali_temp < 20:
        pushbullet.push_notification("Raspberry Pi",
        "Current room temparature is "+str(cali_temp)+"'C, It kind of cold so your might want to bring your jacket")
    else:
        pushbullet.push_notification("Raspberry Pi",
        "Current room temparature is "+str(cali_temp)+"'C, The weather is very nice")

room_temp_check()
