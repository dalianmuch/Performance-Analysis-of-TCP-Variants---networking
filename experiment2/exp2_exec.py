#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import subprocess

# ./exp2_exec.py createdata Reno Reno
# ./exp2_exec.py analysis NewReno Reno throughput
task = ""
tcp1 = ""
tcp2 = ""
type = ""
dataname = ""
scriptname = ""


if len(sys.argv) == 4:
    if sys.argv[1] == "createdata":
        task = sys.argv[1]
        tcp1 = sys.argv[2]
        tcp2 = sys.argv[3]

if len(sys.argv) == 5:
    if sys.argv[1] == "analysis":
        task = sys.argv[1]
        tcp1 = sys.argv[2]
        tcp2 = sys.argv[3]
        type = sys.argv[4]

dataname = "./%s%s/%s_%s_" % (tcp1, tcp2, tcp1, tcp2)
print "dataname: " + dataname

if type == "throughput" or type == "packet_drop_rate" or type == "latency":
    scriptname = "./exp2_analysis_%s.py" % (type)

print "scriptname: " + scriptname

# ns exp2.tcl Reno Reno 1
if task == "createdata":
    for i in range(1,11):
        cmd = "ns exp2.tcl %s %s " % (tcp1, tcp2) + str(i)
        print cmd
        try:
            print subprocess.call(cmd, shell=True)
        except OSError as e:
            print "Error Happening!!"
            print e

if task == "analysis":
    for i in range(1,11):
        new_tr_file = dataname + str(i) + ".tr"
        cmd = scriptname + " " + new_tr_file
        try:
            print subprocess.call(cmd, shell=True)
        except OSError as e:
            print "Error Happening!!"
            print e
