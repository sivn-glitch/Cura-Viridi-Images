import adafruit_amg88xx
import busio
import board
import numpy as np


i2c_bus = busio.I2C(board.SCL, board.SDA)

amg_sensor = adafruit_amg88xx.AMG88XX(i2c_bus)

def get_thermal_rgb():
    temperatures = amg_sensor.pixels
    colors = []
    for temp_row in temperatures:
        color_row = []
        for temp in temp_row:
            r, g, b = 0, 0, 0
            if temp < 20:
                b = (temp - 0) / (20 - 0)
            elif temp < 30:
                g = (temp - 20) / (30 - 20)
                b = 1 - g
            else:
                r = (temp - 30) / (80 - 30)
                g = 1 - r
            color_row.append((r * 255, g * 255, b * 255))
        colors.append(color_row)
        arr_list = np.array(colors)
        arr_list = arr_list.tolist()
    return arr_list 

if __name__ == "__main__":
    print(get_thermal_rgb())

