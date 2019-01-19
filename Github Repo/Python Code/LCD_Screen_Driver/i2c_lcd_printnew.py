import I2C_LCD_driver
from time import *
import sys

mylcd = I2C_LCD_driver.lcd()
msg1 = sys.argv[0]
text = sys.argv[1]
#linenumber = sys.argv[2]
linenumber = int(sys.argv[2])
#pos = sys.argv[3]
pos = int(sys.argv[3])

#print(help(mylcd.lcd_display_string))
#mylcd.lcd_display_string(text, linenumber, pos)

mylcd.lcd_display_string("This is how you", 2)
sleep(5)

#mylcd.lcd_clear()
