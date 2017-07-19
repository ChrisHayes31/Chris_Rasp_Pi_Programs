import RPi.GPIO as GPIO
import time
import os
import sys

#import keyboard
GPIO.setmode(GPIO.BCM) # assign the GPIO to the BCM method
GPIO.setwarnings(False) # stop error messages crashing the program

# declare the variables
start_time = 0
elapsed_time = 0
d_delay = 1 # 5 seconds
delayed_time = 0
run_time =False
Short_Button_Press = 2 # change this to reflect the length of the short button press action
Long_Button_Press  = 3 # change this to reflect the length of the long button press action

Input_Button_1 = 17 # GPIO assignment to Button/s 1
Input_Button_2 = 18 # GPIO assignment to Button/s 2
Input_Button_3 = 27 # GPIO assignment to Button/s 3
Input_Button_4 = 23 # GPIO assignment to Button/s 4
Output_Relay_1 = 22 # GPIO assignment for relay/s 1
Output_Relay_2 = 24 # GPIO assignment for relay/s 2
Output_Relay_3 = 25 # GPIO assignment for relay/s 3
Output_Relay_4 = 5  # GPIO assignment for relay/s 4

# GPIO Assignments for the input button pushes
GPIO.setup(Input_Button_1,GPIO.IN)   #pin 11 as GPIO 17 for input 1 
GPIO.setup(Input_Button_2,GPIO.IN)   #pin 12 as GPIO 18 for input 2 
GPIO.setup(Input_Button_3,GPIO.IN)   #pin 13 as GPIO 27 for input 3 
GPIO.setup(Input_Button_4,GPIO.IN)   #pin 16 as GPIO 23 for input 4 

# GPIO Assignments for the output relay functions
GPIO.setup(Output_Relay_1,GPIO.OUT)  #pin 15 as GPIO 22 for Output 1 
GPIO.setup(Output_Relay_2,GPIO.OUT)  #pin 18 as GPIO 24 for Output 2 
GPIO.setup(Output_Relay_3,GPIO.OUT)  #pin 22 as GPIO 25 for Output 3 
GPIO.setup(Output_Relay_4,GPIO.OUT)  #pin 24 as GPIO 5  for Output 4 

def cls():
    os.system('clear')

def release_relay(): # turn off all relays in one go
    GPIO.output(Output_Relay_1,GPIO.HIGH) # turn relay 1 off
    #print ("Relay 1 off ") # echo which relay off
    GPIO.output(Output_Relay_2,GPIO.HIGH) # turn relay 2 off
    #print ("Relay 2 off ") # echo which relay off
    GPIO.output(Output_Relay_3,GPIO.HIGH) # turn relay 3 off
    #print ("Relay 3 off ") # echo which relay off
    GPIO.output(Output_Relay_4,GPIO.HIGH) # turn relay 4 off
    #print ("Relay 4 off ") # echo which relay off
    print ("Relays 1,2,3,4 - Off ") # echo all relays off
    delayed_time = 0 # reset the time off variable       
              
def relay_control(channel_act, e_time):
    global Short_Button_Press
    global Long_Button_Press
    if (e_time <= Short_Button_Press): # if button pressed time is below Short_Button_Press single relay activation
        if (channel_act == Input_Button_1):
            GPIO.output(Output_Relay_1,GPIO.LOW) # turn relay 1 on
            print ("Relay 1 on ") # echo which relay on
        if (channel_act == Input_Button_2):
            GPIO.output(Output_Relay_2,GPIO.LOW) # turn relay 2 on
            print ("Relay 2 on ") # echo which relay on
        if (channel_act == Input_Button_3):
            GPIO.output(Output_Relay_3,GPIO.LOW) # turn relay 3 on
            print ("Relay 3 on ") # echo which relay on
        if (channel_act == Input_Button_4):
            GPIO.output(Output_Relay_4,GPIO.LOW) # turn relay 4 on
            print ("Relay 4 on ") # echo which relay on
        
    if (e_time >= Long_Button_Press) : # if button pressed above Long_Button_Press two relay activation for button 1 & 3 only
        if (channel_act == Input_Button_1):
            GPIO.output(Output_Relay_1,GPIO.LOW) # turn relay 1 on
            GPIO.output(Output_Relay_2,GPIO.LOW) # turn relay 2 on
            print ("Relays 1 & 2 on ") # echo which relay/s on
        if (channel_act == Input_Button_3):
            GPIO.output(Output_Relay_3,GPIO.LOW) # turn relay 3 on
            GPIO.output(Output_Relay_4,GPIO.LOW) # turn relay 4 on
            print ("Relays 3 & 4 on ") # echo which relay/s on
    time.sleep(d_delay)
    release_relay()

   
def button_pressed(channel):
    cls()
    global elapsed_time # setup global variable for how long button was pressed for
    global start_time # setup global variable for when button pressed in time
    global delayed_time # setup global variable for the time delay to turn off relays
    global snap_time # setup time capture variable
    if (GPIO.input(channel) == 1): # detects the edge is rising - button pressed
        #print("leading edge detected on channel %s - "%channel) # just echos feedback of what button pressed
        #print ("Time elapsed = " , elapsed_time) # echo how long button pressed
        #print(" ")
        elapsed_time = 0 # reset elapsed_time timer to zero -
        start_time = time.time() # capture exactly what time the button was pressed - start clock counter

    if (GPIO.input(channel) == 0): # detects the edge is falling - button released
        #print("trailing edge detected on channel %s - "%channel) # just echos feedback of what button pressed
        snap_time = time.time()
        elapsed_time = (snap_time - start_time) # capture how long button released for
        delayed_time = snap_time + d_delay
        #print ("Time elapsed = " , elapsed_time) # echo how long button pressed
        #print ("Relay off time = " , delayed_time , " " , snap_time) # echo how time relays off
        #print(" ")
        relay_control(channel, elapsed_time) # activate the relays
        elapsed_time = 0 # reset elapsed_time timer to zero 

# setup the interupts for the 4 buttons - look for ledgeing and trailing edge triggers
# note this method when a button pressed will interupt the running program below
# this is very good for immediate action to a button press
# call the button_pressed rountine to reveal which button and whether ledging or trailing edge
# bouncetime is a software bounce code to stop multiple button pushes
# this code MUST before the running program as it is only actioned when an event happens

GPIO.add_event_detect(Input_Button_1,GPIO.BOTH,callback = button_pressed, bouncetime=200)
GPIO.add_event_detect(Input_Button_2,GPIO.BOTH,callback = button_pressed, bouncetime=200)
GPIO.add_event_detect(Input_Button_3,GPIO.BOTH,callback = button_pressed, bouncetime=200)
GPIO.add_event_detect(Input_Button_4,GPIO.BOTH,callback = button_pressed, bouncetime=200)
        
while True:
    try:
        if (run_time == False):
            print ("Welcome - enjoy")
            run_time = True            

    except KeyboardInterrupt: # use CTL-x to shutdown
        print("Time to clean up...")
        release_relay()
        GPIO.cleanup()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


      
