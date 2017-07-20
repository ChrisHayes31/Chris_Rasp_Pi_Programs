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


class Button_Press_Example:

    def __init__(self):
        print ("Welcome")
    
    GPIO.add_event_detect(Input_Button_1, GPIO.RISING)

    while True:
        try:
            Input_Button_1 = GPIO.wait_for_edge(Input_Button_1, GPIO_RISING, timeout=5000)
            if Input_Button_1 is None:
                print('Timeout occurred')
            else:
                print('Edge detected on channel', Input_Button_1)

        finally:
            GPIO.cleanup()
    


