"""Implements a HD44780 character LCD connected via PCF8574 on I2C."""

from i2c_lcd import I2cLcd
import time
from sys import exit
# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x3f

def test_main():
    lcd = I2cLcd(1, DEFAULT_I2C_ADDR, 2, 16)
    lcd.blink_cursor_on()
    time.sleep(3)
    lcd.clear()
    exit()
        
if __name__ == "__main__":
    test_main()
