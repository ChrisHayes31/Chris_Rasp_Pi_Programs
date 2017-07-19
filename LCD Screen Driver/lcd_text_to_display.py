import I2C_LCD_driver
#import time

from time import *
import sys
mylcd = I2C_LCD_driver.lcd()
total = len(sys.argv) # nmumber of arguments in string
lcd_text = str(sys.argv) # text to print
line_to_display = (sys.argv[total-1]) # get the line number from end argument

#count = 0
#while count <= total:
#    mess1[i] = sys.argv[i]
#    count += 1
#var newMsg = {payload:loc_msg.concat(" ", text_msg, "|", line_number)}; 

while True:
    #mylcd.lcd_display_string(arg1, arg2)

    mylcd.lcd_display_string(lcd_text,int(line_to_display))
    #mylcd.lcd_display_string(lcd_text,int(line_to_display))
    
    #mylcd.lcd_display_string(lcd_text2,3)
    #mylcd.lcd_display_string(line_to_display,4)
    #mylcd.lcd_display_string(lcd_text,int(line_to_display)) #works

    
    #mylcd.lcd_display_string(lcd_text,line_to_display)
    #mylcd.lcd_display_string(text_to_display, line_to_display)
    #mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
    
    #mylcd.lcd_display_string("Date: %s" %time.strftime("%m/%d/%Y"), 2)
    sleep(0.4)
    
