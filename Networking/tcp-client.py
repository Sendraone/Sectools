import socket
import sys

if len(sys.argv) > 1:
        print "Please enter target web-page.";

t_host= sys.argv[1]
t_port= 80

#Create a socket
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Create the client
cli.connect((t_host,t_port))

#send some data
cli.send("GET / HTTP/1.1\r\nHost: test.com\r\n\r\n")

#receive  data
response = cli.recv(4096)

print response
