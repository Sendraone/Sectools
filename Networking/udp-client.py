import socket
import sys

if len(sys.argv) > 2:
        print "Please enter target web-page.";

t_host= sys.argv[1]
t_port= int(sys.argv[2])

#print "Arg 1:", (target_host)
#print "Arg 2:", (target_port)

#Create a socket
cli= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send  data
cli.sendto("THISISATEST",(t_host,t_port))

#receive  data
data, addr = cli.recvfrom(4096)

print data
