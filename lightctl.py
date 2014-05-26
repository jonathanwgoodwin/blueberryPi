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
LAST_STATUS = True

THRESHOLD = -85

def set(gpio, value):
    s = '%s=%s\n' % (gpio, value)
    FIFO.write(s)

def set_all(val):
    for each in GPIOS:
         set(each, val)

def lightctl(last_status):
     on = PREVENT_FUCKING_FLAPPING(last_status)

     if on:
          set(RED_GPIO,1)
          set(GREEN_GPIO,.7)
          set(BLUE_GPIO,0)
     else:
         set_all(1)

     return on

def PREVENT_FUCKING_FLAPPING(last_status):
    data = json.load(urllib2.urlopen('http://potato:5984/bluetooth_metrics/_design/timed_docs/_view/docs_w_dates?descending=true&limit=5'))
    str_list = []
    threshold_count = {'on' : 0 , 'off' : 0 }
    for each in data['rows']:
        strength = int(each['value']['bluetooth_strength'])
        str_list.append(strength)
        if strength > THRESHOLD:
            threshold_count['on'] = threshold_count['on'] + 1
        else:
            threshold_count['off'] = threshold_count['off'] + 1

    STR = str_list[0]
    if STR > THRESHOLD:
        # it should be on
        print 'Lights on, str: %s' % ( STR )
        return True
    if STR < THRESHOLD and not LAST_STATUS:
        # it should be off; and it was off last time
        print 'Lights off, str: %s' % ( STR )
        return False
    if STR < THRESHOLD and LAST_STATUS:
        # it should probably be off; but it was on last time
        if threshold_count['on'] > threshold_count['off']:
            # more on's in the last 5 than offs
            # it should probably just be on
            print 'Lights on, vote on: %d off: %d str: %s' % ( threshold_count['on'], threshold_count['off'], STR )
            return True
        else:
            # more offs; therefor SHUT IT DOWN
            print 'lights off, vote on: %d off: %d str: %s' % ( threshold_count['on'], threshold_count['off'], STR )
            return False


# wat
while True:
    LAST_STATUS = lightctl(LAST_STATUS)
    time.sleep(3)
