from flask import Flask, render_template, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DATABASE_URL will contain the database connection string:
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
# Connects to the database using the app config
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/index')
def test_index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

