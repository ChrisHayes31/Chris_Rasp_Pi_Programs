import socket
import sys
#Client
# Create a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_ip ='192.168.1.125'
sock_port = 10000
# Connect the socket to the port where the server is listening
server_address = ('192.168.1.125', 10000)
#server_address = (sock_ip, sock_port)
print ('connecting to - ' , server_address)
#sock.connect((sock_ip, sock_port))
#sock.connect(server_address)
sock.bind(('192.168.1.125', 10000))
try:
    
    # Send data
    message = (input('What key to send - '))
    
    if (message != ""):
        
        print ('sending - ' , message)
        #message = 'This is the message.  It will be repeated.'
        #print ('sending - ' , message)
        #sock.send(message,(sock_ip, sock_port))
        sock.send(b"ascii")
        #sock.send(message.encode('ascii'))
        #sock.sendall('This is the message.  It will be repeated.')

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print ('received - ' , data)

finally:
    print ('closing socket')
    sock.close()
