#!/usr/bin/python

# About half of this (the part that's not integrated w/ bluetooth, is lifed from here: https://github.com/pranav/pyblaster
import urllib2
import json
import time
RED_GPIO = 23
BLUE_GPIO = 24
GREEN_GPIO = 18
GPIOS = [RED_GPIO, BLUE_GPIO, GREEN_GPIO]
FIFO = open('/dev/pi-blaster', 'w', buffering=0)


THRESHOLD = -100

def set(gpio, value):
    s = '%s=%s\n' % (gpio, value)
    FIFO.write(s)

def set_all(val):
    for each in GPIOS:
         set(each, val)

def lightctl():
     response = urllib2.urlopen('http://localhost:5000/strength')
     on = PREVENT_FUCKING_FLAPPING(json.load(response)['strength'])

     if on:
          set(RED_GPIO,1)
          set(GREEN_GPIO,.7)
          set(BLUE_GPIO,0)
     else:
         set_all(1)

def PREVENT_FUCKING_FLAPPING(STR):
    data = json.load(urllib2.urlopen('http://potato:5984/bluetooth_metrics/_design/timed_docs/_view/docs_w_dates?descending=true&limit=1'))
    STR = data['rows'][0]['value']['bluetooth_strength']
    print STR
    return STR > THRESHOLD

# wat
while True:
    lightctl()
    time.sleep(3)
