#!/usr/bin/env python3
import sys
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/CalibrateTemperature')

from sense_hat import SenseHat
import os
import json
import requests
import calibrate_temperature
import time
import config_pushbullet_noti

#main function
def main():
    while True:
        #temperature limit if lower then is mean the weather is cool
        current_temp_limit = config_pushbullet_noti.get_temp_limit()
        room_temp_check(current_temp_limit)

#function to push a notification to other device 
def push_notification(title, body): 
    #push-bullet api
    api_key = config_pushbullet_noti.get_api_key()
    #data will be send
    data_send = {"type": "note", "title": title, "body": body}
    #send a post request to the pushbullet sever (create-push)
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + api_key, 
                         'Content-Type': 'application/json'})
    #throw exception if the response is not OK(200) 
    if resp.status_code != 200:
        raise Exception('Unable to send message, something wrong')
    else:
        print('Message sent')


#check the room temperature and decide what message to send
def room_temp_check(temp_limit):
    #delay  after notify devices
    delay_time = config_pushbullet_noti.get_delay_time()
    cali_temp = calibrate_temperature.actual_temperature()
    if cali_temp < temp_limit:
        push_notification("Raspberry Pi",
                "Current room temparature is "+str(cali_temp)+"'C, It kind of cold so you might want to bring your jacket")
        time.sleep(delay_time)#set a delay time after every notification sent 

#exceute code
main()
