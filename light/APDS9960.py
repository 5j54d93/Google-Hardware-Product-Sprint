from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
import board
import time

class APDS:
    def __init__(self):
        i2c = board.I2C()
        self.APDS9960 = APDS9960(i2c)
        self.APDS9960.enable_color = True
    
    def light_value(self):
        while not self.APDS9960.color_data_ready : time.sleep(0.005)
        r,g,b,c = self.APDS9960.color_data
        return colorutility.calculate_lux(r, g, b)

    def light_value_percentage(self):
        return self.light_value() / 34196.163 * 100
    
    def light_color_temperature(self):
        while not self.APDS9960.color_data_ready : time.sleep(0.005)
        r,g,b,c = self.APDS9960.color_data
        return colorutility.calculate_color_temperature(r, g, b)
    
    def bright_or_dark(self):
        if self.light_value_percentage() >= 50 : return 'Bright enough！'
        else : return "It's not bright enough！"
