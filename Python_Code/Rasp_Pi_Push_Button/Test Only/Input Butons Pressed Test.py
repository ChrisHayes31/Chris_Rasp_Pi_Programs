import RPi.GPIO as GPIO
import time


class Button_press:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        #pin 11 as GPIO 17 or input 1 Up
        GPIO.setup(17,GPIO.IN)
        #pin 12 as GPIO 18 or input 2 Down
        GPIO.setup(18,GPIO.IN)
        #pin 13 as GPIO 27 or input 3 Select
        GPIO.setup(27,GPIO.IN)
        #pin 16 as GPIO 23 or input 4 Menu
        GPIO.setup(23,GPIO.IN)

        prev_input = 0
        bounce_input = 0




while ((Input17_Pressed == False) and (bounce_input == 0)):
    if (GPIO.input(17)):
        print("Up pressed")
        bounce_input = 1
        Input17_Pressed = True
        
while ((Input18_Pressed == False) and (bounce_input == 0)):
    if (GPIO.input(18)):
        print("Down pressed")
        bounce_input = 1
        Input18_Pressed = True

while ((Input27_Pressed == False) and (bounce_input == 0)):
    if (GPIO.input(27)):
        print("Select pressed")
        bounce_input = 1
        Input27_Pressed = True

while ((Input23_Pressed == False) and (bounce_input == 0)):
    if (GPIO.input(23)):
        print("Menu pressed")
        bounce_input = 1
        Input23_Pressed = True
        
    
    #if (GPIO.input(17)):
    #    G_test = G_Input17
    #    prev_input = G_test
    #    print("Up pressed")
    #    time.sleep(0.05)

    
    #input = GPIO.input(17)
    #input = GPIO.input(18)
    #input = GPIO.input(27)
    #input = GPIO.input(23)

    #if ((not prev_input) and input):
    #    prev_input = input
    #    time.sleep(0.05)
        
    #if (GPIO.input(17)):
    #    input = GPIO.input(17)
    #    G_test = G_Input17
    #    if ((not prev_input) and input):
    #        prev_input = input
    #        print("Up pressed")
    #        time.sleep(0.05)
            
    #if (GPIO.input(18)):
    #    input = GPIO.input(18)
    #    G_test = G_Input18
    #    if ((not prev_input) and input):
    #        prev_input = input
    #        print("Down pressed")
    #        time.sleep(0.05)
            
    #if (GPIO.input(18) and (not prev_input)):
    #if ((not prev_input) and input):
    #    prev_input = input
    #    print("Down pressed")
    #    time.sleep(0.05)
        
    #if (GPIO.input(27) and (not prev_input)):
    #if ((not prev_input) and input):
    #    prev_input = input
    #    print("Select pressed")
    #    time.sleep(0.05)
        
    #if (GPIO.input(23) and (not prev_input)):
    #if ((not prev_input) and input):
    #    prev_input = input
    #    print("Menu pressed")
    #    time.sleep(0.05)
            
