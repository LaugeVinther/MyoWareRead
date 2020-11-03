import time
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
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

#csv
file = open("/media/usb/data_log.csv", "a") 

if os.stat("/home/pi/data_log.csv").st_size == 0: 
    file.write("{:>5}\t{:>5}".format("raw", "v\n"))

print("{:>5}\t{:>5}".format("raw", "v"))


while True:
    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    file.write("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage)+"\n")

    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('s'):  # if key 's' is pressed 
            print('******Stopped data collecting*******')
            break  # finishing the loop
    except:
        break
    
file.flush()
file.close() 
