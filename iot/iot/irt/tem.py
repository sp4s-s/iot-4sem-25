from smbus2 import SMBus
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)

print(f"Ambient Temp: {sensor.get_amb_temp()} °C")
print(f"Object Temp : {sensor.get_obj_temp()} °C")

bus.close()
