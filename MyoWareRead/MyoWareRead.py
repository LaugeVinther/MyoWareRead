import time
import os
from time import sleep
from datetime import datetime
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import keyboard

SAMPLES = 1000

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)


##csv
#f = open("/mnt/mydisk/1_no_noise.csv", "a") 


try:
    while True:
        print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
        #f.write(str(chan.value) + ";" + str(chan.voltage) + "\n")
        #time.sleep(0.01)
except KeyboardInterrupt:
    pass

#f.flush()
#f.close() 
print("Jeg nåede herned")
