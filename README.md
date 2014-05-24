blueberryPi
===========

Bluetooth stuff for my RaspberryPi project(s)


I stole the check_rssi script from someone here [http://stackoverflow.com/....](http://stackoverflow.com/questions/7628758/linux-bluetooth-l2ping-with-signal-strength-without-connecting).

I am currently kind of sad because polling takes 10s. Should be some way to get this down so the app is more responsive to changes in signal strength.


Notes
=====

/usr/bin/bluez-simple-agent:
  capability = "DisplayYesNo"
  
because otherwise everything fails...
