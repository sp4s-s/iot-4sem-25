#!/usr/bin/env python3
import time
import board
import busio
import adafruit_mlx90614

# Initialize I2C bus and sensor
i2c = busio.I2C(board.SCL, board.SDA)
mlx = adafruit_mlx90614.MLX90614(i2c)

print("Measuring temperature (°C):")
while True:
    ambient = mlx.ambient_temperature
    obj = mlx.object_temperature
    print(f"Ambient: {ambient:0.2f} °C  Object: {obj:0.2f} °C")
    time.sleep(1)
