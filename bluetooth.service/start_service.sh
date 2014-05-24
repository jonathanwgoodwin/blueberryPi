#!/bin/bash
python service.py &> service.out & 
python web.py &> web.out &
