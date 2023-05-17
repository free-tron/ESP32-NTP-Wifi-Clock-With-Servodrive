import os
import math
import time
import re
import utime
import esp32
import machine

onboardled = machine.Pin(2, machine.Pin.OUT)

print("running OK")
onboardled.on()
time.sleep(0.25)
onboardled.off()
time.sleep(0.25)
onboardled.on()
time.sleep(0.25)
onboardled.off()
execfile("code.py")
