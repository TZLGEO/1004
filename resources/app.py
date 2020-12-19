from flask import Flask, render_template, jsonify, request, redirect
from sqlalchemy import create_engine, inspect, MetaData, Table
from sqlalchemy import Column, Integer, String, DateTime
import subprocess
import os
import json
import get_data as gt

# initialize the flask app
app = Flask(__name__)

#connect to db
DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)

# renders our html
@app.route('/')
def hello():
    return render_template("index.html")

# returns or responds with data for the songs that 
# top the chart with their count
@app.route('/chartstay')
def chart_stay():
    res = gt.stay_on_chart(engine)
    return jsonify(res)

# returns or responds with data for the #1 songs that 
# top the chart with their count  
@app.route('/charttopstay')
def chart_top_stay():
    res = gt.no1_on_chart(engine)
    return jsonify(res)

# when called will return a particu;ar no. of rows
# example "/data/100" will return 100 rows of our data
@app.route('/data/<rows>')
def test_data(rows):
    rows=int(rows)
    res = gt.get_data(engine, rows)
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)

