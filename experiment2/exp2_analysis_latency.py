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

def avg_rtts(atts_dict):
    """
    Return the average rtt in ms of the atts
    in the given dict, as latency, in milliseconds
    """
    total = 0.0
    bad_rtts = 0
    for k, v in atts_dict.items():
        if v[0] and v[1]:
            total += (v[1] - v[0])
        else:
            # print 'Packet: %s has null ack time: %s' % (k, tuple(v))
            bad_rtts += 1
    # print 'From rtts dict: %d packets has null ack time' % bad_rtts
    num_valid_rtts = len(atts_dict.items()) - bad_rtts
    avg_rtts = (total / num_valid_rtts) * 1000
    return avg_rtts

# file scope constants
receive = 'r'
enqueue = '+'
dequeue = '-'
drop = 'd'
delimiter = ' '
time_pairs_1 = {}
total_packet_number_1 = 0
time_pairs_2 = {}
total_packet_number_2 = 0

# ./exp2_analysis_latency.py ./RenoReno/Reno_Reno_1.tr

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    assert False

print 'processing exp2 file for latency: %s' % filename
# function scope constants
tcp_fid_1 = '1'
tcp_src_node_1 = '0'
tcp_sink_node_1 = '3'
tcp_fid_2 = '2'
tcp_src_node_2 = '4'
tcp_sink_node_2 = '5'

with open(filename, 'r') as f:
    for line in f:
        fields = line.split()
        # grab tcp events according to the flow id
        if fields[7] == tcp_fid_1:
            # a tcp packet enque (send) event
            if fields[0] == enqueue:
                if fields[2] == tcp_src_node_1 and fields[4] == 'tcp':
                    if fields[10] not in time_pairs_1:
                        time_pairs_1[fields[10]] = [float(fields[1]), None]
            # a tcp packet recv event
            if fields[0] == receive:
                if fields[3] == tcp_src_node_1 and fields[4] == "ack":
                    if time_pairs_1.has_key(fields[10]):
                        time_pairs_1[fields[10]][1] = float(fields[1])
        if fields[7] == tcp_fid_2:
            # a tcp packet enque (send) event
            if fields[0] == enqueue:
                if fields[2] == tcp_src_node_2 and fields[4] == 'tcp':
                    if fields[10] not in time_pairs_2:
                        time_pairs_2[fields[10]] = [float(fields[1]), None]
            # a tcp packet recv event
            if fields[0] == receive:
                if fields[3] == tcp_src_node_2 and fields[4] == "ack":
                    if time_pairs_2.has_key(fields[10]):
                        time_pairs_2[fields[10]][1] = float(fields[1])

# convert latency, in ms
final_latency_1 = avg_rtts(time_pairs_1)
final_latency_2 = avg_rtts(time_pairs_2)

print "final latency for n1 -> n4 is: %s" % str(final_latency_1)
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "final latency for n5 -> n6 is: %s" % str(final_latency_2)
