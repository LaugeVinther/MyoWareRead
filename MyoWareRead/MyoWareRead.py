import time
import os
from time import sleep
from datetime import datetime
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import keyboard

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

ads.data_rate = 3300
ads.mode = Mode.CONTINUOUS


##åben bil
f = open("/mnt/mydisk/1.txt", "a") 


try:
    while True:
        f.write(str(chan0.value) + ";" + str(chan1.voltage) + ";" + str(chan2.voltage) + ";" + str(chan3.voltage) + "\n\r")
except KeyboardInterrupt:
    pass

f.flush()
f.close() 
print("Jeg nåede herned")
