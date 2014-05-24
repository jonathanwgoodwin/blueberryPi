#!/usr/bin/python

import subprocess
import sys

def get_rssi():
    proc = subprocess.Popen("python check_rssi.py",
              stdout=subprocess.PIPE,
              stderr=subprocess.STDOUT,
              shell=True)
    proc.wait()
    f = open('./bluetooth.status', 'w')
    for line in iter (proc.stdout.readline, ''):
        if line[0:4] == "RSSI":
            f.write(line.split('[')[1].split(']')[0])
            f.close()

while True:
    get_rssi()


