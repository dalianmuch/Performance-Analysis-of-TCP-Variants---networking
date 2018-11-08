#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

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

# ./exp2_analysis_throughput.py ./RenoReno/Reno_Reno_1.tr

# file scope constants
receive = 'r'
enqueue = '+'
dequeue = '-'
drop = 'd'
delimiter = ' '
filename = ""
throughput_1 = 0
throughput_2 = 0

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    assert False

print 'processing exp2 file for throughput: %s' % filename
# function scope constants
tcp_id_1 = 0
tcp_fid_1 = '1'
tcp_src_node_1 = '0'
tcp_sink_node_1 = '3'

tcp_id_2 = 1
tcp_fid_2 = '2'
tcp_src_node_2 = '4'
tcp_sink_node_2 = '5'
rtts = [{}, {}]

with open(filename, 'r') as f:
    for line in f:
        fields = line.split()
        # grab tcp events according to the flow id
        if fields[7] == tcp_fid_1:
            # a tcp packet enque (send) event
            if fields[0] == enqueue:
                if fields[2] == tcp_src_node_1 and fields[4] == "tcp":
                    if fields[10] not in rtts[tcp_id_1]:
                        rtts[tcp_id_1][fields[10]] = [float(fields[1]), None]

            # a tcp packet recv event
            if fields[0] == receive:
                # if it is a tcp packet recved by tcp sink node
                if fields[3] == tcp_sink_node_1:
                    # record packet size to throughput
                    throughput_1 += int(fields[5]) * 8
                # a tcp src node recv (ack) event
                elif fields[3] == tcp_src_node_1 and fields[4] == 'ack':
                    if fields[10] in rtts[tcp_id_1]:
                        rtts[tcp_id_1][fields[10]][1] = float(fields[1])
                        throughput_1 += int(fields[5]) * 8

        if fields[7] == tcp_fid_2:
            # a tcp packet enque (send) event
            if fields[0] == enqueue:
                if fields[2] == tcp_src_node_2 and fields[4] == "tcp":
                    if fields[10] not in rtts[tcp_id_2]:
                        rtts[tcp_id_2][fields[10]] = [float(fields[1]), None]

            # a tcp packet recv event
            if fields[0] == receive:
                # if it is a tcp packet recved by tcp sink node
                if fields[3] == tcp_sink_node_2:
                    # record packet size to throughput
                    throughput_2 += int(fields[5]) * 8
                # a tcp src node recv (ack) event
                elif fields[3] == tcp_src_node_2 and fields[4] == 'ack':
                    if fields[10] in rtts[tcp_id_2]:
                        rtts[tcp_id_2][fields[10]][1] = float(fields[1])
                        throughput_2 += int(fields[5]) * 8

# convert throughput, in Mega bits
final_throughput_1 = float(throughput_1) / (1024.0 * 1024.0)
final_throughput_2 = float(throughput_2) / (1024.0 * 1024.0)

print "final throughput for n1 -> n4 is: %s" % (str(final_throughput_1))
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "final throughput for n5 -> n6 is: %s" % (str(final_throughput_2))
