from flask import Flask
from datetime immport datetime
app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    return f"Hello from 13521107 on {now.strftime("%H:%M:%S")}!"
