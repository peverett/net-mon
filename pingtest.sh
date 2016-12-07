#!/bin/bash
#
# Run ping for a count of 60 (~60 seconds) - Store the results in a file with 
# date and time appended to the file-name.

tdnow=`date '+%y%m%d-%H%M'`;
filename="/home/pi/results/pingtest.$tdnow"

ping 8.8.8.8 -c 60 > $filename
