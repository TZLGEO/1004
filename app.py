from flask import Flask, render_template, jsonify, request, redirect
from sqlalchemy import create_engine, inspect, MetaData, Table
from sqlalchemy import Column, Integer, String, DateTime
import subprocess
import os
import json
import pandas as pd
import get_data as gt

app = Flask(__name__)

DATABASE_URL = subprocess.check_output("heroku config:get DATABASE_URL --app billboardchart2", shell=True).decode('utf-8')
engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)
billboard_df = pd.read_sql_table("billboard_chart", con=engine)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/chartstay')
def chart_stay():

    res = gt.stay_on_chart
    return jsonify(json.loads(res))
    
@app.route('/charttopstay')
def chart_top_stay():

    res = gt.no1_on_chart()
    return jsonify(json.loads(res))
    

@app.route('/data/<rows>')
def test_data(rows):
    rows=int(rows)

    res = gt.get_data(billboard_df, rows)
    return jsonify(json.loads(res))


if __name__ == '__main__':
    app.run(debug=True)

