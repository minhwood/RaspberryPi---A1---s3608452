#!/usr/bin/env python3
import sys
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/HumidityLogger/db')
from flask import Flask, render_template, redirect, url_for
import datetime
import db_manager
import bokeh_double_graph
import os

db_path = "/home/pi/RaspberryPi---A1---s3608452/HumidityLogger/db/sense_humidity.db"
db = db_manager.SenseHatDatabase(db_path)
app = Flask(__name__)

@app.route('/')
def about():
    now = datetime.datetime.now().ctime()
    data_output = {
            'time': now
            }
    return render_template('about.html', **data_output)

@app.route('/humidity')
def humid_graph():
    now = datetime.datetime.now().ctime()
    data = db.getAllData()
    bokeh_double_graph.draw_humid_graph(data)
    data_output = {
        'time': now
        }
    return render_template('humidity.html', **data_output)

@app.route('/temperature')
def temp_graph():
    now = datetime.datetime.now().ctime()
    data = db.getAllData()
    bokeh_double_graph.draw_temp_graph(data)
    data_output = {
            'time':now
            }
    return render_template('temperature.html', **data_output)

@app.route('/record_current_humid_temp')
def record_humid_temp():
    os.system('/home/pi/RaspberryPi---A1---s3608452/HumidityLogger/humidity_logger.py')
    return redirect(url_for('humid_graph'))

@app.route('/send_notification')
def sendNotification():
    os.system('/home/pi/RaspberryPi---A1---s3608452/PushBulletNoti/temperature_notification.py')
    return redirect(url_for('temp_graph'))


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
