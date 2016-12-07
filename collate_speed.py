#!/usr/python
"""
Looks for all files with the filename 'speedtest.<date>-<time>', for example
'speedtest.161114-1920'.

Extrat the download and upload speed in mbits and then add to a CSV format 
file.
"""

SPEEDTEST_FN= "speedtests.csv"

import glob

SPEEDTEST_FILES = glob.glob("speedtest.*")
SPEEDTEST_FILES.sort()

with open(SPEEDTEST_FN, "w") as stfh:

    stfh.write("Time, Download, Upload\n")

    for fn in SPEEDTEST_FILES:
        ts_hrs = fn[-4:-2]
        ts_mns = fn[-2:]
        
        download = 0
        upload = 0
        with open(fn) as infh:
            for line in infh.readlines():
                if line.startswith("Download:"):
                    chunks=line.split(" ")
                    download = chunks[1]
                elif line.startswith("Upload:"):
                    chunks=line.split(" ")
                    upload = chunks[1]

        stfh.write("{}:{}, {}, {}\n".format(ts_hrs, ts_mns, download, upload))
    
print("All done. Goodbye.")

