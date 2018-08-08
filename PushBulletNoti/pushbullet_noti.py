from sense_hat import SenseHat
import os

s = SenseHat()

temperature = s.get_temperature()

if temperature < 20:
    print("the room is too cool, remmember to bring your jacket")
    os.system('coolroom_noti.sh')
else:
    print("weather is okay")
    os.system('home/pi/Code/A1/PushBulletNoti/goodweather_noti.sh')
