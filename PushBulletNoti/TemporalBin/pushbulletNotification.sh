#!/bin/bash

curl --request POST https://api.pushbullet.com/v2/pushes\
     --header 'Access-Token: o.kQ8eA9aCX4VK1lasbe84Hdi1wgJI4lmN'\
     --header 'Content-Type: application/json' \
     --data-binary '{"body": "Hi Boss ","title":"RaspberryPi","type":"note"}' \
     
