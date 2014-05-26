#!/bin/bash
python lightctl.py > lightctl.out &
cd bluetooth.service
python service.py > service.out &
