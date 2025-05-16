import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BOARD)
ppin = 11
gp.setup(ppin, gp.OUT)

def pon():
	print("ON")
	gp.output(ppin, gp.HIGH)
def poff():
	print("OFF")
	gp.output(ppin, gp.LOW)

try:
	while True:
		pon()
		sleep(3)
		poff()
		sleep(3)
except KeyboardInterrupt:
	gp.cleanup()

