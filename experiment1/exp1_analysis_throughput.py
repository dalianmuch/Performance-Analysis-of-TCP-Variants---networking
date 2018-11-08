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
throughput = 0

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    assert False

print 'processing exp1 file for throughput: %s' % filename
# function scope constants
tcp_fid = '1'
tcp_src_node = '0'
tcp_sink_node = '3'

# function scope refs
total_bits_received_by_receiver_node = 0
first_packet_sent_time = 10000
last_packet_received_time = -1

with open(filename, 'r') as f:
    for line in f:
        fields = line.split()
        # grab tcp events according to the flow id
        if fields[7] == tcp_fid:
            # a tcp packet enque (send) event
            if fields[0] == enqueue:
                first_packet_sent_time = min(first_packet_sent_time, float(fields[1]))

            # a tcp packet recv event
            if fields[0] == receive:
                last_packet_received_time = max(last_packet_received_time, float(fields[1]))

                # if it is a tcp packet recved by tcp sink node
                if fields[3] == tcp_sink_node:
                    # record packet size to throughput
                    throughput += int(fields[5]) * 8
                # a tcp src node recv (ack) event
                elif fields[3] == tcp_src_node and fields[4] == 'ack':
                    throughput += int(fields[5]) * 8

# convert throughput, in Mbps
seconds_passed = last_packet_received_time - first_packet_sent_time
final_throughput = (float(throughput) / (1024.0 * 1024.0)) / (seconds_passed)

print "final throughput for %s is: %s" % (filename, str(final_throughput))
