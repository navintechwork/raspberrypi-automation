import time
import board
import busio
from adafruit_bmp280 import Adafruit_BMP280_I2C

# Create I2C object
i2c = busio.I2C(board.SCL, board.SDA)

# Create BMP280 object (same as BME280 but without humidity)
bmp280 = Adafruit_BMP280_I2C(i2c, address=0x76)

while True:
    print(f"Temperature: {bmp280.temperature:.2f} °C")
    print(f"Pressure: {bmp280.pressure:.2f} hPa")
    print("--------------------")
    time.sleep(2)