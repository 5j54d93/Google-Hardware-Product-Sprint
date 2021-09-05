from temperature_humidity.SHT31D import SHT31D
from datetime import datetime
import RPi.GPIO as GPIO
import time

class Bump:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.RELAY = 24
        GPIO.setup(self.RELAY, GPIO.OUT)
        self.SHT31D = SHT31D()
        self.last_watering_month = 0
        self.last_watering_day = 0
        self.last_watering_hour = 0
        self.last_watering_min  = 0
    
    def last_watering_time(self):
        if self.last_watering_hour == 0 and self.last_watering_min == 0 : return "未澆過水"
        return str(self.last_watering_month) + '/' + str(self.last_watering_day) + ' ' + str(self.last_watering_hour).zfill(2) + ':' + str(self.last_watering_min).zfill(2)
    
    def upon_last_watering_time(self):
        if self.last_watering_hour == 0 and self.last_watering_min == 0 : return "未澆過水"
        return str(datetime.now().hour * 60 + datetime.now().minute - self.last_watering_hour * 60 - self.last_watering_min)
    
    def update_last_watering_time(self):
        self.last_watering_month = datetime.now().month
        self.last_watering_day = datetime.now().day
        self.last_watering_hour = datetime.now().hour
        self.last_watering_min  = datetime.now().minute
    
    def watering(self):
        GPIO.output(self.RELAY, GPIO.HIGH)          
        time.sleep(3)
        GPIO.output(self.RELAY, GPIO.LOW)
        self.update_last_watering_time()
    
    def auto_watering(self):
        if self.SHT31D.dry_or_wet_plant() == "It's dry for plants！" :
            if self.upon_last_watering_time() == "Haven't watering yet." or self.upon_last_watering_time() >= '720' :
                self.watering()
                self.update_last_watering_time()
