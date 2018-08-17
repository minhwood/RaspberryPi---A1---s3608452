#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
config_file_path = '/home/pi/RaspberryPi---A1---s3608452/PushBulletNoti/config.ini'

#return temperature limit from config file
def get_temp_limit():
    config.read(config_file_path)
    return int(config.get('setting','temp_limit'))

#return api key from config file
def get_api_key():
    config.read(config_file_path)
    return config.get('setting','api_key')

#return delay time from config file
def get_delay_time():
    config.read(config_file_path)
    return int(config.get('setting','delay_time'))

#set a new temperature limit
def set_temp_limit(temp_limit):
    config.set('setting','temp_limit',str(temp_limit))
    with open(config_file_path,'w') as outf:
        config.write(outf)

#set a new api key
def set_api_key(api_key):
    config.set('setting','api_key',str(api_key))
    with open(config_file_path,'w') as outf:
        config.write(outf)

##set a new delay time
def set_delay_time(delay_time):
    config.set('setting','delay_time',str(delay_time))
    with open(config_file_path,'w') as outf:
        config.write(outf)
