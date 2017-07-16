import socket
import sys

if len(sys.argv) > 1:
        print "Please enter target web-page.";

target_host= sys.argv[1]
target_port= 80

#Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Create the client
client.connect((target_host,target_port))

#send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print response
