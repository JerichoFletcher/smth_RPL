from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, flask from 13521107 #1"
