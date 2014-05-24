#!/bin/bash
python service.py & 
python web.py &> web.out &
