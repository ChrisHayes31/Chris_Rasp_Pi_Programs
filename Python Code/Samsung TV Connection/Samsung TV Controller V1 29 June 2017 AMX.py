#!/usr/bin/env python
import socket
import subprocess
import sys
import time
import base64
from datetime import datetime
from PyQt4 import QtGui, QtCore

# Ref page https://gist.github.com/pedrinho/5529f159103dd8577651
# Ref page = https://gist.github.com/danielfaust/998441
# Ref Key codes https://github.com/Bntdumas/SamsungIPRemote/blob/master/samsungKeyCodes.txt

TV_ip_address = '192.168.1.62' # Lounge room TV IP address
src      = b'192.168.1.125'     # ip of raspberry pi remote
mac      = b'b8:27:eb:67:dd:23' # mac address of Raspberry pi
#mac      = '00-AB-11-11-11-11' # mac of remote

remote   = b'python remote'     # remote name
dst      = '192.168.1.62'      # ip of tv
app      = 'python'            # iphone..iapp.samsung
encoding = 'utf-8'
tv       = 'UA55C7000'         # iphone.UA55C7000.iapp.samsung
#tv       = 'LE32C650'          # iphone.LE32C650.iapp.samsung
port     = 55000

AMX_ip          = '192.168.1.150'      # ip of AMX
AMX_port        = 8006 # AMX Port
AMX_Buffer_size = 1024

AMX_tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AMX_tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
AMX_tcpsock.connect((AMX_ip, AMX_port))
#AMX_tcpsock.bind((AMX_ip, AMX_port))
        



key_select = " "

