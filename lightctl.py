#!/usr/bin/python
import urllib2
import json
import time
RED_GPIO = 18
BLUE_GPIO = 23
GREEN_GPIO = 24


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
     print type(strength)
     if strength >= -70:
          set_all(0)
     else:
         set_all(1)



while True:
    lightctl()
    time.sleep(3)
