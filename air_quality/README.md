# [Air quality sensor：SGP30 TVOC/eCO2 Gas Sensor](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-sgp30-gas-tvoc-eco2-mox-sensor.pdf)
<img src="https://github.com/5j54d93/Google-HPS/blob/main/air_quality/photo/SGP30.png" width='78%' height='78%'/>

- I2C interface
- typical accuracy of 15%
- intended for indoor air quality monitoring
- SGP30 can detect a wide range of Volatile Organic Compounds（VOCs）and H₂
- SGP30 will return a Total Volatile Organic Compound（TVOC）reading and an equivalent carbon dioxide reading（eCO2）
- eCO2（equivalent calculated carbon-dioxide）concentration within a range of 400 to 60000 ppm
- TVOC（Total Volatile Organic Compound）concentration within a range of 0 to 60000 ppb
- eCO2 is calculated based on H₂ concentration, so it's not a 'true' CO2 sensor for laboratory use
- SGP30 is the able to set humidity compensation for better accuracy. An external humidity sensor is required and then the RH% is written over I2C to the sensor, so it can better calculate the TVOC/eCO2 values.

## Overview

- [SGP30 wired to Raspberry Pi with I2C](https://github.com/5j54d93/Google-HPS/blob/main/air_quality/README.md#sgp30-wired-to-raspberry-pi-with-i2c)
  - [Raspberry Pi GPIO Pin](https://github.com/5j54d93/Google-HPS/blob/main/air_quality/README.md#raspberry-pi-gpio-pin)
  - [Check the I2C devices](https://github.com/5j54d93/Google-HPS/blob/main/air_quality/README.md#check-the-i2c-devices)
- [Install Libraries](https://github.com/5j54d93/Google-HPS/blob/main/air_quality/README.md#install-libraries)
  - [CircuitPython](https://github.com/5j54d93/Google-HPS/blob/main/air_quality/README.md#circuitpython)
  - [Adafruit's CircuitPython library bundle](https://github.com/5j54d93/Google-HPS/blob/main/air_quality/README.md#adafruits-circuitpython-library-bundle)
  - [adafruit_sgp30.mpy](https://github.com/5j54d93/Google-HPS/blob/main/air_quality/README.md#adafruit_sgp30mpy)
  - [adafruit_bus_device](https://github.com/5j54d93/Google-HPS/blob/main/air_quality/README.md#adafruit_bus_device)
- [Using the SGP30 with CircuitPython and the Adafruit library](https://github.com/5j54d93/Google-HPS/blob/main/air_quality/README.md#using-the-sgp30-with-circuitpython-and-the-adafruit-library)
  - [Docs](https://github.com/5j54d93/Google-HPS/blob/main/air_quality/README.md#docs)
- [Single Page Reference](https://github.com/5j54d93/Google-HPS/blob/main/air_quality/README.md#single-page-reference)

## [SGP30 wired to Raspberry Pi with I2C](https://www.circuito.io/app?components=9443,35286,200000)
<img src="https://github.com/5j54d93/Google-HPS/blob/main/air_quality/photo/SGP30%20wired%20to%20Raspberry%20Pi%20with%20I2C.png" width='45%' height='45%'/>

|SGP30|Raspberry Pi|
|:-:|:-:|
|VIN|3V3|
|GND|GND|
|SCL|SCL|
|SDA|SDA|

### Raspberry Pi GPIO Pin
- **3V3**：1、17
- **GND**：6、9、14、20、25、30、34、39
- **SCL**：5
- **SDA**：3
<img src="https://github.com/5j54d93/Google-HPS/blob/main/photo/Raspberry%20Pi%20GPIO.png" width='95%' height='95%'/>

### Check the I2C devices

- **SGP30**：`0x58`

```shell
pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- 58 -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

## Install Libraries

### [CircuitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)

```shell
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```

### [Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle)

```shell
pip3 install adafruit-circuitpython-lis3dh
```

### [adafruit_sgp30.mpy](https://github.com/adafruit/Adafruit_CircuitPython_SGP30)

```shell
pip3 install adafruit-circuitpython-sgp30
```

### [adafruit_bus_device](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/tree/5aceeae814effae4eb950f1078c194b11401faa7)

```shell
pip3 install adafruit-circuitpython-busdevice
```

## [Using the SGP30 with CircuitPython and the Adafruit library](https://github.com/adafruit/Adafruit_CircuitPython_SGP30/blob/main/examples/sgp30_simpletest.py)

```python
import time
import board
import busio
import adafruit_sgp30

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

print("SGP30 serial #", [hex(i) for i in sgp30.serial])

# IAQ algorithm：convert H₂ to eCO₂
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8AAE)

elapsed_sec = 0

while True:
    # read values：eCO₂ & TVOC
    print("eCO₂ = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))     
    time.sleep(1) # wait
    elapsed_sec += 1
    # every 10 passes print baseline values (relevant to IAQ algorithm)
    if elapsed_sec > 10:
        elapsed_sec = 0
        print("**** Baseline values: eCO₂ = 0x%x, TVOC = 0x%x" % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))
```

### Docs
- [`busio.I2C()`](https://circuitpython.readthedocs.io/en/latest/shared-bindings/busio/#busio.I2C)
- [`adafruit_sgp30.Adafruit_SGP30()`](https://circuitpython.readthedocs.io/projects/sgp30/en/latest/api.html#adafruit_sgp30.Adafruit_SGP30)
- [`sgp30.iaq_init()`](https://circuitpython.readthedocs.io/projects/sgp30/en/latest/api.html?highlight=iaq_init#adafruit_sgp30.Adafruit_SGP30.iaq_init)
- [`sgp30.set_iaq_baseline()`](https://circuitpython.readthedocs.io/projects/sgp30/en/latest/api.html?highlight=set_iaq_baseline#adafruit_sgp30.Adafruit_SGP30.set_iaq_baseline)
- [`sgp30.eCO2`](https://circuitpython.readthedocs.io/projects/sgp30/en/latest/api.html?highlight=eCO2#adafruit_sgp30.Adafruit_SGP30.eCO2)
- [`sgp30.TVOC`](https://circuitpython.readthedocs.io/projects/sgp30/en/latest/api.html?highlight=TVOC#adafruit_sgp30.Adafruit_SGP30.TVOC)
- [`sgp30.baseline_eCO2`](https://circuitpython.readthedocs.io/projects/sgp30/en/latest/api.html?highlight=baseline_eCO2#adafruit_sgp30.Adafruit_SGP30.baseline_eCO2)
- [`sgp30.baseline_TVOC`](https://circuitpython.readthedocs.io/projects/sgp30/en/latest/api.html?highlight=baseline_TVOC#adafruit_sgp30.Adafruit_SGP30.baseline_TVOC)

## Single Page Reference

- [Overview｜Adafruit SGP30 TVOC/eCO2 Gas Sensor｜Adafruit Learning System](https://learn.adafruit.com/adafruit-sgp30-gas-tvoc-eco2-mox-sensor?view=all)
- [SGP30 中文使用說明](https://sharing-life-in-tw.blogspot.com/2021/08/Raspberry-Pi-SGP30.html)
