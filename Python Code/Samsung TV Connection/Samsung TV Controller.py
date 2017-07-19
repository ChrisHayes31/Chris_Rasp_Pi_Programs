#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
from PyQt4 import QtGui, QtCore
TV_ip_address = '192.168.1.62'

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Samsung TV Controller")
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
        
        btn = QtGui.QPushButton("Enter IP Address", self)
        btn.clicked.connect(self.get_ip_address)
        #btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.setStatusTip('Enter IP Address to connect to -')
        btn.move(0,50)

        btn = QtGui.QPushButton("Connecting to TV", self)
        btn.clicked.connect(self.connect_to_ip_address)
        #btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.setStatusTip('Connect to selected TV -')
        btn.move(0,80)

        checkBox = QtGui.QCheckBox('Shrink Window', self)
        checkBox.move(100,25)
        checkBox.stateChanged.connect(self.enlarge_window)
        
        # Progress Bar setup
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        
        self.btn =QtGui.QPushButton("Progress",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.progress_led)

        self.selected_TV_name = QtGui.QLabel("--", self)
        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("Lounge TV")
        comboBox.addItem("Helen's TV")
        comboBox.addItem("Bungalow TV")
        comboBox.move(50, 200)
        self.selected_TV_name.move(50,150)
        comboBox.activated[str].connect(self.select_Tv)
  
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
   
    def get_ip_address(self):
        # Ask for input
        TV_ip_address = input("Enter TV IP Address to connect to: ")
        self.selected_Tv_Ip_address = TV_ip_address
        #remoteServerIP  = socket.gethostbyname(remoteServer)
        # check this to start connection
        
    def connect_to_ip_address(self):
        print ("Connecting to IP address - ", TV_ip_address) 
        
    def close_application(self):
        print("see ya !!")
        sys.exit()

def push(key):
    new = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new.connect((dst, 55000))
    msg = chr(0x64) + chr(0x00) +\
          chr(len(base64.b64encode(src)))    + chr(0x00) + base64.b64encode(src) +\
          chr(len(base64.b64encode(mac)))    + chr(0x00) + base64.b64encode(mac) +\
          chr(len(base64.b64encode(remote))) + chr(0x00) + base64.b64encode(remote)
    pkt = chr(0x00) +\
          chr(len(app)) + chr(0x00) + app +\
          chr(len(msg)) + chr(0x00) + msg
    new.send(pkt)
    msg = chr(0x00) + chr(0x00) + chr(0x00) +\
          chr(len(base64.b64encode(key))) + chr(0x00) + base64.b64encode(key)
    pkt = chr(0x00) +\
          chr(len(tv))  + chr(0x00) + tv +\
          chr(len(msg)) + chr(0x00) + msg
    new.send(pkt)
    new.close()
    time.sleep(0.1)
        
def run():
    subprocess.call('clear', shell=True)
    # Clear the screen
    subprocess.call('clear', shell=True)
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    GUI = Window()
    # Ask for input
    # remoteServer    = input("Enter TV IP Address to connect to: ")
    # remoteServerIP  = socket.gethostbyname(remoteServer)
    sys.exit(app.exec_())


run()
