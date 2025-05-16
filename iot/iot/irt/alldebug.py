import time
from smbus2 import SMBus
from mlx90614 import MLX90614

I2C_BUSES = [1, 2]
POSSIBLE_MLX90614_ADDRS = [0x5A, 0x3A, 0x1A, 0x0A]

def try_sensor(bus, address):
    try:
        sensor = MLX90614(bus, address=address)
        amb = sensor.get_amb_temp()
        obj = sensor.get_obj_temp()
        print(f"    [0x{address:02X}] Ambient: {amb:.2f} °C | Object: {obj:.2f} °C")
        return True
    except OSError as e:
        print(f"    [0x{address:02X}] I2C OSError: {e}")
    except Exception as e:
        print(f"    [0x{address:02X}] Other error: {e}")
    return False

def main():
    print("=== MLX90614 Full I2C Bus + Address Debug ===\n")
    working = []

    for bus_num in I2C_BUSES:
        print(f"Checking I2C bus /dev/i2c-{bus_num}...")
        try:
            with SMBus(bus_num) as bus:
                for addr in POSSIBLE_MLX90614_ADDRS:
                    print(f"  Trying address 0x{addr:02X}...")
                    if try_sensor(bus, addr):
                        working.append((bus_num, addr))
                    time.sleep(0.1)
        except FileNotFoundError:
            print(f"  Bus /dev/i2c-{bus_num} not found or not enabled.")
        except Exception as e:
            print(f"  Unexpected error on bus {bus_num}: {e}")
        print()

    print("=== Scan Complete ===")
    if working:
        for bus_num, addr in working:
            print(f"✓ Sensor detected on bus {bus_num} at address 0x{addr:02X}")
    else:
        print("✗ No MLX90614 sensors detected on buses checked.")

if __name__ == "__main__":
    main()
