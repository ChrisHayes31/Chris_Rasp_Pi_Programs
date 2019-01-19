"""Implements a HD44780 character LCD connected via PCF8574 on I2C."""

from i2c_lcd import I2cLcd
import time
import sys

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x3f
msg1 = sys.argv[1:] # get everything after python script name
text_line, l_number, p_number = msg1 # strip out the text and the line ref
line_number = int(l_number) - 1
pos_number = int(p_number) -1
#lcd.move_to(pos_number, line_number)
#lcd.backlight_on()
#lcd.putstr(str(text_line))
#time.sleep(1)
lcd = I2cLcd(1, DEFAULT_I2C_ADDR, 2, 16)
lcd.blink_cursor_on()
lcd.putstr("Please waiting - initialising")
time.sleep(1)
lcd.clear()

while (text_line == "start"):
    lcd.move_to(0, 0)
    lcd.backlight_on()
    time.sleep(1)
    lcd.putstr(time.strftime('%b %d %Y\n%H:%M:%S', time.localtime()))

#if __name__ == "__main__":
#    test_main()

while (text_line == "stop"):
    lcd.clear()
    time.sleep(1)
    lcd.putstr("clock stopped")
    exit(1) 

