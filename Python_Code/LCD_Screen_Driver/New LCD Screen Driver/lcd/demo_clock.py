"""Implements a HD44780 character LCD connected via PCF8574 on I2C."""

from i2c_lcd import I2cLcd
import time

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x3f

def test_main():
    """Test function for verifying basic functionality."""
    lcd = I2cLcd(1, DEFAULT_I2C_ADDR, 2, 16)
    lcd.blink_cursor_on()
    lcd.putstr("Please waiting - initialising")
    time.sleep(3)
    lcd.clear()

    while True:
        lcd.move_to(0, 0)
        lcd.backlight_on()
        time.sleep(1)
        lcd.putstr(time.strftime('%b %d %Y\n%H:%M:%S', time.localtime()))
        time.sleep(1)
    
        #except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        #    print("Cleaning up!")
        #    display.lcd_clear()

if __name__ == "__main__":
    test_main()
