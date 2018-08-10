#!/usr/bin/env python3
import requests
import json

API_KEY="o.kQ8eA9aCX4VK1lasbe84Hdi1wgJI4lmN"

def push_notification(title, body):
    data_send = {"type": "note", "title": title, "body": body}

    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + API_KEY, 
                         'Content-Type': 'application/json'})

    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')