import RPi.GPIO as gp

gp.setmode(gp.BOARD)
gp.setup(3, gp.IN)
gp.setup(5, gp.OUT)

while True:
    val = gp.input(3)
    print(val)
    if val == 1:
        gp.output(5, gp.LOW)
    else:
        gp.output(5, gp.HIGH)
