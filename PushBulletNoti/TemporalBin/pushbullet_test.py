#import subprocess

#subprocess.call('/home/pi/Code/A1/PushBulletNoti/pb.sh', shell=True)

import pushbullet

pushbullet.push_notification("RasberryPi","Good Morning Boss")

