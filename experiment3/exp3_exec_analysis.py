#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

# ./exp3_exec_analysis.py Reno/SACK DropTail/RED

"""
event = fields[0]
time = fields[1]
from_node = fields[2]
to_node = fields[3]
pkt_type = fields[4]
pkt_size = fields[5]
flags = fields[6]
flow_id = fields[7]
src_addr = fields[8]
dst_addr = fields[9]
seq_num = fields[10]
pkt_id = fields[11]
"""

# file scope constants
receive = 'r'
enqueue = '+'
dequeue = '-'
drop = 'd'
delimiter = ' '
filename = ""
agent = ""
queue = ""

if len(sys.argv) == 3:
    agent = sys.argv[1]
    queue = sys.argv[2]
else:
    assert False

filename = agent + "_" + queue

print 'processing exp3 file for analysis: %s' % filename
# function scope constants
tcp_fid = '1'
tcp_src_node = '0'
tcp_sink_node = '3'

tr_file = "./trs/%s_%s.tr" % (agent, queue)

print tr_file

# We will handle the trs file here

## rtts : {[sequenceNum] : [(first send time), (first ack received time)]}
rtts = {}
## tps : {[second] : [throughput]}
# second means a period
tps = {}

with open(tr_file, 'r') as f:
    for line in f:
        fields = line.split()
        ## if this flow is not tcp flow, continue it.
        if fields[7] != tcp_fid:
            continue

        # calculate throughput for each second
        # refactor
        # if it is an ack received by node 0, add package size into
        # throughput of this second
        # if it is an tcp received by node 3, add package size into
        # throughput of this second
        if fields[0] == receive and \
                ((fields[3] == tcp_src_node and fields[4] == 'ack') or \
                 (fields[3] == tcp_sink_node and fields[4] == 'tcp')):
            ## if this is an ack received by node 0;
            ## put timestamp into rtts's recv time part.
            if fields[3] == tcp_src_node and fields[10] in rtts:
                rtts[fields[10]][1] = float(fields[1])
            ## calculate the throughput
            timeindex = int(float(fields[1]))
            if timeindex in tps:
                tps[timeindex][0] += int(fields[5])
                tps[timeindex][1] += 1
            else:
                tps[timeindex] = [int(fields[5]), 1]
                continue

        ## if node 0 send this SeqNum package for the first time
        ## add a new rtt into rtts dict with seqNum as the key
        if fields[0] == enqueue and fields[2] == tcp_src_node and fields[10] not in rtts:
            rtts[fields[10]] = [float(fields[1]), None]
            continue

## save throughput file
## each file record format: <time bandwidth>
throughputfilename = filename + "_throughput"
throughputfile = open(throughputfilename, 'a')
throughput_template = '%f %f\n'
for key in tps:
    time = key + 0.5
    thp = tps[key][0] * 1.0 / (1024 * 1024) # Mega Bytes
    record = throughput_template % (time, thp)
    throughputfile.write(record)
throughputfile.close()

print throughputfilename

print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

latency_list = []

for key in rtts:
    if not rtts[key][1]:
        continue
    latency = rtts[key][1] - rtts[key][0]
    time = rtts[key][0] + latency / 2
    item = (time, latency * 1000)
    latency_list.append(item)

latency_list.sort(key=lambda tuple: tuple[0])

## save latency file
## each file record format: <time latency>
# latencyfilename = filename + "_latency"
# latencyfile = open(latencyfilename, 'a')
# latency_template = '%f %f\n'
# for item in latency_list:
#     record = latency_template % (item[0], item[1])
#     latencyfile.write(record)
# latencyfile.close()
#
# print latencyfilename

latencyfilenametime = filename + "_latency_time"
latencyfiletime = open(latencyfilenametime, 'a')
for item in latency_list:
    record = "%s\n" % item[0]
    latencyfiletime.write(record)
latencyfiletime.close()

print latencyfilenametime

latencyfilenamevalue = filename + "_latency_value"
latencyfilevalue = open(latencyfilenamevalue, 'a')
for item in latency_list:
    record = "%s\n" % item[1]
    latencyfilevalue.write(record)
latencyfilevalue.close()

print latencyfilenamevalue
