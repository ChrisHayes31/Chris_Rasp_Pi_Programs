import RPi.GPIO as GPIO
import time
counter_timer = 0
button_pressed_timer_active = False
start_time = 0
elapsed_time = 0
#b_action = 0
#button_1_pressed = 0
#button_1_released = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO.cleanup
Input_Button_1 = 17 # GPIO assignment to Buttons
Input_Button_2 = 18 # GPIO assignment to Buttons
Input_Button_3 = 27 # GPIO assignment to Buttons
Input_Button_4 = 23 # GPIO assignment to Buttons
Output_Relay_1 = 22 # GPIO assignment for relays
Output_Relay_2 = 24 # GPIO assignment for relays
Output_Relay_3 = 25 # GPIO assignment for relays
Output_Relay_4 = 8  # GPIO assignment for relays

GPIO.setup(Input_Button_1,GPIO.IN)   #pin 11 as GPIO 17 for input 1 Up
GPIO.setup(Input_Button_2,GPIO.IN)   #pin 12 as GPIO 18 for input 2 Down
GPIO.setup(Input_Button_3,GPIO.IN)   #pin 13 as GPIO 27 for input 3 Select
GPIO.setup(Input_Button_4,GPIO.IN)   #pin 16 as GPIO 23 for input 4 Menu

GPIO.setup(Output_Relay_1,GPIO.OUT)  #pin 15 as GPIO 22 for Output 1 
GPIO.setup(Output_Relay_2,GPIO.OUT)  #pin 18 as GPIO 24 for Output 2 
GPIO.setup(Output_Relay_3,GPIO.OUT)  #pin 22 as GPIO 25 for Output 3 
GPIO.setup(Output_Relay_4,GPIO.OUT)  #pin 24 as GPIO 8  for Output 4 

class Button_press:
    def __init__(self):
        print ("Welcome")

    def inputChng(channel):
        print ("Button Pressed - Relay ", channel, " selected ") # echo which button pressed
        print ("**** timer started **** ") # echo timer has started
        start_time = time.time()           # capture the actual time the button was pressed
        elapsed_time == 0                  # ensure elapsed time is reset

    def button_1_release(channel):
        print ("Timer stopped ") # print timer reset
        elapsed_time = time.time() - start_time # capture how long button pressed for
        if (elapsed_time <= 2): # if elapsed time is less than 2 secs then switch one relay
            print ("Relay 1 activated") # echo which relay switched
        if (elapsed_time >= 3): # if elapsed time is greater than 3 secs then switch the two assigned relays
            print ("Relay 1 & 2 activated") # echo which relay/s switched

    def button_2_pressed(channel):
        print ("Button 2 Pressed - Relay 2 selected ") # echo which button pressed
        #print ("**** timer started **** ") # echo timer has started
        #start_time = time.time()           # capture the actual time the button was pressed
        #elapsed_time == 0                  # ensure elapsed time is reset

    def button_2_release(channel):
        print ("Reset timer ") # print timer reset
        #elapsed_time = time.time() - start_time # capture how long button pressed for
        #if (elapsed_time <= 2): # if elapsed time is less than 2 secs then switch one relay
        print ("Relay 2 activated") # echo which relay switched
        #if (elapsed_time >= 3): # if elapsed time is greater than 3 secs then switch the two assigned relays
        #    print ("Relay 1 & 2 activated") # echo which relay/s switched

            #button_pressed_timer_active ==  False # turn off the timer function process ended
        
        #GPIO.add_event_detect(17, GPIO.RISING, callback=rel1_Rising_callback)
        #GPIO.add_event_detect(Input_Button_1, GPIO.BOTH, callback=my_callback)
        #GPIO.add_event_detect(17, GPIO.FALLING, callback=rel1_Falling_callback)
                
GPIO.add_event_detect(Input_Button_1,GPIO.RISING,callback=inputChng(Output_Relay_1),bouncetime=30)  # detect button 1 pressed
GPIO.add_event_detect(Input_Button_1,GPIO.FALLING,callback=button_1_release(Output_Relay_1),bouncetime=30) # detect button 1 released
GPIO.add_event_detect(Input_Button_2,GPIO.RISING,callback=button_2_pressed(Output_Relay_2),bouncetime=30)  # detect button 2 pressed
GPIO.add_event_detect(Input_Button_2,GPIO.FALLING,callback=button_2_release(Output_Relay_2),bouncetime=30) # detect button 2 released    

"""
GPIO.add_event_detect(Input_Button_1, GPIO.RISING,  callback = my_callback(Output_Relay_1,Output_Relay_1,Button_pressed), bouncetime = 30)  # detect button 1 pressed
GPIO.add_event_detect(Input_Button_1, GPIO.FALLING, callback = my_callback(Output_Relay_1,Output_Relay_2,Button_released), bouncetime = 30) # detect button 1 released
GPIO.add_event_detect(Input_Button_2, GPIO.RISING,  callback = my_callback(Output_Relay_2,Output_Relay_2,Button_pressed), bouncetime = 30)  # detect button 2 pressed
GPIO.add_event_detect(Input_Button_2, GPIO.FALLING, callback = my_callback(Output_Relay_2,Output_Relay_2,Button_released), bouncetime = 30) # detect button 2 released    
"""

while True:
    try:
        #GPIO.wait_for_edge(Input_Button_1, GPIO.FALLING) # detect button 1 release
        #    my_callback=(Output_Relay_1,Output_Relay_1,Button_released)
        #if (GPIO.add_event_detect(Input_Button_1,GPIO.FALLING, bouncetime=300)): # detect button 1 release
        #    my_callback=(Output_Relay_1,Output_Relay_1,Button_released)
                
        #GPIO.wait_for_edge(Input_Button_1, GPIO.RISING) # detect button 1 pressed
        #GPIO.wait_for_edge(Input_Button_2, GPIO.FALLING) # detect button 2 released
        #GPIO.wait_for_edge(Input_Button_2, GPIO.RISING) # detect button 2 pressed        
            # assign which two relays to be used if 2 relays to be switched
            #my_callback=(Output_Relay_1,Output_Relay_2,Button_pressed)    # call button pressed sub routine 
        #if (GPIO.add_event_detect(Input_Button_1,GPIO.RISING, bouncetime=300)): # detect button 1 release
        #    my_callback=(Output_Relay_1,Output_Relay_1,Button_released)
        """
        if (GPIO.wait_for_edge(Input_Button_2,GPIO.FALLING, bouncetime=300)): # detect button 2 release
            my_callback(Output_Relay_2,Output_Relay_2,Button_released)
                
        if (GPIO.wait_for_edge(Input_Button_2,GPIO.RISING, bouncetime=300)): # detect button 2 pressed
            # assign which two relays to be used if 2 relays to be switched
            my_callback(Output_Relay_1,Output_Relay_2,Button_pressed)    # call button pressed sub routine
        """    
        """
        # if button_pressed_timer_active true the capture the eplased time
        if (button_pressed_timer_active == True):
            if elapsed_time >=10:
                button_pressed_timer_active == False # turn off the button_pressed_timer_active stop process
        """        
    except ValueError:
        print ("Opps error, re-try....")
        GPIO.cleanup

    finally:
        GPIO.cleanup
            
        

