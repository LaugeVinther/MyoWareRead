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

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

ads.data_rate = 3300
ads.mode = Mode.CONTINUOUS


##åben fil
f = open("/mnt/mydisk/1.txt", "a") 

data0 = []
data1 = []
data2 = []
data3 = []

try:
    while True:
        data0.append(chan0.voltage)
        data1.append(chan1.voltage)
        data2.append(chan2.voltage)
        data3.append(chan3.voltage)
        #f.write(str(chan0.voltage) + ";" + str(chan1.voltage) + ";" + str(chan2.voltage) + ";" + str(chan3.voltage) + "\n\r")
except KeyboardInterrupt:
    pass

print("Gemmer array til fil...")

for i in range(len(data0)):
    f.write(str(data0[i]) + ";" + str(data1[i]) + ";" + str(data2[i]) + ";" + str(data3[i]) + "\n\r")
    

f.flush()
f.close() 

print("\nJeg er færdig!")
