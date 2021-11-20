from flask import Flask, render_template, request
from acceleration.ADXL203EB import ADXL203EB
from air_quality.SGP30 import SGP30
from bump.Bump import Bump
from buzzer.Buzzer import Buzzer
from light.APDS9960 import APDS
from temperature_humidity.SHT31D import SHT31D
from datetime import datetime

app = Flask("Demeter")
acceleration = ADXL203EB()
air_quality = SGP30()
bump = Bump()
buzzer = Buzzer()
light = APDS()
temperature_humidity = SHT31D()

@app.route("/", methods=['GET', 'POST'])
def home():
    bump.auto_watering()
    buzzer.auto_noising()
    if request.method == 'POST':
        if request.form.get('Watering') == 'Watering':
            bump.watering()
            bump.update_last_watering_time()
            return reload()
        elif request.form.get('Noise') == 'Noise':
            buzzer.noising()
            buzzer.update_last_noise_time()
            return reload()
    return reload()

def reload():
    return render_template('home.html',
                           air_quality = air_quality.good_or_bad(),
                           eCO2 = air_quality.eCO2(),
                           TVOC = air_quality.TVOC(),
                           acceleration_x = acceleration.X(),
                           acceleration_y = acceleration.Y(),
                           stable_or_sway = acceleration.stable_or_sway(),
                           bright_or_dark = light.bright_or_dark(),
                           light_value = round(light.light_value(),2),
                           light_value_percentage = round(light.light_value_percentage(),2),
                           light_color_temperature = round(light.light_color_temperature(),2),
                           cold_or_hot = temperature_humidity.cold_or_hot(),
                           temperature_C = round(temperature_humidity.temperature_C(),2),
                           temperature_F = round(temperature_humidity.temperature_F(),2),
                           dry_or_wet_plant = temperature_humidity.dry_or_wet_plant(),
                           dry_or_wet_people = temperature_humidity.dry_or_wet_people(),
                           humidity = round(temperature_humidity.humidity(),2),
                           year = datetime.now().year,
                           month = datetime.now().month,
                           day = datetime.now().day,
                           hour = str(datetime.now().hour).zfill(2),
                           min = str(datetime.now().minute).zfill(2),
                           last_watering_time = bump.last_watering_time(),
                           upon_last_watering_time = bump.upon_last_watering_time(),
                           last_noise_time = buzzer.last_noise_time(),
                           upon_last_noise_time = buzzer.upon_last_noise_time(),
                          )

if __name__ == '__main__' : app.run(debug=True, port=80, host='0.0.0.0')
