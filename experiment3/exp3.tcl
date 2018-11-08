#Create a simulator object
set ns [new Simulator]

#ns exp3.tcl Reno/SACK DropTail/RED

#set TCP variant & queuing discipline from commandline
set variant [lindex $argv 0]
set queue [lindex $argv 1]
set filename ${variant}_${queue}

#Open the trace file (before you start the experiment!)
set tf [open ${filename}.tr w]
$ns trace-all $tf

#Define colors for different data flows
$ns color 1 Blue
$ns color 2 Red

#Open the NAM trace file
set nf [open ${filename}.nam w]
$ns namtrace-all $nf

#Define a 'finish' procedure
proc finish {} {
        global ns nf tf
        $ns flush-trace
        #Close the NAM trace file
        close $nf
        #Close the trace file (after you finish the experiment!)
        close $tf
        #Execute NAM on the trace file
        #exec nam out.nam &
        exit 0
}

#Create 6 nodes
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]

#Create links between the nodes
#crete links for the nodes
if {$queue eq "DropTail"} {
        $ns duplex-link $n1 $n2 10Mb 10ms DropTail
        $ns duplex-link $n5 $n2 10Mb 10ms DropTail
        $ns duplex-link $n2 $n3 10Mb 10ms DropTail
        $ns duplex-link $n4 $n3 10Mb 10ms DropTail
        $ns duplex-link $n6 $n3 10Mb 10ms DropTail
} elseif {$queue eq "RED"} {
        $ns duplex-link $n1 $n2 10Mb 10ms RED
        $ns duplex-link $n5 $n2 10Mb 10ms RED
        $ns duplex-link $n2 $n3 10Mb 10ms RED
        $ns duplex-link $n4 $n3 10Mb 10ms RED
        $ns duplex-link $n6 $n3 10Mb 10ms RED
}

#set queue size
$ns queue-limit $n1 $n2 15
$ns queue-limit $n5 $n2 15
$ns queue-limit $n2 $n3 15
$ns queue-limit $n4 $n3 15
$ns queue-limit $n6 $n3 15

#Give node position (for NAM)
$ns duplex-link-op $n1 $n2 orient right-down
$ns duplex-link-op $n5 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n3 $n4 orient right-up
$ns duplex-link-op $n3 $n6 orient right-down

#create UDP client at n5 and sink at n6
set udp [new Agent/UDP]
$ns attach-agent $n5 $udp
set null [new Agent/Null]
$ns attach-agent $n6 $null

#create the datalink from n5 to n6 with Red color
$ns connect $udp $null
$udp set fid_ 2

#Setup a CBR over UDP connection
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
$cbr set rate_ 5mb
$cbr set random_ false

#set a TCP
if {$variant == "Reno"} {
        set tcp [new Agent/TCP/Reno]
        set sink [new Agent/TCPSink]
} elseif {$variant == "SACK"} {
        set tcp [new Agent/TCP/Sack1]
        set sink [new Agent/TCPSink/Sack1]
}

#attach tcp at n1
$ns attach-agent $n1 $tcp
$ns attach-agent $n4 $sink
$tcp set fid_ 1
$tcp set window_ 200

#create the datalink from n1 to n2 with Blue color
$ns connect $tcp $sink

#Setup a FTP over TCP connection
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

#Schedule events for the CBR agents
$ns at 0 "$ftp start"
$ns at 2 "$cbr start"
$ns at 7 "$cbr stop"
$ns at 9 "$ftp stop"

#Call the finish procedure after 5 seconds of simulation time
$ns at 10 "finish"

#Print CBR packet size and interval
#puts "CBR packet size = [$cbr set packet_size_]"
#puts "CBR interval = [$cbr set interval_]"

#Run the simulation
$ns run
