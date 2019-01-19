#import I2C_LCD_driver
#import socket
#import fcntl
#import struct

#mylcd = I2C_LCD_driver.lcd()

#def get_ip_address(ifname):
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    return socket.inet_ntoa(fcntl.ioctl(
#        s.fileno(),
#        0x8915, 
#        struct.pack('256s', ifname[:15])
#    )[20:24])

#mylcd.lcd_display_string("IP Address:", 1) 

#mylcd.lcd_display_string(get_ip_address('eth0'), 2)

"""Implements a HD44780 character LCD connected via PCF8574 on I2C."""

from i2c_lcd import I2cLcd
import time

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x3f

def test_main():
    """Test function for verifying basic functionality."""
    lcd = I2cLcd(1, DEFAULT_I2C_ADDR, 2, 16)
    lcd.blink_cursor_on()
    lcd.putstr("Please wait!\ninitialising")
    time.sleep(3)
    lcd.clear()
    lcd.blink_cursor_off()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])

    while True:
        lcd.move_to(0, 0)
        lcd.putstr("IP address =")
        lcd.move_to(1, 0)
        lcd.putstr(get_ip_address('etho'))
        #lcd.putstr(time.strftime('%b %d %Y\n%H:%M:%S', time.localtime()))
        time.sleep(1)

if __name__ == "__main__":
    test_main()
