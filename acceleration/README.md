# [G sensor：ADXL203EB](http://www.farnell.com/datasheets/1793797.pdf)
<img src="https://github.com/5j54d93/Google-HPS/blob/main/acceleration/photo/ADXL203EB.png" width='30%' height='30%'/><img src="https://github.com/5j54d93/Google-HPS/blob/main/acceleration/photo/MCP3008.png" width='40%' height='40%'/>

- SPI interface
- High accuracy, 2-axis tilt sensing
- Abuse event detection

## Overview

- [ADXL203EB wired to Raspberry Pi with I2C](https://github.com/5j54d93/Google-HPS/tree/main/acceleration#adxl203eb-wired-to-raspberry-pi-with-spi)
  - [Raspberry Pi GPIO Pin](https://github.com/5j54d93/Google-HPS/tree/main/acceleration#raspberry-pi-gpio-pin)
  - [Check the SPI devices](https://github.com/5j54d93/Google-HPS/tree/main/acceleration#check-the-spi-devices)
- [Install Libraries](https://github.com/5j54d93/Google-HPS/tree/main/acceleration#install-libraries)
  - [adafruit-blinka](https://github.com/5j54d93/Google-HPS/tree/main/acceleration#adafruit-blinka)
  - [mcp3008](https://github.com/5j54d93/Google-HPS/tree/main/acceleration#mcp3008)
- [Using ADXL203EB and MCP3008 with Adafruit library](https://github.com/5j54d93/Google-HPS/tree/main/acceleration#using-adxl203eb-and-mcp3008-with-adafruit-library)
  - [Docs](https://github.com/5j54d93/Google-HPS/tree/main/acceleration#docs)
- [Single Page Reference](https://github.com/5j54d93/Google-HPS/tree/main/acceleration#single-page-reference)

## [ADXL203EB wired to Raspberry Pi with SPI](https://www.circuito.io/app?components=9269,9443,200000)

Because ADXL203EB is an analog input for Raspberry Pi, we should use MCP3008 to connect between ADXL203EB and Raspberry Pi with SPI！

<img src="https://github.com/5j54d93/Google-HPS/blob/main/acceleration/photo/ADXL203EB%20wired%20to%20Raspberry%20Pi%20with%20SPI.png" width='45%' height='45%'/><img src="https://github.com/5j54d93/Google-HPS/blob/main/acceleration/photo/MCP3008%20Pinout.png" width='55%' height='55%'/>

|ADXL203EB|MCP3008|Raspberry Pi|
|:-:|:-:|:-:|
||VDD|3.3V|
||VREF|3.3V|
||AGND|GND|
||CLK|SCLK|
||DOUT|MISO|
||DIN|MOSI|
||CS|GPIO #22|
||DGND|GND|
|ST||3.3V|
|X|CH0||
|Y|CH1||
|G||GND|

### Raspberry Pi GPIO Pin
- **3V3**：1、17
- **GND**：6、9、14、20、25、30、34、39
- **SCLK**：23
- **MISO**：21
- **MOSI**：19
- **GPIO #22**：15

<img src="https://github.com/5j54d93/Google-HPS/blob/main/photo/Raspberry%20Pi%20GPIO.png" width='95%' height='95%'/>

### Check the SPI devices

```shell
pi@raspberrypi:~ $ ls -l /dev/spidev*
crw-rw---- 1 root spi 153, 0 Aug 28 13:17 /dev/spidev0.0
crw-rw---- 1 root spi 153, 1 Aug 28 13:17 /dev/spidev0.1
```

## Install Libraries

### [adafruit-blinka](https://github.com/adafruit/Adafruit_Blinka#installing-from-pypi)

```shell
pip3 install adafruit-blinka
```

### [mcp3008](https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx#installing-from-pypi)

```shell
pip3 install adafruit-circuitpython-mcp3xxx
```

## [Using ADXL203EB and MCP3008 with Adafruit library](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Analog_Inputs_for_Raspberry_Pi_Using_the_MCP3008/code.py)

```python
import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)

print('Raw ADC Value: ', chan0.value)
print('ADC Voltage: ' + str(chan0.voltage) + 'V')

last_read = 0       # this keeps track of the last potentiometer value
tolerance = 250     # to keep from being jittery we'll only change
                    # volume when the pot has moved a significant amount
                    # on a 16-bit ADC

def remap_range(value, left_min, left_max, right_min, right_max):
    # this remaps a value from original (left) range to new (right) range
    # Figure out how 'wide' each range is
    left_span = left_max - left_min
    right_span = right_max - right_min

    # Convert the left range into a 0-1 range (int)
    valueScaled = int(value - left_min) / int(left_span)

    # Convert the 0-1 range into a value in the right range.
    return int(right_min + (valueScaled * right_span))

while True:
    # we'll assume that the pot didn't move
    trim_pot_changed = False

    # read the analog pin
    trim_pot = chan0.value

    # how much has it changed since the last read?
    pot_adjust = abs(trim_pot - last_read)

    if pot_adjust > tolerance:
        trim_pot_changed = True

    if trim_pot_changed:
        # convert 16bit adc0 (0-65535) trim pot read into 0-100 volume level
        set_volume = remap_range(trim_pot, 0, 65535, 0, 100)

        # set OS volume playback volume
        print('Volume = {volume}%' .format(volume = set_volume))
        set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' \
        .format(volume = set_volume)
        os.system(set_vol_cmd)

        # save the potentiometer reading for the next loop
        last_read = trim_pot

    # hang out and do nothing for a half second
    time.sleep(0.5)
```

### Docs
- [`busio.SPI()`](https://circuitpython.readthedocs.io/en/latest/shared-bindings/busio/#busio.SPI)
- [`digitalio.DigitalInOut()`](https://circuitpython.readthedocs.io/en/latest/shared-bindings/digitalio/index.html#digitalio.DigitalInOut)
- [`MCP.MCP3008()`](https://circuitpython.readthedocs.io/projects/mcp3xxx/en/latest/api.html#adafruit_mcp3xxx.mcp3008.MCP3008)
- [`AnalogIn()`](https://circuitpython.readthedocs.io/projects/mcp3xxx/en/latest/api.html#adafruit_mcp3xxx.analog_in.AnalogIn)
- [`value`](https://circuitpython.readthedocs.io/projects/mcp3xxx/en/latest/api.html#adafruit_mcp3xxx.analog_in.AnalogIn.value)
- [`voltage`](https://circuitpython.readthedocs.io/projects/mcp3xxx/en/latest/api.html?highlight=MCP3008#adafruit_mcp3xxx.analog_in.AnalogIn.voltage)

## Single Page Reference

- [Overview｜Analog Inputs for Raspberry Pi Using the MCP3008｜Adafruit Learning System](https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi?view=all#script)
- ADXL203EB 和 MCP3008 中文使用說明
