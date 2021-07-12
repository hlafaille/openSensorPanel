import os

from flask import Flask, render_template

from werkzeug.utils import redirect

from SensorData import CPU, RAM, GPU, Network
import config

#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)
app = Flask(__name__)

Net = Network.NetTest()
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


@app.route('/diskUsage')
def diskUsage():
    return RAM.diskUsage()


@app.route('/gpuTemp')
def gpuTemp():
    return GPU.temp()


@app.route('/netPing')
def netPing():
    return Net.ping()


@app.route('/netDownload')
def netDownload():
    return Net.download()


@app.route('/netUpload')
def netUpload():
    return Net.upload()


@app.route('/update/')
def update():
    updateLog = ["Looking for updates...",
                 ]
    return render_template("update.html",
                           version=config.MAIN['VERSION'],
                           updateLog=updateLog,
                           )

@app.route('/setting/')
def settings():
    if os.name == "nt":
        os.system("config.py")
    if os.name == "posix":
        os.system("xdg-open config.py")
    return redirect("http://127.0.0.1:5000/", code=302)



if __name__ == "__main__":
    #webbrowser.open("127.0.0.1:5000", new=1, autoraise=True)
    app.run(debug=True)
