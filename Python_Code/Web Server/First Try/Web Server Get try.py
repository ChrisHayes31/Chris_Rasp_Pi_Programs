#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "GET /SetChannel.cgi?Channel=1"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8089, for port 80, which is normally used for a http server, you need root access
  server_address = ('192.168.1.170', 8089)
  #server_address = ('127.0.0.1', 8089)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()
