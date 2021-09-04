from adafruit_mcp3xxx.analog_in import AnalogIn
import adafruit_mcp3xxx.mcp3008 as MCP
import digitalio
import busio
import board
import time
import math
import os

class ADXL203EB:
    def __init__(self):
        self.spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        self.cs = digitalio.DigitalInOut(board.D22)
        self.mcp = MCP.MCP3008(self.spi, self.cs)
        self.chan0 = AnalogIn(self.mcp, MCP.P0)
        self.chan1 = AnalogIn(self.mcp, MCP.P1)
        self.last_read_x = 0
        self.last_read_y = 0
        self.tolerance_x = 250
        self.tolerance_y = 250
    
    def remap_range(self, value, left_min, left_max, right_min, right_max):
        left_span = left_max - left_min
        right_span = right_max - right_min
        valueScaled = int(value - left_min) / int(left_span)
        return int(right_min + (valueScaled * right_span))
    
    def X(self):
        trim_pot_changed = False
        trim_pot = self.chan0.value
        pot_adjust = abs(trim_pot - self.last_read_x)
        if pot_adjust > self.tolerance_x : trim_pot_changed = True
        if trim_pot_changed :
            set_volume = self.remap_range(trim_pot, 0, 65535, 0, 100)
            set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' \
            .format(volume = set_volume)
            os.system(set_vol_cmd)
            self.last_read_x = trim_pot
            return set_volume
        else : return self.remap_range(self.last_read_x, 0, 65535, 0, 100)
    
    def Y(self):
        trim_pot_changed = False
        trim_pot = self.chan1.value
        pot_adjust = abs(trim_pot - self.last_read_y)
        if pot_adjust > self.tolerance_y : trim_pot_changed = True
        if trim_pot_changed :
            set_volume = self.remap_range(trim_pot, 0, 65535, 0, 100)
            set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' \
            .format(volume = set_volume)
            os.system(set_vol_cmd)
            self.last_read_y = trim_pot
            return set_volume
        else : return self.remap_range(self.last_read_y, 0, 65535, 0, 100)
	
    def stable_or_sway(self):
        x = self.X()
        y = self.Y()
        if math.sqrt(x * x + y * y) > 50 : return "It's swaying！"
        else : return "It's stable now～"
