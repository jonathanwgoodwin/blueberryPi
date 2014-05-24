#!/usr/bin/python
import threading
import subprocess
import check_rssi
import time

RED_GPIO = 18
BLUE_GPIO = 23
GREEN_GPIO = 24


GPIOS = [RED_GPIO, BLUE_GPIO, GREEN_GPIO]

FIFO = open('/dev/pi-blaster', 'w', buffering=0)

def set(gpio, value):
    s = "%s=%s\n" % (gpio, value)
    FIFO.write(s)

def get_rssi():
    proc = subprocess.Popen("python check_rssi.py",
              stdout=subprocess.PIPE,
              stderr=subprocess.STDOUT,
              shell=True)
    proc.wait()
    for line in iter (proc.stdout.readline, ''):
        if line[0:4] == "RSSI":
            rssi = int(line.split('[')[1].split(']')[0])
            if rssi > -70:
                print 'Strength %s, turning on lights' % str(rssi)
                for each in GPIOS:
                    set (each, 0)
            else:
                print "Strength too low: " +str(rssi)
                for each in GPIOS:
                    set (each, 1)

while True:
    get_rssi()
