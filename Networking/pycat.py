import sys
import socket
import getopt
import threading
import subprocess

listen      = False
command     = False
upload      = False
execute     = ""
target      = ""
upload_destination = ""
port        = 0

def usage ():
    print "Pycat Tool"
    print
    print "Usage: pycat.py -t target host -p port"
    print "-l  --listen                 - listen on [host]:[port] for incoming
                                            connections"
    print "-e --execute=file_to_run     - execute the given file upon receiving
                                            a connection"
    print "-c --command                 - Initialize command shell"
    print ""
