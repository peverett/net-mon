#!/bin/bash
#
# Run speedtest-cli and store the results in a file with the date and time
# appended to the file-name.

tdnow=`date '+%y%m%d-%H%M'`;
filename="/home/pi/results/speedtest.$tdnow"

python /usr/local/lib/python2.7/dist-packages/speedtest_cli.py > $filename
