#Create a simulator object
set ns [new Simulator]

#set TCP variant & CBR rate from command line
set variant1 [lindex $argv 0]
set variant2 [lindex $argv 1]
set cbrrate [lindex $argv 2]
set filename ${variant1}_${variant2}_${cbrrate}

#Open the trace file (before you start the experiment!)
set tf [open ${filename}.tr w]
$ns trace-all $tf

#Define colors for different data flows
$ns color 1 Blue
$ns color 2 Red
$ns color 3 Green

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
$ns duplex-link $n1 $n2 10Mb 10ms DropTail
$ns duplex-link $n5 $n2 10Mb 10ms DropTail
$ns duplex-link $n2 $n3 10Mb 10ms DropTail
$ns duplex-link $n3 $n4 10Mb 10ms DropTail
$ns duplex-link $n3 $n6 10Mb 10ms DropTail

# set the queue size on the critical path
$ns queue-limit $n2 $n3 10

#Give node position (for NAM)
$ns duplex-link-op $n1 $n2 orient right-down
$ns duplex-link-op $n5 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n3 $n4 orient right-up
$ns duplex-link-op $n3 $n6 orient right-down

#create UDP client at n2 and sink at n3
set udp [new Agent/UDP]
$ns attach-agent $n2 $udp
set null [new Agent/Null]
$ns attach-agent $n3 $null
$udp set fid_ 3
$ns connect $udp $null

#Setup a CBR over UDP connection
set cbr [new Application/Traffic/CBR]
$cbr set rate_ ${cbrrate}mb
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
$cbr set random_ false

#set first TCP for n1
if {$variant1 == "Tahoe"} {
	set tcp1 [new Agent/TCP]
} elseif {$variant1 == "Reno"} {
	set tcp1 [new Agent/TCP/Reno]
} elseif {$variant1 == "NewReno"} {
	set tcp1 [new Agent/TCP/Newreno]
} elseif {$variant1 == "Vegas"} {
	set tcp1 [new Agent/TCP/Vegas]
}

#attach first tcp at n1
$ns attach-agent $n1 $tcp1

#set Vegas parameter, in this configuration Vegas tries to keep between 1 and 3 packet queueed in the network
if {$variant1 == "Vegas"} {
	$tcp1 set v_alpha_ 1
	$tcp1 set v_beta_ 3
}

#create TCP sink at n4
set sink1 [new Agent/TCPSink]
$ns attach-agent $n4 $sink1

#create the datalink from n1 to n2 with Blue color
$ns connect $tcp1 $sink1
$tcp1 set fid_ 1

#Setup a FTP over TCP connection
set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp1 set type_ FTP

#set second TCP for n5
if {$variant2 == "Tahoe"} {
	set tcp2 [new Agent/TCP]
} elseif {$variant2 == "Reno"} {
	set tcp2 [new Agent/TCP/Reno]
} elseif {$variant2 == "NewReno"} {
	set tcp2 [new Agent/TCP/Newreno]
} elseif {$variant2 == "Vegas"} {
	set tcp2 [new Agent/TCP/Vegas]
}

#attach first tcp at n5
$ns attach-agent $n5 $tcp2

#set Vegas parameter, in this configuration Vegas tries to keep between 1 and 3 packet queueed in the network
if {$variant2 == "Vegas"} {
	$tcp2 set v_alpha_ 1
	$tcp2 set v_beta_ 3
}

#create TCP sink at n4
set sink2 [new Agent/TCPSink]
$ns attach-agent $n6 $sink2

#create the datalink from n1 to n2 with Blue color
$ns connect $tcp2 $sink2
$tcp2 set fid_ 2

#Setup a FTP over TCP connection
set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp2
$ftp2 set type_ FTP

#Schedule events for the CBR agents
$ns at 0 "$cbr start"
$ns at 1 "$ftp1 start"
$ns at 1 "$ftp2 start"
$ns at 9 "$ftp1 stop"
$ns at 9 "$ftp2 stop"
$ns at 10 "$cbr stop"

#Call the finish procedure after 5 seconds of simulation time
$ns at 10 "finish"

#Print CBR packet size and interval
#puts "CBR packet size = [$cbr set packet_size_]"
#puts "CBR interval = [$cbr set interval_]"

#Run the simulation
$ns run
