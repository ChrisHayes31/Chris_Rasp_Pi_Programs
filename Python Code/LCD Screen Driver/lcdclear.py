import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Clear Display", 1)
sleep(1)

mylcd.lcd_clear()
