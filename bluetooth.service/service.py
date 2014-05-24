#!/user/bin/python
from flask import Flask
import subprocess
app = Flask(__name__)

strength = -100

def get_rssi():
    proc = subprocess.Popen("python check_rssi.py",
              stdout=subprocess.PIPE,
              stderr=subprocess.STDOUT,
              shell=True)
    proc.wait()
    for line in iter (proc.stdout.readline, ''):
        if line[0:4] == "RSSI":
            strength = int(line.split('[')[1].split(']')[0])

while True:
    get_rssi()



@app.route("/")
def welcome():
    return "welcome to blueberry"


@app.route("/strength")
def strength():
    return strength
