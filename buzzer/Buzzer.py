from acceleration.ADXL203EB import ADXL203EB
import RPi.GPIO as GPIO
import datetime
import time

class Buzzer:
    def __init__(self):
        self.GPIO.setmode(GPIO.BCM)
        self.Buzzer = 23
        self.GPIO.setup(self.Buzzer, GPIO.OUT)
        self.ADXL203EB = ADXL203EB()
        self.last_noise_month = 0
        self.last_noise_day   = 0
        self.last_noise_hour  = 0
        self.last_noise_min   = 0
    
    def last_noise_time(self):
        if self.last_noise_hour = 0 and self.last_noise_min = 0 : return "Haven't noised yet."
        return str(self.last_noise_month) + '/' + str(self.last_noise_day) + ' ' + str(self.last_noise_hour).zfill(2) + ':' + str(self.last_noise_min).zfill(2)
    
    def upon_last_noise_time(self):
        if self.last_noise_hour = 0 and self.last_noise_min = 0 : return "Haven't noised yet."
        return datetime.now().hour * 60 + datetime.now().minute - self.last_nois_hour * 60 - self.last_nois_min
    
    def update_last_noise_time(self):
        self.last_noise_month = datetime.now().month
        self.last_noise_day = datetime.now().day
        self.last_noise_hour = datetime.now().hour
        self.last_noise_min  = datetime.now().minute
    
    def noising(self):
        b = self.GPIO.PWM(self.Buzzer, 50)
        b.start(50)
        b.ChangeFrequency(523)
        time.sleep(1)
        b.ChangeFrequency(587)
        time.sleep(1)
        b.ChangeFrequency(659)
        time.sleep(1)
        b.stop()
        self.update_last_noise_time
    
    def auto_noising(self):
        if self.ADXL203EB.stable_or_sway() == "It's swaying！" :
            self.noising
            self.update_last_noise_time
