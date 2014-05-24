#!/bin/bash
arr[0]=18
arr[1]=23
arr[2]=24
for each in 0 1 2
do
	echo  "${arr[each]}=0"
	echo  "${arr[each]}=0" >/dev/pi-blaster
done
