import RPi.GPIO as GPIO
import time

RELAY_PIN = 17

GPIO.setmode(GPIO.BCM)

# Set as output first
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Then immediately set HIGH to keep relay OFF
GPIO.output(RELAY_PIN, GPIO.HIGH)

# Now safe to use
print("Relay de-energized (HIGH)")
time.sleep(2)

GPIO.output(RELAY_PIN, GPIO.LOW)  # Activate relay
print("Relay energized (LOW)")
time.sleep(2)

GPIO.output(RELAY_PIN, GPIO.HIGH)
print("Relay off again")
GPIO.cleanup()
