from flask import Flask, render_template, request
from acceleration.ADXL203EB import ADXL203EB
from air_quality.SGP30 import SGP30
from bump.Bump import Bump
from buzzer.Buzzer import Buzzer
from light.APDS9960 import APDS9960
from temperature_humidity.SHT31D import SHT31D

app = Flask("Demeter")
acceleration = ADXL203EB()
air_quality = SGP30()
bump = Bump()
buzzer = Buzzer()
light = APDS9960()
temperature_humidity = SHT31D()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('Noise') == 'Noise':
            timeInfo.update_last_noise_year(datetime.datetime.now().year)
            timeInfo.update_last_noise_month(datetime.datetime.now().month)
            timeInfo.update_last_noise_day(datetime.datetime.now().day)
            timeInfo.update_last_noise_hour(datetime.datetime.now().hour)
            timeInfo.update_last_noise_minute(datetime.datetime.now().minute)
            print('Noise')
            #無源蜂鳴器
            #p = GPIO.PWM(BUZZIER, 50)
            #p.start(50)
            #p.ChangeFrequency(523)
            #time.sleep(1)
            #p.ChangeFrequency(587)
            #time.sleep(1)
            #p.ChangeFrequency(659)
            #time.sleep(1)
            #p.stop()
            #有源蜂鳴器
            GPIO.output(BUZZIER, GPIO.LOW)
            time.sleep(5)          
            GPIO.output(BUZZIER, GPIO.HIGH)
            
            
        el
    if temperatureHumidity.auto_water() == 'true' :
        # 等於 0 初始值；或是距離上次澆水滿半天 12 小時，而且溼度又乾，就自動澆水
        if timeInfo.get_last_watering_hour() == 0 or datetime.datetime.now().hour * 60 + datetime.datetime.now().minute - timeInfo.get_last_watering_hour() * 60 - timeInfo.get_last_watering_minute() >= 720 :
           GPIO.output(RELAY, GPIO.HIGH)          
           time.sleep(3)
           GPIO.output(RELAY, GPIO.LOW)
           timeInfo.update_last_watering_month(datetime.datetime.now().month)
           timeInfo.update_last_watering_day(datetime.datetime.now().day)
           timeInfo.update_last_watering_hour(datetime.datetime.now().hour)
           timeInfo.update_last_watering_minute(datetime.datetime.now().minute)
           return render_template('home.html',
                                  last_water_time=timeInfo.get_last_watering_time(),
                                  last_noise_time=timeInfo.get_last_noise_time(),
                                  upon_last_watering_time=timeInfo.upon_last_watering_time(),
                                  upon_last_noise_time=timeInfo.upon_last_noise_time(),
                                  )
    if gsensor.auto_noise() == 'true' :
        p = GPIO.PWM(BUZZIER, 50)
        p.start(50)
        p.ChangeFrequency(523)
        time.sleep(1)
        p.ChangeFrequency(587)
        time.sleep(1)
        p.ChangeFrequency(659)
        time.sleep(1)
        p.stop()
        timeInfo.update_last_noise_month(datetime.datetime.now().month)
        timeInfo.update_last_noise_day(datetime.datetime.now().day)
        timeInfo.update_last_noise_hour(datetime.datetime.now().hour)
        timeInfo.update_last_noise_minute(datetime.datetime.now().minute)
        return render_template('home.html',
                                  last_water_time=timeInfo.get_last_watering_time(),
                                  last_noise_time=timeInfo.get_last_noise_time(),
                                  upon_last_watering_time=timeInfo.upon_last_watering_time(),
                                  upon_last_noise_time=timeInfo.upon_last_noise_time(),
                                  )
    return render_template('home.html',
                           airQuality_good_or_bad=airQuality.good_or_bad(),
                           eCO2_Data=airQuality.get_eCO2_Data(),
                           TVOC_Data=airQuality.get_TVOC_Data(),
                           gsensor_data=str(gsensor.getData()),
                           gsensor_data_y=str(gsensor.getDataY()),
                           stable_or_sway=gsensor.stable_or_sway(),
                           bright_ot_dark=light.bright_ot_dark(),
                           light_value=light.getData(),
                           coloe_lux=str(light.get_color_temperature_Data()),
                           lux_percentage = light.lux_percentage(),
                           cold_or_hot=temperatureHumidity.cold_or_hot(),
                           temperature=str(temperatureHumidity.getTemperatureData()),
                           temperatureF=str(temperatureHumidity.getTemperatureF()),
                           dry_or_wet=temperatureHumidity.dry_or_wet(),
                           dry_or_wet_people=temperatureHumidity.dry_or_wet_people(),
                           humidity=str(temperatureHumidity.getHumidityData()),
                           year=datetime.datetime.now().year,
                           month=datetime.datetime.now().month,
                           day=datetime.datetime.now().day,
                           hour=str(datetime.datetime.now().hour).zfill(2),
                           minute=str(datetime.datetime.now().minute).zfill(2),
                           last_water_time=timeInfo.get_last_watering_time(),
                           last_noise_time=timeInfo.get_last_noise_time(),
                           upon_last_watering_time=timeInfo.upon_last_watering_time(),
                           upon_last_noise_time=timeInfo.upon_last_noise_time(),
                          )

if __name__ == '__main__':
   app.run(debug=True, port=80, host='0.0.0.0')
