# doorbell.py
import RPi.GPIO as GPIO
import os
import time

# Pin configuration
BUTTON_PIN = 18

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Button pressed
            os.system("aplay doorbell_sound.wav")  # Play sound
            time.sleep(1)  # Debounce
except KeyboardInterrupt:
    GPIO.cleanup()