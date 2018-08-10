from flask import Flask, render_template

import datetime
import db_manager


db_path = './db/sense_humidity.db'
db = db_manager.SenseHatDatabase(db_path)
app = Flask(__name__)

@app.route('/graph')
def graph():
    now = datetime.datetime.now().ctime()
    sensehat_data = db.getAllData()
    data_output = {
        'time': now,
        'data': sensehat_data
        }
    return render_template('graph.html', **data_output)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
