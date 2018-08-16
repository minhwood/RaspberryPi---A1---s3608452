#!/usr/bin/env python3
import sys
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/CalibrateTemperature')

from sense_hat import SenseHat
import os
import json
import requests
import calibrate_temperature
import configparser
import time
#temperature limit if lower then is mean the weather is cool
temp_limit = 0
#push-bullet api
api_key = "o.kQ8eA9aCX4VK1lasbe84Hdi1wgJI4lmN"
#delay  after notify devices
delay_time = 0

def main():
    get_setting()
    room_temp_check(temp_limit)

#get value from config file
def get_setting():
    config = configparser.ConfigParser()
    config.read('config.ini')
    temp_limit = int(config.get('setting','temp_limit'))
    api_key = config.get('setting','api_key')
    delay_time = int(config.get('setting','delay_time'))

#function to push a notification to other device 
def push_notification(title, body):
    #data will be send
    data_send = {"type": "note", "title": title, "body": body}
    #send a post request to the pushbullet sever (create-push)
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + api_key, 
                         'Content-Type': 'application/json'})
    #throw exception if the response is not OK(200) 
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('Message sent')


#check the room temperature and decide what message to send
def room_temp_check(temp_limit):
    while True:
        cali_temp = calibrate_temperature.actual_temperature()
        if cali_temp < temp_limit:
            push_notification("Raspberry Pi",
                    "Current room temparature is "+str(cali_temp)+"'C, It kind of cold so you might want to bring your jacket")
            time.sleep(delay_time)#4 hrs 


main()
