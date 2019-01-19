"""Implements a HD44780 character LCD connected via PCF8574 on I2C."""
# http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/
#from i2c_lcd import I2cLcd
import I2C_LCD_driver
import time
import sys
# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x3f

def test_main():
    #mylcd = I2C_LCD_driver.lcd()

    #mylcd.lcd_display_string("Hello World!", 2, 3)
    """Test function for verifying basic functionality."""
    mylcd = I2C_LCD_driver.lcd(1, DEFAULT_I2C_ADDR, 2, 16)
    #lcd = I2cLcd(1, DEFAULT_I2C_ADDR, 2, 16)
    #mylcd.blink_cursor_on()
    #lcd.putstr("Please wait\ninitialising")
    time.sleep(0.5)
    mylcd.lcd_clear()
    #lcd.blink_cursor_off()
    count = 0
    total = len(sys.argv) # nmumber of arguments in string
    msg1 = sys.argv[1:] # get everything after python script name
    text_line, l_number, p_number = msg1 # strip out the text and the line ref
    line_number = int(l_number) - 1
    pos_number = int(p_number) -1
    #move_to(self, cursor_x, cursor_y):
    while True:
        #mylcd.move_to(pos_number, line_number)
        #lcd.putstr(time.strftime('%b %d %Y\n%H:%M:%S', time.localtime()))
        #time.sleep(1)
        #lcd.backlight_on()
        mylcd.lcd_display_string("Hello World!", 2, 3)
        #mylcd.lcd_display_string(str(text_line), pos_number, line_number)
        #lcd.putstr(str(text_line))
        #lcd.putstr(time.strftime('%b %d %Y\n%H:%M:%S', time.localtime()))
        #lcd.putstr(datetime.datetime.now().time()), 3)
        # Write just the time to the display
        time.sleep(1)
        exit()
   
if __name__ == "__main__":
    test_main()
