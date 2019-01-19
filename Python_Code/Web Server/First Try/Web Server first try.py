## Creating a basic web server in python without 
## any external modules or dependencies

import os
import http.server
#import SimpleHTTPServer
import socketserver
PORT = 8089
## 'SimpleHTTPRequestHeader' is setup to serve up any 
## files located in the current directory
Handler = http.server.SimpleHTTPRequestHandler
#Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("localhost", PORT), Handler)

print ("serving at port: ", PORT)
httpd.serve_forever()




#import http.server
#import socketserver

#PORT = 8000

#Handler = http.server.SimpleHTTPRequestHandler

#with socketserver.TCPServer(("", PORT), Handler) as httpd:
#    print("serving at port", PORT)
#    httpd.serve_forever()
