import board
import busio
import time
import sys
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Setup 
i2c_bus = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c_bus)

def read_voltage(channel):
    while True:
        buf = list()
        
        for i in range(10): # Take 10 samples
            buf.append(channel.voltage)
        buf.sort() # Sort samples and discard highest and lowest
        buf = buf[2:-2]
        avg = (sum(map(float,buf))/6) # Get average value from remaining 6

        print(round(avg,2),'V')
        time.sleep(2)

if __name__ == '__main__':
    print('\n\n\n')
    print('    RPi-ADS115-PH Calibrator    ')
    input('Ground the BNC connector and once done hit enter:')
    channel = None
    while channel not in [0,1,2,3]:
        try: 
            channel = int(input('What is the ADS1115 channel for your pH sensor (0-3): '))  
        except:
            print('Not a valid option. Enter a value between 0-3.')
    if channel == 0:
        channel = AnalogIn(ads, ADS.P0)
    elif channel == 1:
        channel = AnalogIn(ads, ADS.P1)
    elif channel == 2:
        channel = AnalogIn(ads, ADS.P1)
    elif channel == 3:
        channel = AnalogIn(ads, ADS.P1)
    else:
        sys.exit('Error selecting pin.')
    print('Adjust right potentiometer pointing the BNC to the right down to ~2.50V')
    print('Starting...Press CTRL+C to stop...')
    try:
        read_voltage(channel)
    except KeyboardInterrupt:
        pass