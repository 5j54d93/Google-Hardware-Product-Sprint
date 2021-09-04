from temperature_humidity.SHT31D import SHT31D
import adafruit_sgp30
import board
import busio
import math

class SGP30:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.SGP30 = adafruit_sgp30.Adafruit_SGP30(i2c)
        self.SGP30.iaq_init()
        self.SGP30.set_iaq_baseline(0x8973, 0x8AAE)
        
        self.SHT31D = SHT31D()
        RH = self.SHT31D.humidity()
        t = self.SHT31D.temperature_C()
        AH = 216.7 * ((RH / 100.0) * 6.112 * math.exp((17.62 * t) / (243.12 + t)) / (273.15 + t))
        self.SGP30.set_iaq_humidity(AH)
    
    def eCO2(self):
        return self.SGP30.eCO2
    
    def TVOC(self):
        return self.SGP30.TVOC
    
    def Ethanol(self):
        return self.SGP30.Ethanol # maybe ppb
    
    def H2(self):
        return self.SGP30.H2 # maybe ppb

    def good_or_bad(self):
        # CO₂ standard：average 1000 ppm within 8 hours
        # TVOC standard：average 560 ppb within 1 hours
        if self.eCO2() <= 1000 and self.TVOC() <= 560 : return "Can't be better～"
        elif self.eCO2() > 1000 and self.TVOC() <= 560 : return 'CO₂ is too high！'
        elif self.eCO2() <= 1000 and self.TVOC() <= 560 : return 'TVOC is too high！'
        else : return 'Air quality is so bad！'
