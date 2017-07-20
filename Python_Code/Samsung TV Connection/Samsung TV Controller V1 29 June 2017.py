import time
import socket
import base64
import sys
from PyQt4 import QtGui, QtCore

app
Selected_Key = 0

src     = '192.168.1.125'     # ip of raspberry pi remote
mac     = 'b8:27:eb:67:dd:23' # mac address of Raspberry pi
#mac     = '00-AB-11-11-11-11' # mac of remote

remote  = 'python remote'     # remote name
dst     = '192.168.1.62'      # ip of tv
app     = 'python'            # iphone..iapp.samsung
tv      = 'UA55C7000'         # iphone.UA55C7000.iapp.samsung
#tv      = 'LE32C650'          # iphone.LE32C650.iapp.samsung

class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Samsung TV Controller")
        self.home()
        
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(100,100)
        btn.move(100.100)
        self.show()
        
    def run():
        app = QtGui.Application(sys.argv)
        GUI = Window()
        sys.exit(app.exec_())


    """
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
    """
while True:
    try:
        run()
        Selected_Key = input('Enter Key ')
        print (Selected_Key)
        """
        # switch to tv
        push("KEY_TV")
          
        # switch to channel one
        push("KEY_1")
        push("KEY_ENTER")
          
        time.sleep(5)
          
        # switch to channel 15
        push("KEY_1")
        push("KEY_5")
        push("KEY_ENTER")
          
        time.sleep(5)
        
        # switch to HDMI
        push("KEY_HDMI")
        
        time.sleep(5)
        """
