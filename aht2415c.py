import time
import smbus

# I2C address for AHT2415C
AHT_SENSOR_ADDR = 0x38

# Commands to initiate sensor readings
INIT_CMD = [0xBE, 0x08, 0x00]
READ_CMD = [0xAC, 0x33, 0x00]

# Initialize I2C bus
bus = smbus.SMBus(1)  # 1 for Raspberry Pi's I2C bus 1

def init_sensor():
    """Initialize the AHT2415C sensor"""
    bus.write_i2c_block_data(AHT_SENSOR_ADDR, INIT_CMD[0], INIT_CMD[1:])
    time.sleep(0.5)

def read_data():
    """Read temperature and humidity from AHT2415C"""
    bus.write_i2c_block_data(AHT_SENSOR_ADDR, READ_CMD[0], READ_CMD[1:])
    time.sleep(0.5)

    data = bus.read_i2c_block_data(AHT_SENSOR_ADDR, 0x00, 6)

    # Convert the data
    humidity = ((data[1] & 0x3F) << 8) + data[2]
    humidity = humidity * 100.0 / 16383.0

    temperature = ((data[3] & 0x3F) << 8) + data[4]
    temperature = (temperature * 165.0 / 16383.0) - 40.0

    return temperature, humidity

# Main loop
init_sensor()
while True:
    temperature, humidity = read_data()
    print(f"Temperature: {temperature:.2f} °C")
    print(f"Humidity: {humidity:.2f} %")
    time.sleep(2)