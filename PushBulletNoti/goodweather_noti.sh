#!/bin/bash

curl --header 'Access-Token: o.kQ8eA9aCX4VK1lasbe84Hdi1wgJI4lmN'\
     --header 'Content-Type: application/json' \
     --data-binary '{"body": "Good weather","title":"RaspberryPi","type":"note"}' \
     --request POST \
     https://api.pushbullet.com/v2/pushes
