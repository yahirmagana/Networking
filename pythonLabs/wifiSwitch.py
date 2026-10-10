#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import subprocess

# Pin Configuration
SW_DISABLE_PIN = 17  
SW_ENABLE_PIN = 27   
LED_PIN = 18         

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW_DISABLE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW_ENABLE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

def has_valid_ip():
    """Checks if the Raspberry Pi has a valid, fully connected IP address."""
    try:
        output = subprocess.check_output("hostname -I", shell=True, text=True).strip()
        # Ensure we have an output AND it isn't a disconnected 169.254.x.x fallback IP
        if len(output) > 0 and not output.startswith("100."):
            return True
        return False
    except subprocess.CalledProcessError:
        return False

print("Starting WiFi Control... Press Ctrl+C to exit.")

led_state = False
last_blink_time = 0
blink_interval = 0.5 

try:
    while True:
        # 1. Check Disable Switch
        if GPIO.input(SW_DISABLE_PIN) == GPIO.HIGH:
            print("Disable Switch pressed! Turning WiFi OFF...")
            # Use modern NetworkManager command to disable WiFi
            subprocess.call("nmcli radio wifi off", shell=True)
            time.sleep(1)  # Longer delay to prevent rapid double-presses
            
        # 2. Check Enable Switch
        if GPIO.input(SW_ENABLE_PIN) == GPIO.HIGH:
            print("Enable Switch pressed! Turning WiFi ON...")
            # Use modern NetworkManager command to enable and auto-reconnect
            subprocess.call("nmcli radio wifi on", shell=True)
            time.sleep(1)

        # 3. Check IP address status and control LED
        if not has_valid_ip():
            # No valid IP -> Blink the LED
            current_time = time.time()
            if current_time - last_blink_time >= blink_interval:
                led_state = not led_state  
                GPIO.output(LED_PIN, GPIO.HIGH if led_state else GPIO.LOW)
                last_blink_time = current_time
        else:
            # Valid IP exists -> Ensure LED is completely OFF
            GPIO.output(LED_PIN, GPIO.LOW)
            led_state = False

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nExiting and cleaning up GPIO...")
    GPIO.cleanup()
