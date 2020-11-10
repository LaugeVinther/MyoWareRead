import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn

# Data collection setup
RATE = 3300
SAMPLES = 1000

# Create the I2C bus with a fast frequency
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

ads.mode = Mode.CONTINUOUS
ads.data_rate = RATE

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)

data_array = []

def GetSamples():
    while true:
        data_array.append(chan0.voltage)

def GetOneSample():
    return data_array[-1]

def ClearSamples():
    data_array.clear()