#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import subprocess

# ./exec.py throughput Tahoe

analysis_file = ""
tr_file = ""

if len(sys.argv) == 3:
    if sys.argv[1] == "throughput":
        analysis_file = "./analysis_throughput.py"
    elif sys.argv[1] == "packet_drop_rate":
        analysis_file = "./analysis_packet_drop_rate.py"
    elif sys.argv[1] == "latency":
        analysis_file = "./analysis_latency.py"

    if sys.argv[2] == "Tahoe":
        tr_file = "Tahoe/Tahoe_"
    elif sys.argv[2] == "Reno":
        tr_file = "Reno/Reno_"
    elif sys.argv[2] == "NewReno":
        tr_file = "NewReno/NewReno_"
    elif sys.argv[2] == "Vegas":
        tr_file = "Vegas/Vegas_"

if analysis_file == "" or tr_file == "":
    assert False

for i in range(1,11):
    cmd = "" + analysis_file
    new_tr_file = tr_file + str(i) + ".tr"
    cmd = cmd + " " + new_tr_file
    print cmd
    try:
        print subprocess.call(cmd, shell=True)
    except OSError as e:
        print "Error Happening!!"
        print e
