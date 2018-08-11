
from bokeh.plotting import figure, output_file, save
from datetime import datetime
from bokeh.models import DatetimeTickFormatter
from math import pi


db_path = "./db/sense_humidity.db"
db = db_manager.SenseHatDatabase(db_path)
data = db.getAllData()

p1 = figure( title="Humidity and Temperature Record" ,plot_width=600, plot_height=600)

p1.xaxis.axis_label = 'Time'
p1.yaxis.axis_label = 'Temperature and Humidity'

p1.circle( data['time'], data['temp'], color='#A6CEE3', legend='Temperature', size = 8)
p1.circle( data['time'], data['humid'], color='#B2DF8A', legend='Humidity', size = 8)
p1.line( data['time'],data['temp'], color='#A6CEE3', legend='Temperature', line_width=2)
p1.line( data['time'], data['humid'], color='#B2DF8A', legend='Humidity', line_width=2 )
p1.xaxis.formatter=DatetimeTickFormatter(
        hours=["%d %B %Y"]
    )
p1.legend.location = "top_left"
p1.xaxis.major_label_orientation = pi/3


output_file('./templates/graph.html')
save(p1)
