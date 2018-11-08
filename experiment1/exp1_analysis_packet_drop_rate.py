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

# file scope constants
receive = 'r'
enqueue = '+'
dequeue = '-'
drop = 'd'
delimiter = ' '
filename = ""

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    assert False

print 'processing exp1 file for packet drop rate: %s' % filename
# function scope constants
tcp_fid = '1'

# function scope refs
total_send_packets_number = 0;
total_received_packets_number = 0;

with open(filename, 'r') as f:
    for line in f:
        fields = line.split()
        # grab tcp events according to the flow id
        if fields[7] == tcp_fid:
            if (fields[0] == enqueue):
                total_send_packets_number += 1
            if (fields[0] == receive):
                total_received_packets_number += 1

# convert packet drop rate, in a%
packet_drop_rate = (total_send_packets_number - total_received_packets_number) * 1.0 * 100 / total_send_packets_number

print "final packet drop rate for %s is: %s" % (filename, str(packet_drop_rate))
