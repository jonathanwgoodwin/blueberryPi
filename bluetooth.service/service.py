#!/usr/bin/python
# This is disgusting, but it works
import subprocess
import sys
import couchdb
from datetime import datetime

Empty_Tracker = 0

def get_rssi(count):
    found_strength = False
    proc = subprocess.Popen("python check_rssi.py",
              stdout=subprocess.PIPE,
              stderr=subprocess.STDOUT,
              shell=True)
    proc.wait()
    db = couchdb.Server(url='http://potato:5984')['bluetooth_metrics']
    lines = proc.stdout.readlines()
    print lines
    for line in lines:
        if line[0:4] == "RSSI":
            STR = line.split('[')[1].split(']')[0]
            doc = {'bluetooth_strength' : STR, 'time' : str(datetime.now()) }
            doc_id, doc_rev = db.save(doc)
            print doc
            found_strength = True
            print 'count at %d' % ( count )

        else:
            count = count + 1
            if count > 15:
                doc = {'bluetooth_strength' : -200, 'time' : str(datetime.now()) }
                doc_id, doc_rev = db.save(doc)
                print doc
                print 'count at %d' % ( count )
    if not found_strength:
        print 'setting count to %d' % ( count )
        return count
    else:
        print 'setting count to %d' % ( 0 )
        return 0



while True:
    print 'starting Empty_Tracker at %d' % ( Empty_Tracker )
    Empty_Tracker = get_rssi(Empty_Tracker)


