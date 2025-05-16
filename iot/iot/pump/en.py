import RPi.GPIO as GPIO
import time

RELAY_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    print("Turning motor ON (relay energized)...")
    GPIO.output(RELAY_PIN, GPIO.LOW)  # Energize relay (motor ON)
    time.sleep(2)
    print("Turning motor OFF (relay de-energized)...")
    GPIO.output(RELAY_PIN, GPIO.HIGH) # De-energize relay (motor OFF)
    time.sleep(0)

finally:
    GPIO.cleanup()
