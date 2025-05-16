import RPi.GPIO as g
import time

g.setmode(g.BCM)

relay = 17
g.setup(relay, g.OUT)

try:
    while True:
        g.output(relay, g.LOW)
        print("Relay ON")
        time.sleep(5)


        g.output(relay, g.HIGH)
        print("Relay OFF")
        time.sleep(5)

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    g.cleanup()
