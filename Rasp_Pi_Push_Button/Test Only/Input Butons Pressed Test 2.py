import RPi.GPIO as GPIO
import time
prev_input = 0
bounce_input = 0
counter_timer = 0
button_pressed_timer_active = False
start_time = 0
elapsed_time = 0
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

    def relay_1_ctl_on(arg):
        print ("Testing timer - falling ")
        elapsed_time = time.time() - start_time
        #button_pressed_timer_active ==  False
        if (elapsed_time <=20):
            GPIO.output(Output_Relay_1,GPIO.HIGH) # turn relay 1 on
            print ("Relay 1 on ") # echo which relay on
            print (elapsed_time)
        if (elapsed_time >=30) :
            GPIO.output(Output_Relay_1,GPIO.HIGH) # turn relay 1 on
            GPIO.output(Output_Relay_2,GPIO.HIGH) # turn relay 2 on
            print ("Relays 1 & 2 on ") # echo which relay/s on
            print (elapsed_time)
        return

    def relay_1_ctl_off(arg):
        print ("Relay 1 selected -timer started  - rising") 
        start_time = time.time()
        elapsed_time == 0
        return

GPIO.add_event_detect(Input_Button_1,GPIO.RISING, callback=relay_1_ctl_off, bouncetime=200)
GPIO.wait_for_edge(Input_Button_1,GPIO.RISING)
GPIO.add_event_detect(Input_Button_1,GPIO.FALLING, callback=relay_1_ctl_on, bouncetime=200)
GPIO.wait_for_edge(Input_Button_1,GPIO.FALLING)
        
while True:
    try:
        if (GPIO.input(Input_Button_2)):
            print ("Relay 2 on")
            GPIO.output(Output_Relay_2,GPIO.HIGH) # turn relay 2 on
        if (GPIO.input(Input_Button_3)):
            print ("Relay 3 on")
            GPIO.output(Output_Relay_3,GPIO.HIGH) # turn relay 3 on
            
        if (GPIO.input(Input_Button_4)):
            print ("all Relays off")
            GPIO.output(Output_Relay_1,GPIO.LOW) # turn relay 1 off
            GPIO.output(Output_Relay_2,GPIO.LOW) # turn relay 2 off
            GPIO.output(Output_Relay_3,GPIO.LOW) # turn relay 3 off

    except ValueError:
        print ("Opps error, re-try....")
        GPIO.cleanup

    finally:
        GPIO.cleanup
            
        

