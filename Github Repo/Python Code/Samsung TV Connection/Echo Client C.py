#Client
# TCP Client Code
from socket import *           # Imports socket module
 
#host="127.0.0.1"              # Set the server address to variable host

host = "192.168.1.121"
port = 10000                     # Sets the variable port to 4444
 
s=socket(AF_INET, SOCK_STREAM) # Creates a socket
s.connect((host,port))            # Connect to server address
#s.send('amx test')

message = (input('enter key to send .. '))

if (message == 'q'):
    print ("Quitting...")
    s.close()                            # Closes the socket
    
elif (message != ""):
    #s.send(message)
    s.send(message.encode())
    print ("Message sent : " , message)

# End of code
    
