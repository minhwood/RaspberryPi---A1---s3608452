#!/usr/env/bin python3
from bokeh.plotting import figure, output_file, save
from datetime import datetime
from bokeh.models import DatetimeTickFormatter
from math import pi
from bokeh.layouts import gridplot
from bokeh.palettes import Spectral6
from bokeh.transform import linear_cmap

#Temperature graph
def draw_temp_graph(data):
    p1 = figure(x_axis_type = "datetime", title="Temperature Record" ,plot_width=600, plot_height=600)
    p1.xaxis.axis_label = 'Time'
    p1.yaxis.axis_label = 'Temperature'
    p1.circle( data['time'], data['temp'], color='#0080FF' , legend='Temperature', size = 8)
    p1.line( data['time'], data['temp'], color='#0080FF',legend='Temperature', line_width=2)
    p1.xaxis.formatter=DatetimeTickFormatter(
            minsec = ['%d %B %Y at %H:%M'],
            hours=["%d %B %Y at %H:%M"],
            minutes = ['%d %B %Y at %H:%M'],
            hourmin = ['%d %B %Y at %H:%M'],
            days = ['%d %B %Y at %H:%M'],
            months = ['%d %B %Y at %H:%M'],
            years = ['%d %B %Y at %H:%M']
        )
    p1.legend.location = "top_left"
    p1.xaxis.major_label_orientation = pi/3
    output_file('./templates/temp_graph.html')
    save(p1)

# Humidity graph
def draw_humid_graph(data):
    p2 = figure(x_axis_type="datetime", title="Humidity Record" ,plot_width=600, plot_height=600)
    p2.xaxis.axis_label = 'Time'
    p2.yaxis.axis_label = 'Humidity'
    p2.circle( data['time'], data['humid'], color='#B2DF8A', legend='Humidity', size = 8)
    p2.line( data['time'], data['humid'], color='#B2DF8A', legend='Humidity', line_width=2 )
    p2.xaxis.formatter=DatetimeTickFormatter(
            minsec = ['%d %B %Y at %H:%M'],
            hours=["%d %B %Y at %H:%M"],
            minutes = ['%d %B %Y at %H:%M'],
            hourmin = ['%d %B %Y at %H:%M'],
            days = ['%d %B %Y at %H:%M'],
            months = ['%d %B %Y at %H:%M'],
            years = ['%d %B %Y a5 %H:%M']
        )
    p2.legend.location = "top_left"
    p2.xaxis.major_label_orientation = pi/3
    output_file('./templates/humid_graph.html')
    save(p2)
