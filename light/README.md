# [Light sensor：APDS9960](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-apds9960-breakout.pdf?timestamp=1630771488)
<img src="https://github.com/5j54d93/Google-HPS/blob/main/light/photo/APDS9960.png" width='78%' height='78%'/>

- I2C interface
- gesture sensing
- RGB color sensing
- ambient light sensing
- proximity sensing：allows to measure the distance an object is from the front of the sensor（up to a few centimeters）with 8 bit resolution

## Overview

- [APDS9960 wired to Raspberry Pi with I2C](https://github.com/5j54d93/Google-HPS/tree/main/light#apds9960-wired-to-raspberry-pi-with-i2c)
  - [Raspberry Pi GPIO Pin](https://github.com/5j54d93/Google-HPS/tree/main/light#raspberry-pi-gpio-pin)
  - [Check the I2C devices](https://github.com/5j54d93/Google-HPS/tree/main/light#check-the-i2c-devices)
- [Install Libraries](https://github.com/5j54d93/Google-HPS/tree/main/light#install-libraries)
  - [adafruit_apds9960](https://github.com/5j54d93/Google-HPS/tree/main/light#adafruit_apds9960)
  - [adafruit_bus_device](https://github.com/5j54d93/Google-HPS/tree/main/light#adafruit_bus_device)
  - [adafruit_register](https://github.com/5j54d93/Google-HPS/tree/main/light#adafruit_register)
- [Using APDS9960 with Adafruit library](https://github.com/5j54d93/Google-HPS/tree/main/light#using-apds9960-with-adafruit-library)
  - [Docs](https://github.com/5j54d93/Google-HPS/tree/main/light#docs)
- [Single Page Reference](https://github.com/5j54d93/Google-HPS/tree/main/light#single-page-reference)

## [APDS9960 wired to Raspberry Pi with I2C](https://www.circuito.io/app?components=9443,12787,200000)
<img src="https://github.com/5j54d93/Google-HPS/blob/main/light/photo/APDS9960%20wired%20to%20Raspberry%20Pi%20with%20I2C.png.png" width='45%' height='45%'/>

|APDS9960|Raspberry Pi|
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

- **APDS9960**：`0x39`

```shell
pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- 39 -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

## Install Libraries

### [adafruit_apds9960](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960)

```shell
pip3 install adafruit-circuitpython-apds9960
```

### [adafruit_bus_device](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/tree/5aceeae814effae4eb950f1078c194b11401faa7)

```shell
pip3 install adafruit-circuitpython-busdevice
```

### [adafruit_register](https://github.com/adafruit/Adafruit_CircuitPython_Register)

```shell
pip3 install adafruit-circuitpython-register
```

## [Using APDS9960 with Adafruit library](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960/tree/main/examples)

```python
import time
import board
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

i2c = board.I2C()
apds = APDS9960(i2c)
apds.enable_color = True

while True:
    # create some variables to store the color data in

    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    # get the data and print the different channels
    r, g, b, c = apds.color_data
    print("red: ", r)
    print("green: ", g)
    print("blue: ", b)
    print("clear: ", c)

    print("color temp {}".format(colorutility.calculate_color_temperature(r, g, b)))
    print("light lux {}".format(colorutility.calculate_lux(r, g, b)))
    time.sleep(0.5)
```

### Docs
- [`busio.I2C()`](https://circuitpython.readthedocs.io/en/latest/shared-bindings/busio/#busio.I2C)
- [`APDS9960()`](https://circuitpython.readthedocs.io/projects/apds9960/en/latest/api.html)
- [`enable_color`](https://circuitpython.readthedocs.io/projects/apds9960/en/latest/api.html?highlight=enable_color#adafruit_apds9960.apds9960.APDS9960.enable_color)
- [`color_data_ready`](https://circuitpython.readthedocs.io/projects/apds9960/en/latest/api.html?highlight=color_data_ready#adafruit_apds9960.apds9960.APDS9960.color_data_ready)
- [`color_data`](https://circuitpython.readthedocs.io/projects/apds9960/en/latest/api.html?highlight=color_data#adafruit_apds9960.apds9960.APDS9960.color_data)
- [`calculate_color_temperature()`](https://circuitpython.readthedocs.io/projects/apds9960/en/latest/api.html?highlight=calculate_color_temperature#adafruit_apds9960.colorutility.calculate_color_temperature)
- [`calculate_lux()`](https://circuitpython.readthedocs.io/projects/apds9960/en/latest/api.html?highlight=calculate_lux#adafruit_apds9960.colorutility.calculate_lux)

## Single Page Reference

- [Overview｜Adafruit APDS9960 breakout｜Adafruit Learning System](https://learn.adafruit.com/adafruit-apds9960-breakout?view=all)
- APDS 中文使用說明
