import http.server
import socketserver

PORT = 4056
handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), handler)

print("serving at port", PORT)
httpd.serve_forever()
