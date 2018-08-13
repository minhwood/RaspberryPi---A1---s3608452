from sense_hat import SenseHat
import os

def cpu_temperature():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=","")
    temp = temp.replace("'C\n","")
    return float(temp)


def actual_temperature():
    s = SenseHat()

    avg_temp = s.get_temperature()
    cpu_temp = cpu_temperature()
    #cali_temp = avg_temp - ((cpu_temp - avg_temp) / 5.466)
    #cali_temp = avg_temp - (cpu_temp-avg_temp)
    #cali_temp = avg_temp - ((cpu_temp-avg_temp)/5.466)-6
    cali_temp = avg_temp - ((cpu_temp -avg_temp)/1.5)
    cali_temp = round(cali_temp,1)
    return cali_temp
