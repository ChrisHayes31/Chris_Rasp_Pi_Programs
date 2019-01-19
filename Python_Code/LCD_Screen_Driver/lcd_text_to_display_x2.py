import I2C_LCD_driver
import time
import sys
mylcd = I2C_LCD_driver.lcd()

text_to_display = str(sys.argv)
line_to_display = str(sys.argv)
msg1 = text_to_display.split(' ',1)
while True:
    #mylcd.lcd_display_string(arg1, arg2)
    mylcd.lcd_display_string(msg1, 1)
    #mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
    
    #mylcd.lcd_display_string("Date: %s" %time.strftime("%m/%d/%Y"), 2)

#https://www.tutorialspoint.com/python/string_split.htm
    
