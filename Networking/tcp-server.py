import socket
import threading

bind_ip_addr = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip_addr,bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip_addr,bind_port)

def handle_cli(client_socket):
    request = cli_socket.recv(1024)
    print "[*] Received: %s" % request
    cli_socket.send("ACK!")

    cli_socket.close()

while True:
    cli,addr = server.accept()
    print "[*] Accepted connection from %s:%d " % (addr[0],addr[1])

    cli_handler = threading.Thread(target = handle_client,args=(cli,))
    cli_handler.start()
