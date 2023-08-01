import adafruit_onewire
import os
import glob


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def get_tank_temp():

    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.1)
        lines = f.readlines()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        tank_temp = float(temp_string) / 1000.0
        temp_f = tank_temp * 9.0 / 5.0 + 32.0
        
        return tank_temp

if __name__ == "__main__":
    print(get_tank_temp())
