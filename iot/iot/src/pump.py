import RPi.GPIO as GPIO
import time

RELAY_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

def countdown(duration):
    interval = 0.1
    steps = int(duration / interval)
    for i in range(1, steps + 1):
        print(f"{i * interval:.1f} sec")
        time.sleep(interval)

try:
    print("Turning motor ON (relay energized)...")
    GPIO.output(RELAY_PIN, GPIO.LOW)  # Energize relay (motor ON)
    countdown(2) 

    print("Turning motor OFF (relay de-energized)...")
    GPIO.output(RELAY_PIN, GPIO.HIGH)

finally:
    GPIO.cleanup()
