import adafruit_bmp280
import board
import busio


# Initialize I2C bus and sensors
i2c_bus = busio.I2C(board.SCL, board.SDA)

bmp_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c_bus, address=0x76)

def get_ambient_temp():
    

    return bmp_sensor.temperature

print(get_ambient_temp())