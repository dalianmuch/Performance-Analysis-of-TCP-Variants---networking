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
time_pairs = {}
total_packet_number = 0

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    assert False

print 'processing exp1 file for latency: %s' % filename
# function scope constants
tcp_fid = '1'
tcp_src_node = '0'
tcp_sink_node = '3'

with open(filename, 'r') as f:
    for line in f:
        fields = line.split()
        # grab tcp events according to the flow id
        if fields[7] == tcp_fid:
            # a tcp packet enque (send) event
            if fields[0] == enqueue:
                if fields[2] == tcp_src_node and fields[4] == 'tcp':
                    if fields[10] not in time_pairs:
                        time_pairs[fields[10]] = [float(fields[1]), None]
            # a tcp packet recv event
            if fields[0] == receive:
                if fields[3] == tcp_src_node and fields[4] == "ack":
                    if time_pairs.has_key(fields[10]):
                        time_pairs[fields[10]][1] = float(fields[1])


# convert latency, in ms
final_latency = avg_rtts(time_pairs)

print "final latency for %s is: %s" % (filename, str(final_latency))
