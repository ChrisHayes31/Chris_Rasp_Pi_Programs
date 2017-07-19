import socket

RASP_Pi_address = '192.168.1.125'
RASP_Pi_port    = 10000
RASP_Pi_vserver = (RASP_Pi_address, RASP_Pi_port)
RASP_Pi_BUFSIZE = 4096

RASP_Pi_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

RASP_Pi_server.bind(RASP_Pi_vserver)
#RASP_Pi_server.listen(5)

while True:
    message = (input('Enter Key... '))
    if (message != ""):
        RASP_Pi_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        RASP_Pi_server.connect(RASP_Pi_vserver)
        print ('server connected ...' ,addr)
        if (message == 'q'):
            print ('closing now')
            conn.close()
            print ('server disconnected ...')
    
