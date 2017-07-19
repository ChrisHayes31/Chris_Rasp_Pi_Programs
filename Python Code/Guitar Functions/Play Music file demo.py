import sys
import pygame
from PyQt4 import QtGui
app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setGeometry(0, 0, 500, 300)
window.setWindowTitle("Play Audio Track")
window.show()

pygame.mixer.init()
pygame.mixer.music.load("badswap.wav")

pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    print ("playing file now")
    continue


