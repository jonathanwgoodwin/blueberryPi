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


PREV_STR = [1]
LAST_STATUS = 'off'
THRESHOLD = -100

def set(gpio, value):
    s = "%s=%s\n" % (gpio, value)
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
    STATUS_LIST = [STR] + PREV_STR
    STATUS = { 'on' : 0, 'off' : 0 }
    if len(PREV_STR) > 5:
        PREV_STR.pop(0)
        PREV_STR.append(STR)

    if STR > THRESHOLD:
        return True
    else:
        for strength in STATUS_LIST:
            if strength > THRESHOLD:
                STATUS['on']=STATUS['on'] + 1
            else:
                STATUS['off']=STATUS['off'] + 1

        return STATUS['on'] > STATUS['off']

# wat
while True:
    lightctl()
    time.sleep(3)
