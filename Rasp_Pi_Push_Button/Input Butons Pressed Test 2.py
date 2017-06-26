import RPi.GPIO as GPIO
import time
prev_input = 0
bounce_input = 0
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
        
    def Display_Button_Pressed (x_button):
        if (x_button == "Up"):
            print ("Up Pressed")
        if (x_button == "Down"):
            print ("Down Pressed")
        if (x_button == "Select"):
            print ("Select Pressed")
        if (x_button == "Menu"):
            print ("Menu Pressed")

    def Relay_Control (Rel_Switch):
        if (Rel_Switch == 22):
            print ("Relay 1")
            
        if (Rel_Switch == 24):
            print ("Relay 2")

        if (Rel_Switch == 25):
            print ("Relay 3")

        if (Rel_Switch == 8):
            print ("Relay 4")
            
''' def rel1_Rising_callback(channel):
            print ("Relay 1 on ")
            
    def rel1_Falling_callback(channel):
            print ("Relay 1 off ")
        
    def rel2_Rising_callback(channel):
            print ("Relay 2 on ")
            
    def rel2_Falling_callback(channel):
            print ("Relay 2 off ")
'''
def my_callback(channel):
    if (GPIO.input(Input_Button_1)):
        print ("Relay 1 on ") # port 17 on
    else:
        print ("Relay 1 off ") # port 17 off

    if (GPIO.input(Input_Button_2)):
        print ("Relay 1 on ") # port 18 on
    else:
        print ("Relay 1 off ") # port 18 off
        

while True:
    try:
        if ((GPIO.input(Input_Button_1) == True)) :
            #GPIO.add_event_detect(17, GPIO.RISING, callback=rel1_Rising_callback)
            GPIO.add_event_detect(Input_Button_1, GPIO.BOTH, callback=my_callback)
            #GPIO.add_event_detect(17, GPIO.FALLING, callback=rel1_Falling_callback)

        if ((GPIO.input(Input_Button_2) == True)):
            #GPIO.add_event_detect(18, GPIO.RISING, callback=rel2_Rising_callback)
            GPIO.add_event_detect(Input_Button_2, GPIO.BOTH, callback=my_callback)
            #GPIO.add_event_detect(18, GPIO.FALLING, callback=rel2_Falling_callback)
        
        

        #elif ((GPIO.input(27) == True) and (prev_input != 27)):
        #elif ((GPIO.input(23) == True) and (prev_input != 23)):
         


        """
        if ((GPIO.input(17) == True) and (prev_input != 17)):
            Display_Button_Pressed ('Up')
            prev_input = 17
            #time.sleep(0.05)

        elif ((GPIO.input(18) == True) and (prev_input != 18)):
            Display_Button_Pressed ('Down')
            prev_input = 18
            #time.sleep(0.05)

        elif ((GPIO.input(27) == True) and (prev_input != 27)):
            Display_Button_Pressed ('Select')
            prev_input = 27
            time.sleep(0.05)

        elif ((GPIO.input(23) == True) and (prev_input != 23)):
            Display_Button_Pressed ('Menu')
            prev_input = 23
            time.sleep(0.05)

        elif ((GPIO.input(17) == False) and (GPIO.input(18) == False) and (GPIO.input(27) == False) and (GPIO.input(23) == False) and (prev_input != 0)):
            prev_input = 0
            time.sleep(0.05)
        

        #elif (GPIO.input(25) == True):
        #    break
    """

    except ValueError:
        print ("Opps error, re-try....")
        GPIO.cleanup

    finally:
        GPIO.cleanup
            
        

