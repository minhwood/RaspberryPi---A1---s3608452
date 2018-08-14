#!/usr/bin/env python3
import sys
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/CalibrateTemperature')

from sense_hat import SenseHat
import os
import json
import requests
import calibrate_temperature

#temperature limit if lower then is mean the weather is cool
TEMPERATURE_LIMIT = 20

def main():
    room_temp_check(TEMPERATURE_LIMIT)

#Specific API-key (change to send to different devices)
API_KEY="o.kQ8eA9aCX4VK1lasbe84Hdi1wgJI4lmN"

#function to push a notification to other device 
def push_notification(title, body):
    #data will be send
    data_send = {"type": "note", "title": title, "body": body}
    #send a post request to the pushbullet sever (create-push)
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + API_KEY, 
                         'Content-Type': 'application/json'})
    #throw exception if the response is not OK(200) 
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')


#check the room temperature and decide what message to send
def room_temp_check(temp_limit):
    cali_temp = calibrate_temperature.actual_temperature()
    if cali_temp < temp_limit:
        push_notification("Raspberry Pi",
        "Current room temparature is "+str(cali_temp)+"'C, It kind of cold so your might want to bring your jacket")
    else:
        push_notification("Raspberry Pi",
        "Current room temparature is "+str(cali_temp)+"'C, The weather is very nice")

main()