class Window(QtGui.QMainWindow):

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
            
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Samsung TV Controller - 192.168.1.62")
        #self.setWindowIcon(QtGui.QIcon('Samsung_Logo very small.png'))

        extractAction = QtGui.QAction("&File", self)
        extractAction = QtGui.QAction("Open", self)
        extractAction.setShortcut("Ctrl+O")
        extractAction.setStatusTip('Open file')
        #extractAction.triggered.connect(self.close_application)
        extractAction = QtGui.QAction("Save", self)
        #extractAction.setShortcut("Ctrl+O")
        extractAction.setStatusTip('Save file')
        #extractAction.triggered.connect(self.close_application)
        extractAction = QtGui.QAction("Save As", self)
        #extractAction.setShortcut("Ctrl+O")
        extractAction.setStatusTip('Save file')
        #extractAction.triggered.connect(self.close_application)

        
        extractAction = QtGui.QAction("E&xit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        fileMenu = mainMenu.addMenu('Open')
        fileMenu.addAction(extractAction)

        fileMenu = mainMenu.addMenu('Save')
        fileMenu.addAction(extractAction)
        
        fileMenu = mainMenu.addMenu('Save As')
        fileMenu.addAction(extractAction)
        
        #exitMenu = mainMenu.addMenu('E&xit')
        #exitMenu.addAction(extractAction)

        self.home()

    def home(self):
        
        self.selected_Tv_Ip_address = QtGui.QLabel("192.168.1.62", self)
        self.selected_Tv_Ip_address.move(200, 50)
        #textbox = QLineEdit(TV_ip)
        #textbox.move(30, 50)
        #textbox.resize(280,40)
        
        #btn = QtGui.QPushButton("Enter IP Address", self)
        #btn.clicked.connect(self.get_ip_address)
        #btn.clicked.connect(self.close_application)
        #btn.resize(btn.minimumSizeHint())
        #btn.setStatusTip('Enter IP Address to connect to -')
        #btn.move(0,50)
        
        # Connect to HDMI 1 input
        btn = QtGui.QPushButton("HDMI 1", self)
        btn.clicked.connect(self.connect_HDMI1)
        btn.resize(btn.minimumSizeHint())
        btn.setStatusTip('Select HDMI 1 input -')
        btn.move(0,25)
         # Connect to HDMI 2 input
        btn = QtGui.QPushButton("HDMI 2", self)
        btn.clicked.connect(self.connect_HDMI2)
        btn.resize(btn.minimumSizeHint())
        btn.setStatusTip('Select HDMI 2 input -')
        btn.move(100,25)

        # Connect to AV 1 input
        btn = QtGui.QPushButton("AV 1", self)
        btn.clicked.connect(self.connect_AV1)
        btn.resize(btn.minimumSizeHint())
        btn.setStatusTip('Select AV 1 input -')
        btn.move(0,60)
        # Connect to AV 2 input
        btn = QtGui.QPushButton("AV 2", self)
        btn.clicked.connect(self.connect_AV2)
        btn.resize(btn.minimumSizeHint())
        btn.setStatusTip('Select AV 2 input -')
        btn.move(100,60)

        # Connect to POWER OFF
        btn = QtGui.QPushButton("Power Off", self)
        btn.clicked.connect(self.connect_POWEROFF)
        btn.resize(btn.minimumSizeHint())
        btn.setStatusTip('Turn TV Off')
        btn.move(200,120)

        # Send to TV Button
        btn = QtGui.QPushButton("Send Key Code to TV", self)
        btn.clicked.connect(self.send_selected_key)

        #btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.setStatusTip('Connect to selected TV -')
        btn.move(0,100)

        #checkBox = QtGui.QCheckBox('Shrink Window', self)
        #checkBox.move(100,25)
        #checkBox.stateChanged.connect(self.enlarge_window)
        
        # Progress Bar setup
        #self.progress = QtGui.QProgressBar(self)
        #self.progress.setGeometry(200, 80, 250, 20)
        
        #self.btn =QtGui.QPushButton("Progress",self)
        #self.btn.move(200,120)
        #self.btn.clicked.connect(self.progress_led)

        self.key_to_send = QtGui.QLabel("Key - ", self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("KEY_EXT1")
        comboBox.addItem("KEY_EXT2")
        comboBox.addItem("KEY_AV1")
        comboBox.addItem("KEY_AV2")
        comboBox.addItem("KEY_HDMI")
        comboBox.addItem("KEY_HDMI2")
        comboBox.addItem("KEY_MENU")
        comboBox.addItem("KEY_ENTER")
        comboBox.addItem("KEY_UP")
        comboBox.addItem("KEY_DOWN")
        comboBox.addItem("KEY_VOLUP")
        comboBox.addItem("KEY_VOLDOWN")
        comboBox.addItem("KEY_POWEROFF")
        
        comboBox.move(50, 200)
        
        self.key_to_send.move(50,150)
        comboBox.activated[str].connect(self.get_which_key)
        #btn.clicked.connect(self.connect_AV2)
  
        self.show()
        
    def progress_led(self):
        #run a timed loop for progress bar example
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
    
    def select_Tv(self, text):
        self.selected_TV_name.setText(text)
        
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 5000, 300)

    def connect_HDMI1(self): # connect to HDMI-1 input
        #TV_input = ("KEY_HDMI1")
        key_send('KEY_HDMI')
    def connect_HDMI2(self): # connect to HDMI-2 input
        #TV_input = ("KEY_HDMI2")
        key_send('KEY_HDMI2')
        
    def connect_HDMI3(self): # connect to HDMI-3 input
        #TV_input = ("KEY_HDMI3")
        key_send('KEY_HDMI3')
    
    def connect_AV1(self):   # connect to AV1 input
        #TV_input = ("KEY_AV1")
        key_send('KEY_AV1')
        
    def connect_AV2(self):
        # connect to AV2 input
        #TV_input = ("KEY_AV2")
        key_send('KEY_AV2')
        
    def connect_POWEROFF(self):
        # turn TV off
        #TV_input = ("KEY_POWEROFF")
        key_send('KEY_POWEROFF')

    def get_which_key(self, text):
        self.key_to_send.setText(text) # update label to reflect key selected
        self.key_select = self.key_to_send.text() # trap key variable
       
    def send_selected_key(self):
        print (self.key_select)
        key_send(self.key_select)
        #which_key = input("Enter key code activate: ")
        #self.selected_Tv_Ip_address = TV_ip_address
        #remoteServerIP  = socket.gethostbyname(remoteServer)
        # check this to start connection
        
    def connect_to_ip_address(self):
        print ("Connecting to IP address - ", TV_ip_address) 
        
    def close_application(self):
        print("see ya !!")
        sys.exit()
        
    def connect(self, AMX_ip, AMX_port):
        self.sock.connect((AMX_ip, AMX_port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return ''.join(chunks)



    def receive_keys(rx_key):
        new = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new.connect((AMX_dst, AMX_port))
        

        new.close()
        time.sleep(0.1)
        return True

def key_send(key):
    try:
        new = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new.connect((dst, port))
        byte_key = bytes(key, encoding)

        msg =  chr(0x64) + chr(0x00) +\
               chr(len(base64.b64encode(src).decode(encoding))) +\
               chr(0x00) + base64.b64encode(src).decode(encoding) +\
               chr(len(base64.b64encode(mac).decode(encoding))) +\
               chr(0x00) + base64.b64encode(mac).decode(encoding) +\
               chr(len(base64.b64encode(remote).decode(encoding))) +\
               chr(0x00) + base64.b64encode(remote).decode(encoding)

        #print (msg)
        
        pkt = chr(0x00) + chr(len(app)) + chr(0x00) + app + chr(len(msg)) +\
              chr(0x00) + msg

        new.send(bytes(pkt, encoding))
                 
        msg =  chr(0x00) + chr(0x00) + chr(0x00) +\
               chr(len(base64.b64encode(byte_key).decode(encoding))) +\
               chr(0x00) + base64.b64encode(byte_key).decode(encoding)
        
        pkt = chr(0x00) + chr(len(tv))  + chr(0x00) + tv + chr(len(msg)) + chr(0x00) + msg
        new.send(bytes(pkt, encoding))
        
        new.close()
        time.sleep(0.1)
        return True
    except socket.error:
        return False
                 
def run():
    subprocess.call('clear', shell=True)
    # Clear the screen
    subprocess.call('clear', shell=True)
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    GUI = Window()
    """
    while True:
        rx_key = conn.recv(1024)
        if not data: break
        print ("received data: ", rx_key)
    """ 
    
    # Ask for input
    # remoteServer    = input("Enter TV IP Address to connect to: ")
    # remoteServerIP  = socket.gethostbyname(remoteServer)
    sys.exit(app.exec_())

while True:
    AMX_tcpsock.listen(4)
    print ("waiting for incomming connectiosn...")
    (conn, (AMX_ip, AMX_port)) = AMX_tcpsock.accept()
    run()
