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
msg1 = sys.argv[1:] # get everything after python script name
total = len(sys.argv) # number of arguments in string

# need to extract the following parts
# Bus Voltage
# Bus Current
# Supply Voltage
# Shunt Voltage
# Power

text_line = msg1     # strip out the text and the line ref
#text_line, l_number, p_number = msg1 # strip out the text and the line ref

#line_number = int(l_number) - 1 # set line number
#pos_number = int(p_number) -1   # set text on line position

# extract data
# How to use find()
Bus_Voltage    = msg1.split('\n')


#      a.split('\n')[:-1]



"""
Bus_Voltage    = msg1[1:11]
bus_current_location = msg1.find('Bus Current')
supply_current_location = msg1.find('Supply Voltage')
Bus_Current    = msg1.array([2])

Bus_Voltage    = msg1.array([1])
Bus_Current    = msg1.array([2])
Supply_Voltage = msg1.array([3])
Shunt_Current  = msg1.array([4])
Power_         = msg1.array([5])


Bus_Voltage    = text_line.find('Bus Voltage');
Bus_Current    = text_line.find('Bus Current');
Supply_Voltage = text_line.find('Supply Voltage');
Shunt_Current  = text_line.find('Shunt Voltage');
Power_         = text_line.find('Power');
"""
# setup display ready for text to be sent
#move_to(self, cursor_x, cursor_y):
#lcd.move_to(pos_number, line_number)                # place the data onto the line and position
lcd.backlight_on()                                  # ensure backlight on

# now send data to screen
lcd.move_to(0, 0)                                 # place the data onto the line and position
lcd.putstr(Bus_Voltage);         # send the data to the display

lcd.move_to(0, 1)                                 # place the data onto the line and position
#lcd.putstr(Bus_Voltage);         # send the data to the display
#lcd.putstr("Bus Vdc-V");         # send the data to the display

lcd.move_to(0, 2)                                 # place the data onto the line and position
#lcd.putstr("Bus Amp-I");         # send the data to the display

lcd.move_to(0, 3)                                 # place the data onto the line and position
#lcd.putstr("Shunt Current-I"); # send the data to the display

#lcd.move_to(0, 4)                                 # place the data onto the line and position
#lcd.putstr("Power- w");                # send the data to the display

#lcd.putstr(str(text_line)) # send the data to the display
time.sleep(1)
