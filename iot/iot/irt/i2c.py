import smbus2
import time

I2C_ADDR = 0x5A
AMBIENT_REG = 0x06
OBJECT_REG = 0x07

def read_temp(bus, reg):
    try:
        data = bus.read_word_data(I2C_ADDR, reg)
        # Swap bytes
        data = (data << 8 & 0xFF00) + (data >> 8)
        return data * 0.02 - 273.15
    except Exception as e:
        print(f"I2C read error: {e}")
        return None

bus = smbus2.SMBus(1)

while True:
    amb = read_temp(bus, AMBIENT_REG)
    obj = read_temp(bus, OBJECT_REG)
    print(f"Ambient: {amb:.2f} °C | Object: {obj:.2f} °C")
    time.sleep(1)
