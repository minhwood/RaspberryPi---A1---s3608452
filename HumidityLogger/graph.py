from flask import Flask, render_template, redirect, url_for

import datetime
import db_manager
#import bokeh_double_graph

db_path = "./db/sense_humidity.db"
db = db_manager.SenseHatDatabase(db_path)
app = Flask(__name__)

@app.route('/graph')
def graph():
    now = datetime.datetime.now().ctime()
    data = db.getAllData()
    #bokeh_double_graph.draw_graph(data)
    data_output = {
        'time': now
        }
    return render_template('index.html', **data_output)

@app.route('/newlog')
def newlog():
    print('redirect')
    return redirect(url_for('graph'))


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
