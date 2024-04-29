'''

Written by alfredc333
'''

import os
import time

from flask import (
    Flask,
    g,
    jsonify,
    make_response,
    request,
    render_template
)

from . import db

path = os.path.abspath(".")
instancePath = os.path.join(path, './instance')  
print(instancePath)

app = Flask(__name__, instance_path=instancePath)
print(app.instance_path)

app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'sensorData.db'),
    )

db.init_db_app(app)

@app.route("/")
def showIndex():
    print("test")  

    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    app.logger.debug('Starting DB retrieval at ' + ts)
    dbH = db.get_db()
    query = 'SELECT * from Measurements ORDER By Mid DESC'
    cur = dbH.execute(query)
    rows = cur.fetchone()    
    return render_template('home.html', d = rows)
    


@app.route("/hello")
def hello_world():
    return render_template('try.html')
    #return "<p>Flask is up and running!</p>"



@app.route("/getData")
def getData():
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    app.logger.debug('Starting DB retrieval at ' + ts)
    dbH = db.get_db()
    query = 'SELECT * from Measurements ORDER By Mid DESC'
    cur = dbH.execute(query)
    rows = cur.fetchone()

    response = make_response(
        jsonify({
            'Mid': str(rows["Mid"]),
            'Temperature': str(rows["Temperature"]),
            'Humidity': str(rows["Humidity"]),
            'AirPressure': str(rows["AirPressure"]),
            'CO2level': str(rows["CO2level"]),
            'Measurement Timestamp': str(rows["Timestamp"]),
            'Time Now ': ts
        }), 200)

    response.headers["Content-Type"] = "application/json"
    return response

@app.route("/setData", methods=['POST'])
def setData():
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    app.logger.debug('Starting DB write at ' + ts)
    dbConnection = db.get_db()
    c = dbConnection.cursor()
    #test line dbString = 'INSERT INTO Measurements VALUES(null ,\'2001-01-01 10:37:09\', 4, 14, 44, 444)'
    dbString = request.json['data'] 
    print(dbString)

    c.execute(dbString)
    dbConnection.commit()  
        
    response = make_response("Measurement written into DB", 200)
    #response.headers["Content-Type"] = "application/json"
    return response

