import smbus2
import time

I2C_ADDR = 0x5A
AMBIENT_REG = 0x06
OBJECT_REG = 0x07

def read_temp(bus, reg):
    raw = bus.read_word_data(I2C_ADDR, reg)
    raw = (raw << 8 & 0xFF00) + (raw >> 8)
    return raw, raw * 0.02 - 273.15

bus = smbus2.SMBus(1)
time.sleep(0.2)

while True:
    try:
        raw_amb, amb = read_temp(bus, AMBIENT_REG)
        raw_obj, obj = read_temp(bus, OBJECT_REG)
        print(f"Raw: {raw_amb}, {raw_obj} → Ambient: {amb:.2f} °C  | Object: {obj:.2f} °C")
    except Exception as e:
        print(f"Read error: {e}")
    time.sleep(1)
