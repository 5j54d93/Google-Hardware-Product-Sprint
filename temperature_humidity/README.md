# [Temperature & Humidity sensor：SHT31-D](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-sht31-d-temperature-and-humidity-sensor-breakout.pdf?timestamp=1630807470)

<img src="https://github.com/5j54d93/Google-Hardware-Product-Sprint/blob/main/temperature_humidity/.github/assets/SHT31-D.png" width='78%' height='78%'/>

- I2C interface
- excellent ±2% relative humidity and ±0.3°C accuracy
- two address options
- Pin「ADR」tie to pin「Vin」could change address from `0x44` to `0x45`

## Overview

1. [**SHT31-D wired to Raspberry Pi with I2C**](https://github.com/5j54d93/Google-HPS/tree/main/temperature_humidity#sht31-d-wired-to-raspberry-pi-with-i2c)
   - [Raspberry Pi GPIO Pin](https://github.com/5j54d93/Google-HPS/tree/main/temperature_humidity#raspberry-pi-gpio-pin)
   - [Check the I2C devices](https://github.com/5j54d93/Google-HPS/tree/main/temperature_humidity#check-the-i2c-devices)
2. [**Install Libraries**](https://github.com/5j54d93/Google-HPS/tree/main/temperature_humidity#install-libraries)
   - [adafruit_sht31d.mpy](https://github.com/5j54d93/Google-HPS/tree/main/temperature_humidity#adafruit_sht31dmpy)
   - [adafruit_bus_device](https://github.com/5j54d93/Google-HPS/tree/main/temperature_humidity#adafruit_bus_device)
3. [**Using SHT31-D with Adafruit library**](https://github.com/5j54d93/Google-HPS/tree/main/temperature_humidity#using-sht31-d-with-adafruit-library)
   - [Docs](https://github.com/5j54d93/Google-HPS/tree/main/temperature_humidity#docs)
4. [**Single Page Reference**](https://github.com/5j54d93/Google-HPS/tree/main/temperature_humidity#single-page-reference)

## SHT31-D wired to Raspberry Pi with I2C

<img src="https://github.com/5j54d93/Google-Hardware-Product-Sprint/blob/main/temperature_humidity/.github/assets/SHT31-D%20wired%20to%20Raspberry%20Pi%20with%20I2C.png" width='45%' height='45%'/>

|SHT31-D|Raspberry Pi|
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

<img src="https://github.com/5j54d93/Google-Hardware-Product-Sprint/blob/main/temperature_humidity/.github/assets/Raspberry%20Pi%20GPIO.png" width='95%' height='95%'/>

### Check the I2C devices

- **SHT31-D**：`0x44`

```shell
pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- 44 -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

## Install Libraries

### [adafruit_sht31d.mpy](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960)

```shell
pip3 install adafruit-circuitpython-sht31d
```

### [adafruit_bus_device](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/tree/5aceeae814effae4eb950f1078c194b11401faa7#adafruit-circuitpython-busdevice)

```shell
pip3 install adafruit-circuitpython-busdevice
```

## [Using SHT31-D with Adafruit library](https://github.com/adafruit/Adafruit_CircuitPython_SHT31D/tree/main/examples)

```python
import time
import board
import adafruit_sht31d

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()
sensor = adafruit_sht31d.SHT31D(i2c)

loopcount = 0
while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    loopcount += 1
    time.sleep(2)
    # every 10 passes turn on the heater for 1 second
    if loopcount == 10:
        loopcount = 0
        sensor.heater = True
        print("Sensor Heater status =", sensor.heater)
        time.sleep(1)
        sensor.heater = False
        print("Sensor Heater status =", sensor.heater)
```

### Docs

- [`busio.I2C()`](https://circuitpython.readthedocs.io/en/latest/shared-bindings/busio/#busio.I2C)
- [`adafruit_sht31d.SHT31D()`](https://circuitpython.readthedocs.io/projects/sht31d/en/latest/api.html#adafruit_sht31d.SHT31D)
- [`temperature`](https://circuitpython.readthedocs.io/projects/sht31d/en/latest/api.html#adafruit_sht31d.SHT31D.temperature)
- [`relative_humidity`](https://circuitpython.readthedocs.io/projects/sht31d/en/latest/api.html#adafruit_sht31d.SHT31D.relative_humidity)
- [`heater`](https://circuitpython.readthedocs.io/projects/sht31d/en/latest/api.html#adafruit_sht31d.SHT31D.heater)

## Single Page Reference

- [Overview｜Adafruit SHT31-D Temperature & Humidity Sensor Breakout｜Adafruit Learning System](https://learn.adafruit.com/adafruit-sht31-d-temperature-and-humidity-sensor-breakout?view=all)
- SHT31-D 中文使用說明
