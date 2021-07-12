from datetime import datetime

import psutil
from elevate import elevate
from flask import Flask, render_template
from SensorData import CPU, RAM
import config

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", windowTitle=config.MAIN['WINDOW_TITLE'], cpuModel=CPU.name())

@app.route('/cpuLoad')
def cpuLoad():
    return CPU.load()

@app.route('/cpuTemp')
def cpuTemp():
    return CPU.temp()

@app.route('/cpuFreq')
def cpuFreq():
    return CPU.frequency()

@app.route('/ramTotal')
def ramTotal():
    return RAM.total()

@app.route('/ramAvailable')
def ramAvailable():
    return RAM.available()

if __name__ == "__main__":
    app.run(debug=True)
