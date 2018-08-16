#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
config_file_path = '/home/pi/RaspberryPi---A1---s3608452/PushBulletNoti/config.ini'
config.read(config_file_path)

def get_temp_limit():
    return int(config.get('setting','temp_limit'))

def get_api_key():
    return config.get('setting','api_key')

def get_delay_time():
    return int(config.get('setting','delay_time'))

def set_temp_limit(temp_limit):
    config.set('setting','temp_limit',str(temp_limit))
    with open(config_file_path,'w') as outf:
        config.write(outf)

def set_api_key(api_key):
    config.set('setting','api_key',str(api_key))
    with open(config_file_path,'w') as outf:
        config.write(outf)

def set_delay_time(delay_time):
    config.set('setting','delay_time',str(delay_time))
    with open(config_file_path,'w') as outf:
        config.write(outf)
