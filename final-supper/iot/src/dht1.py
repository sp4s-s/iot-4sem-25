import time
import board
import adafruit_dht

dht_device = adafruit_dht.DHT11(board.D4, use_pulseio=False)

while True:
    try:
        temp = dht_device.temperature
        hum = dht_device.humidity
        print(f"Temperature in C : {temp:.1f}C,     Humidity:  {hum:.1f}%")

    except RuntimeError as error:
        print(f"Reading error: {error.args[0]}")
    time.sleep(2.0)
