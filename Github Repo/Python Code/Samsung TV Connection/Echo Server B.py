import socket

RASP_Pi_address = '192.168.1.125'
RASP_Pi_port    = 10000
RASP_Pi_vserver = (RASP_Pi_address, RASP_Pi_port)

RASP_Pi_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

RASP_Pi_server.bind(RASP_Pi_vserver)
RASP_Pi_server.listen(5)

while True:
    conn, addr = RASP_Pi_server.accept()
    print ('client connected ...' ,addr)

    while True:
        data = conn.recv(BUFSIZE)
        if not data:break
        print ('data received ...' , data)

    print ('closing now')
    conn.close()
    print ('client disconnected ...')
    
