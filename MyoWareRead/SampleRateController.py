import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn
import SampleCollector as SC
import _thread

SAMPLES = 1000

data = [None] * SAMPLES

try:
    _thread.start_new_thread(SC.GetSamples())
except:
    print("Error")


time.sleep(2)
start = time.monotonic()

# Read the same channel over and over
for i in range(SAMPLES):
    data[i] = SC.GetOneSample()
    time.sleep(0.001)
    #print(str(chan0.value))

end = time.monotonic()
total_time = end - start

print("Time of capture: {}s".format(total_time))
print("Actual={}".format(SAMPLES / total_time))
