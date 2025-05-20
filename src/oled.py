from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time

# OLED display setup
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

try:
    while True:
        with canvas(device) as draw:
            draw.text((0, 0), "Starting...\n Current Status===== \n Temp: 36C \. 🍐", fill="white")
        time.sleep(2)

        with canvas(device) as draw:
            draw.text((0, 0), "Starting...\n Current Status===== \n Temp: 36C \. 🍐", fill="red")
        time.sleep(2)
except KeyboardInterrupt:
    pass
