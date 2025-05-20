import RPi.GPIO as GPIO
import time

RELAY_PIN = 2  # GPIO2 = Pin 3

GPIO.setmode(GPIO.BCM)

# Setup GPIO2 as output
GPIO.setup(RELAY_PIN, GPIO.OUT)

# De-energize relay by default
GPIO.output(RELAY_PIN, GPIO.HIGH)
print("Relay OFF (HIGH)")
time.sleep(2)

# Energize relay (motor ON)
GPIO.output(RELAY_PIN, GPIO.LOW)
print("Relay ON (LOW)")
time.sleep(2)

# Turn off again
GPIO.output(RELAY_PIN, GPIO.HIGH)
print("Relay OFF again")

GPIO.cleanup()

