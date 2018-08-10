import os

def cpu_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=","")
    temp = temp.replace("'C\n","")
    return float(temp)

