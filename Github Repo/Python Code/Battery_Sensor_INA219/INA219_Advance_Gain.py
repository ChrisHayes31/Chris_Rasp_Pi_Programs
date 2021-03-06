#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 0.2


def read():
    ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
    #ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS, address=0x41) # add other address
    ina.configure(ina.RANGE_16V, ina.GAIN_1_40MV)

    print ("Bus Voltage: %.3f V" % ina.voltage())
    try:
        print ("Bus Current: %.3f mA" % ina.current())
        print ("Power: %.3f mW" % ina.power())
        print ("Shunt voltage: %.3f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        print ("Current overflow")


if __name__ == "__main__":
    read()
