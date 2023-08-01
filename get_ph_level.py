import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import busio
import board


# Initialize I2C bus and sensors
i2c_bus = busio.I2C(board.SCL, board.SDA)

#Initialize ADS pH Sensor
ads = ADS.ADS1115(i2c_bus)
ads_channel = AnalogIn(ads, ADS.P0)

def get_ph_level():

    buf = list()

    for i in range(10): # Take 10 samples
        buf.append(ads_channel.voltage)
    buf.sort() # Sort samples and discard highest and lowest
    buf = buf[2:-2]
    ph_level = (sum(map(float,buf))/6) # Get average value from remaining 6
    
 
    return ph_level

if __name__ == "__main__":
    print(get_ph_level())
