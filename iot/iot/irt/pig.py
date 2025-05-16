import pigpio

pi = pigpio.pi()
handle = pi.i2c_open(1, 0x5A)  # 1 = bus, 0x5A = MLX90614

(count, data) = pi.i2c_read_i2c_block_data(handle, 0x06, 3)  # ambient temp
print(data)

pi.i2c_close(handle)
