#server
# TCP Server Code
from socket import *                # Imports socket module
 
#host="127.0.0.1"              # Set the server address to variable host
host = "192.168.1.107"         # Set the server address to variable host
port = 10000                   # Sets the variable port to 4444

s=socket(AF_INET, SOCK_STREAM)
s.bind((host,port))         # Binds the socket. Note that the input to 
                               # the bind function is a tuple
s.listen(5)                    # Sets socket to listening state with a  queue
                               # of 1 connection
print ("Listening for connections.. ")
q, addr = s.accept()               # Accepts incoming request from client and returns

data = q,recv(1024).decode("ascii")
print( 'data receivced .. ', data)
#s.close()
# End of code
    
