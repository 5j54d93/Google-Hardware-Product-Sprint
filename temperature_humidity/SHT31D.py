import adafruit_sht31d
import board
import busio
import time

class SHT31D:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.SHT31D = adafruit_sht31d.SHT31D(i2c, 0x44)
        self.readcount = 0
    
    def heater_on(self, second):
        self.SHT31D.heater = True
        time.sleep(second)
        self.SHT31D.heater = False
    
    def temperature_C(self):
        self.readcount += 1
        if self.readcount == 10 :
           self.readcount = 0
           self.heater_on(1)
        return self.SHT31D.temperature
    
    def temperature_F(self):
        self.readcount += 1
        if self.readcount == 10 :
           self.readcount = 0
           self.heater_on(1)
        return self.SHT31D.temperature * 9 / 5 + 32
    
    def humidity(self):
        self.readcount += 1
        if self.readcount == 10 :
           self.readcount = 0
           self.heater_on(1)
        return self.SHT31D.relative_humidity
    
    def cold_or_hot(self):
        temperature_C = self.temperature_C()
        if   temperature_C >= 27 : return "It's very hot！！"
        elif temperature_C >= 23 : return "It's hot！"
        elif temperature_C >= 21 : return "It's warm."
        elif temperature_C >= 17 : return "It's comfortable～"
        elif temperature_C >=  9 : return "It's cool."
        elif temperature_C >=  1 : return "It's cold！"
        else                     : return "It's very cold！！"
    
    def dry_or_wet_plant(self):
        humidity = self.humidity()
        temperature_C = self.temperature_C()
        if humidity >= 80 : return "It's humid for plants！"
        elif humidity >= 60 and humidity < 80 and temperature_C >= 22 and temperature_C <= 32 : return 'Plants feel comfortable～'
        elif humidity >= 60 and humidity < 80 : return "It's good for plants."
        else : return "It's dry for plants！"
    
    def dry_or_wet_people(self):
        humidity = self.humidity()
        temperature_C = self.temperature_C()
        if humidity >= 65 : return "It's humid for people！"
        elif humidity >= 45 and humidity < 65 and temperature_C >= 18 and temperature_C <= 23 : return "People feel comfortable～"
        elif humidity >= 45 and humidity < 65 : return "It's good for people."
        else : return "It's dry for people！"
