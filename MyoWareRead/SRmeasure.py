
import time
import os
from time import sleep
from datetime import datetime
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import Mode
import keyboard

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

RATE = 

ads.mode = Mode.CONTINUOUS
ads.data_rate = RATE

# Create single-ended inputs
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

SAMPLES = 1000
data = [None] * SAMPLES

start = time.monotonic()

#print("1000 samples med brug af 'data.append(chan0.voltage)'")
# Read the same channel over and over
for i in range(SAMPLES):
    data.append(chan0.voltage)
    #data[i] = chan0.voltage
    #time.sleep(0.001)
    #print(str(chan0.value))

end = time.monotonic()
total_time = end - start

print("Ønsket samplerate: " + str(RATE))
print("Tid: {}s".format(total_time))
print("Aktuel samplerate: {}".format(SAMPLES / total_time))

