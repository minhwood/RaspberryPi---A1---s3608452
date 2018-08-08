from sense_hat import SenseHat

s = SenseHat()

temperature = s.get_temperature()

if temperature < 20:
    print("the room is too cool, remmember to bring your jacket")
else:
    print("weather is okay")