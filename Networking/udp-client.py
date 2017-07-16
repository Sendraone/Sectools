import socket
import sys

if len(sys.argv) > 2:
        print "Please enter target web-page.";

target_host= sys.argv[1]
target_port= int(sys.argv[2])

#print "Arg 1:", (target_host)
#print "Arg 2:", (target_port)

#Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto("THISISATEST",(target_host,target_port))

#receive some data
data, addr = client.recvfrom(4096)

print data
