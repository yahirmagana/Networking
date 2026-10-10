#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import subprocess

# Set up the GPIO pin for the LED
LED_PIN = 18  # Change this to whatever BCM pin you are using for the LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def get_icmp_count():
    """Runs netstat -s and extracts the number of received ICMP messages."""
    try:
        # Run the netstat command and decode the output
        output = subprocess.check_output("netstat -s", shell=True, text=True)
        
        # Search line-by-line for the ICMP received count
        for line in output.split('\n'):
            if "ICMP messages received" in line:
                # The line usually looks like "    123 ICMP messages received"
                # split()[0] grabs the first string of non-whitespace characters (the number)
                return int(line.strip().split()[0])
    except Exception as e:
        print(f"Error reading netstat: {e}")
    
    return 0

print("Monitoring for incoming pings...")

# Initialize tracking variables
last_count = get_icmp_count()
last_ping_time = 0
timeout = 3  # Number of seconds to keep the LED on after the pinging stops

try:
    while True:
        current_count = get_icmp_count()
        
        # If the count is higher than before, we received a new ping
        if current_count > last_count:
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
            last_ping_time = time.time()     # Reset the timer
            print(f"Ping detected! Total ICMP received: {current_count}")
        
        # If the timer has exceeded the timeout, turn the LED off
        if time.time() - last_ping_time > timeout:
            GPIO.output(LED_PIN, GPIO.LOW)
            
        # Update the previous count for the next loop iteration
        last_count = current_count
        
        # Wait 1 second before checking again
        time.sleep(1)

except KeyboardInterrupt:
    # Safely turn off the LED and clean up pins when exiting with Ctrl+C
    GPIO.cleanup()
