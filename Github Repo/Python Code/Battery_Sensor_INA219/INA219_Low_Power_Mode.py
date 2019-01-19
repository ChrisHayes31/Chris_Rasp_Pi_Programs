ina.configure(ina.RANGE_16V)
while True:
    print "Voltage : %.3f V" % ina.voltage()
    ina.sleep()
    time.sleep(60)
    ina.wake();
