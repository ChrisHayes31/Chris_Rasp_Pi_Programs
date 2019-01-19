"""Implements a HD44780 character LCD connected via PCF8574 on I2C."""

from i2c_lcd import I2cLcd
import time
import sys
# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x3f
lcd = I2cLcd(1, DEFAULT_I2C_ADDR, 2, 16)
lcd.blink_cursor_on()
time.sleep(0.5)
lcd.clear()
lcd.blink_cursor_off()
total = len(sys.argv) # nmumber of arguments in string
msg1 = sys.argv[1:] # get everything after python script name
text_line, l_number, p_number = msg1 # strip out the text and the line ref
line_number = int(l_number) - 1
pos_number = int(p_number) -1
#move_to(self, cursor_x, cursor_y):
lcd.move_to(pos_number, line_number)
lcd.backlight_on()
lcd.putstr(str(text_line))
time.sleep(1)
