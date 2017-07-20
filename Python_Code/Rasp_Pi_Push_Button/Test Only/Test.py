#!/usr/bin/env python
import time
import datetime
import os.path
#import pycurl
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
def GetGas(arg):
 
    time.sleep(0.01)  # need to filter out the false positive of some power fluctuation
    if GPIO.input(10) != GPIO.HIGH:
       return
 
    gastotal=0
    if os.path.isfile('/var/www/myscripts/gas/gastotale.txt'):
            file = open("/var/www/myscripts/gas/gastotale.txt","r")
            gastotal = float(file.read())
            file.close()
    gastotal = gastotal+0.01
 
    file = open("/var/www/myscripts/gas/gastotale.txt","w")
    file.write(str(gastotal))
    file.close()
 
    now = datetime.datetime.now()
    fileday = '/var/www/myscripts/gas/'+now.strftime("%Y-%m-%d")+'.txt'
    gasday = 0
 
    if os.path.isfile(fileday):
            file = open(fileday,"r")
            gasday = float(file.read())
            file.close()
    gasday = gasday+0.01
 
    file = open(fileday,"w")
    file.write(str(gasday))
    file.close()
 
    oem = pycurl.Curl()
    oem.setopt(oem.URL, 'http://emoncms.org/input/post.json?node=0&amp;csv=0,'+str(gasday)+',0,0,'+str(gastotale)+'&amp;apikey=xxxx')
    oem.perform()
 
GPIO.add_event_detect(10, GPIO.RISING, callback=GetGas, bouncetime=300)
 
GPIO.wait_for_edge(10, GPIO.FALLING)
 
 
GPIO.cleanup()
