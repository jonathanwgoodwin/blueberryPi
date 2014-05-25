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

def set(gpio, value):
    s = "%s=%s\n" % (gpio, value)
    FIFO.write(s)

def set_all(val):
    for each in GPIOS:
         set(each, val)

def lightctl():
     response = urllib2.urlopen('http://localhost:5000/strength')
     strength = json.load(response)['strength']
     if strength >= -100:
          set(RED_GPIO,1)
          set(GREEN_GPIO,.3)
          set(BLUE_GPIO,0)
     else:
         set_all(1)

# wat
while True:
    lightctl()
    time.sleep(3)
