#!/usr/bin/env python
# Import proper libraries
import RPi.GPIO as GPIO  
import time  
import os

# Use BCM pin numbering scheme
GPIO.setmode(GPIO.BCM)

# Set pin 17 as the INPUT (change 17 if you are using a different pin)
button_pin = 17
GPIO.setup(button_pin, GPIO.IN)

# Keep track of the button's previous state to ensure it only triggers once per press
prev_state = 0 

print("Waiting for button press...")

try:
    while True:
        # Read the current state
        curr_state = GPIO.input(button_pin)
        
        # Check if the state changed from 0 (unpressed) to 1 (pressed)
        if curr_state == 1 and prev_state == 0:
            print("Button Pressed! Pinging google.com...")
            
            # Execute the Linux ping command. 
            # -c 1 ensures it only pings once instead of infinitely.
            os.system("ping -c 1 google.com")
            
            time.sleep(0.05)  # 50ms delay to debounce the physical switch
            
        # Update the previous state for the next loop iteration
        prev_state = curr_state

except KeyboardInterrupt:
    # Clean up the GPIO pins if the user exits the program with Ctrl+C
    GPIO.cleanup()
