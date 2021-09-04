# Google Hardware Product Sprint－2021 APAC TW HPS

![GitHub](https://img.shields.io/github/license/5j54d93/Google-HPS)
![GitHub contributors](https://img.shields.io/github/contributors/darrenyaoyao/GoogleHPS)
![GitHub repo size](https://img.shields.io/github/repo-size/5j54d93/Google-HPS)
![GitHub followers](https://img.shields.io/github/followers/5j54d93)
![GitHub Repo stars](https://img.shields.io/github/stars/5j54d93/Google-HPS)
![GitHub watchers](https://img.shields.io/github/watchers/5j54d93/Google-HPS)

Using Raspberry Pi 3 Model B+ to help us auto watering plants, and if there are birds aproaching, buzzer will noise to scare them away！We also have a dashboard（web）to view all related data which could auto switching between Day theme and Nithgt theme！And you could also remote control Raspberry Pi to watering or noising by clicking the button on website if you want！

<img src="https://github.com/5j54d93/Google-HPS/blob/main/photo/Product.png" width='100%' height='100%'/>

- **Contibuters：[Ricky](https://github.com/5j54d93)、[Darren](https://github.com/darrenyaoyao)、[Zona](https://github.com/zona8815)、[Amy](https://github.com/AmyCHANGY)、[Andrew](https://github.com/TingWeiWong)**
- **Origin repository**：Improving from [here](https://github.com/darrenyaoyao/GoogleHPS)！
- **PDF of our project slides**：[here](https://www.linkedin.com/in/5j54d93/detail/treasury/position:1818345962/?entityUrn=urn%3Ali%3Afsd_profileTreasuryMedia%3A(ACoAAC6VbdQBQobxRd1rOO_UKJMpmq7spKspF2E%2C1635468225149)&parentEntityUrn=urn%3Ali%3Afsd_profilePosition%3A(ACoAAC6VbdQBQobxRd1rOO_UKJMpmq7spKspF2E%2C1818345962)&section=position%3A1818345962&treasuryCount=2)
- **Project name**：Demeter
- **Mentor**：Weihsuan
- **Team**：2

## Wiring to Raspberry Pi

- [**［I2C］Air Quality**：SGP30]()
- **［SPI］Acceleration**：ADXL203EB
- **［I2C］Light**：APDS9960
- **［I2C］Temperature & Humidity**：SHT31-D

### Check the I2C devices：

- **SGP30**：`0x58`
- **APDS9960**：`0x39`
- **SHT31-D**：`0x44`

```
pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- 39 -- -- -- -- -- --
40: -- -- -- -- 44 -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- 58 -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

### Check the SPI devices：

- **Raspberry Pi** -> **MCP3008** -> **ADXL203EB**

```
pi@raspberrypi:~ $ ls -l /dev/spidev*
crw-rw---- 1 root spi 153, 0 Aug 28 13:17 /dev/spidev0.0
crw-rw---- 1 root spi 153, 1 Aug 28 13:17 /dev/spidev0.1
```

## Install Libraries on Raspberry Pi

```
sudo pip3 install -r requirements.txt
```

## Run Web Server on Raspberry Pi

```
sudo python3 Demeter.py
```

## Open the Website

You could open it on computer, iPhone, iPad ......, as long as your device has a browser.

- **URL：`http://[your ip]`**
- use `ifconfig` to check your ip
- replace `[your ip]` to something like `192.xxx.x.xx` or `192.xxx.x.xxx`

### Screenshot with Day theme and Nithgt theme（Automatic switching）

<img src="https://github.com/5j54d93/Google-HPS/blob/main/photo/Screenshot.png" width='100%' height='100%'/>
