from sense_hat import SenseHat
import os

#get current cpu temperature 
def cpu_temperature():
    #run comman line  to get cpu temp
    temp = os.popen("vcgencmd measure_temp").readline()
    #replace the character that not needed to convert to float value
    temp = temp.replace("temp=","")
    temp = temp.replace("'C\n","")
    return float(temp)

#caculate the actual temperature using formula:
# actual_temp = avg_temp - ((cpu_temp-avg_temp)/5.446)-6
def actual_temperature():
    s = SenseHat()
    avg_temp = s.get_temperature()
    cpu_temp = cpu_temperature()
    cali_temp = avg_temp - ((cpu_temp-avg_temp)/5.466)-6
    cali_temp = round(cali_temp,1)
    return cali_temp
