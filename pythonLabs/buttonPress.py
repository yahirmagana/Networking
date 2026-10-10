#!/usr/bin/env python
# Import proper libraries
import RPi.GPIO as GPIO  
import time  

# Use BCM pin numbering scheme
GPIO.setmode(GPIO.BCM)

# Set pin 17 as the INPUT
GPIO.setup(17, GPIO.IN)

# Keep track of the button's previous state
prev_state = 0 

while True:
    # Read the current state
    curr_state = GPIO.input(17)
    
    # Check if the state changed from 0 (unpressed) to 1 (pressed)
    if curr_state == 1 and prev_state == 0:
        print("Button Pressed")
        time.sleep(0.05)  # 50ms delay to debounce the physical switch
        
    # Update the previous state for the next loop iteration
    prev_state = curr_state
