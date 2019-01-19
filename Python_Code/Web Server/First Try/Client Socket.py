import socket
import sys
import time
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.170', 8089)
#server_address = ('localhost', 10000)
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    
    # Send data
    message1 = (b'http://192.168.1.170:8089/SetChannel.cgi?Channel=2')
    #message1 = (b'GET /SetChannel.cgi?Channel=1')
    message2 = b'HTTP/1.1 User-Agent : WebCamera'
    message3 = b'Host: 192.168.1.170:8089'
    message4 = b'If-Modified-Since: Mon, 10 Feb 2003 14:07:13 GMT; length=0'
    #message4 = b'Mon, 10 Feb 2003 14:07:13 GMT;'
    msage5 = b'DNT: 1'
    message6 = b'Connection: Keep-Alive'
    message7 = b'Cookie: N=; U=http%253A//192.168.1.170%253A81; D=; P=8089'
    #message = 'This is the message.  It will be repeated.'
    print (sys.stderr, 'sending "%s"' % message1)
    sock.sendall(message1)
    time.sleep(0.2)
    sock.sendall(message2)
    time.sleep(0.2)
    #sock.sendall(message3)
    #time.sleep(0.2)
    sock.sendall(message4)
    time.sleep(0.2)
    sock.sendall(message5)
    time.sleep(0.2)
    sock.sendall(message6)
    time.sleep(0.2)
    sock.sendall(message7)

    # Look for the response
    amount_received = 0
    amount_expected = len(message1)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print (sys.stderr, 'received "%s"' % data)

finally:
    print (sys.stderr, 'closing socket')
    sock.close()
