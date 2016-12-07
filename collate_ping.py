#!/usr/python
"""
Looks for all files with the filename 'pingtest.<date>-<time>', for example
'pingtest.161114-1920'.

Extract the last two lines from the file, which look like this:

    60 packets transmitted, 60 received, 0% packet loss, time 59088ms
    rtt min/avg/max/mdev = 11.353/13.905/52.077/5.304 ms

Extract the packet loss and add/append it to a CSV file listing packet loss by
time.

Extractthe min/avg/max/mdev ping times and store them in a separate CSV file.
"""

PACKET_LOSS_FN = "packet_loss.csv"
PING_TIMES_FN = "ping_times.csv"

import glob
import re

PINGTEST_FILES = glob.glob("pingtest.*")
PINGTEST_FILES.sort()

def last_lines(filename):
    "Read the file and return the last two lines"
    with open(filename) as fh:
        lines = fh.readlines()
        return lines[-2:]


with open(PACKET_LOSS_FN, "w") as plfh, open(PING_TIMES_FN, "w") as ptfh:

    ptfh.write("Time, Min, Avg, Max, MDev\n")
    plfh.write("TIme, PLoss\n")

    for fn in PINGTEST_FILES:
        ts_hrs = fn[-4:-2]
        ts_mns = fn[-2:]

        lines = last_lines(fn)

        res = re.search("\d+%", lines[0])
        if res:

            plfh.write("{}:{}, {}\n".format(ts_hrs, ts_mns, res.group(0)))

            # If there is 100% packet loss the other stats are meaningless.
            if (res.group(0) == "100%"):
                ptfh.write("{}:{} 0, 0, 0, 0\n".format(ts_hrs, ts_mns))
            else:
                chunks = lines[1].strip().split(" ")
                values = chunks[3].split("/")
                ptfh.write("{}:{}, {}, {}, {}, {}\n".format(
                    ts_hrs, ts_mns,
                    values[0], values[1], values[2], values[3]))
    
print("All done. Goodbye.")

