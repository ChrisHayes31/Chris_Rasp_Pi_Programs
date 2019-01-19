import I2C_LCD_driver
#import time

from time import *
import sys
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear() #clear screen first
sleep(0.4)

total = len(sys.argv) # nmumber of arguments in string
msg1 = sys.argv[1:] # get everything after python script name
text_line, line_number = msg1 # strip out the text and the line ref

while True:
    mylcd.lcd_display_string(text_line,int(line_number))
    sleep(0.4)
    
