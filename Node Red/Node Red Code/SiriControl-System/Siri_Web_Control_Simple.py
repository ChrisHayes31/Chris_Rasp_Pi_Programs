from socket import socket
import sys
BUFFER = str(sys.argv)
print("-received- ",str(sys.argv))
sock = socket()
sock.connect(('192.168.1.115', 4056))
#BUFFER = "Hello world!\n"
sock.send(BUFFER.encode(encoding='utf-8'))
sock.close()
