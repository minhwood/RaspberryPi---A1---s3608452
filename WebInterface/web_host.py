#!/usr/bin/env python3
import sys
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/HumidityLogger/db')
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/PushBulletNoti')
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/BluetoothDetection/RegisteredDevicesDB')
from flask import Flask, render_template, redirect, url_for, request
import datetime
import db_manager
import regisdevice_db_manager
import config_pushbullet_noti
import graph
import os
#path to sense hat db
sense_hat_db_path = "/home/pi/RaspberryPi---A1---s3608452/HumidityLogger/db/sense_humidity.db"
db = db_manager.SenseHatDatabase(sense_hat_db_path)

#path to registered devices db
registered_devices_db_path = "/home/pi/RaspberryPi---A1---s3608452/BluetoothDetection/RegisteredDevicesDB/registered_devices.db"
db_registered_device = regisdevice_db_manager.RegisteredDevicesDatabase(registered_devices_db_path)

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now().ctime()
    data_output = {
            'time': now
            }
    return render_template('home.html', **data_output)

#HumidityLogger--------------------------------------------------------------
@app.route('/humidity')
def humid_graph():
    now = datetime.datetime.now().ctime()
    data = db.getAllData()
    graph.draw_humid_graph(data)
    data_output = {
        'time': now
        }
    return render_template('/HumidityLogger/humidity.html', **data_output)

@app.route('/temperature')
def temp_graph():
    now = datetime.datetime.now().ctime()
    data = db.getAllData()
    graph.draw_temp_graph(data)
    data_output = {
            'time':now
            }
    return render_template('/HumidityLogger/temperature.html', **data_output)

@app.route('/record_current_humid_temp')
def record_humid_temp():
    os.system('/home/pi/RaspberryPi---A1---s3608452/HumidityLogger/humidity_logger.py')
    return redirect(url_for('humid_graph'))

#PushBullet Notification ------------------------------------------------------
@app.route('/templimit', methods=['GET','POST'])
def templimit():
    now = datetime.datetime.now().ctime()
    templimit = config_pushbullet_noti.get_temp_limit()
    if request.method == 'POST':
        templimit = request.form['templimit']
        config_pushbullet_noti.set_temp_limit(int(templimit))
    data_output = {
            'time':now,
            'templimit': templimit
            }
    return render_template('/PushBulletNoti/templimit.html', **data_output)

@app.route('/apikey', methods=['GET','POST'])
def apikey():
    now = datetime.datetime.now().ctime()
    api_key = config_pushbullet_noti.get_api_key()
    if request.method == 'POST':
        api_key = request.form['api_key']
        config_pushbullet_noti.set_api_key(api_key)
    data_output = {
            'time':now,
            'api_key': api_key
            }
    return render_template('/PushBulletNoti/api_key.html', **data_output)

@app.route('/delaytime', methods=['GET','POST'])
def delaytime():
    now = datetime.datetime.now().ctime()
    delay_time = config_pushbullet_noti.get_delay_time()
    if request.method == 'POST':
        delay_time = request.form['delay_time']
        config_pushbullet_noti.set_delay_time(int(delay_time))
    data_output = {
            'time':now,
            'delay_time': delay_time
            }
    return render_template('/PushBulletNoti/delay_time.html', **data_output)

#Bluetooth Detection -------------------------------------------------------------- 
@app.route('/adddevice', methods=['GET','POST'])
def adddevice():
    now = datetime.datetime.now().ctime()
    if request.method == 'POST':
        name = request.form['name']
        mac_address = request.form['mac_address']
        db_registered_device.logData(name,mac_address)
    data_output = {
            'time': now
            }
    return render_template('/BluetoothDetection/adddevice.html', **data_output)

@app.route('/registereddevices')
def registereddevices():
    now = datetime.datetime.now().ctime()
    devices = db_registered_device.getAllDevices()
    data_output = {
            'time': now,
            'devices': devices
            }
    return render_template('BluetoothDetection/registereddevices.html',**data_output)

if __name__ == '__main__':
    app.run(debug=False, port=80, host='0.0.0.0')
