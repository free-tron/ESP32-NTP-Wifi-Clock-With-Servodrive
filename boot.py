import esp
esp.osdebug(None)
import esp32
import machine
import time

print("Booting")
print()
print("Current core frequency:",machine.freq(),"hz") # get the current frequency of the CPU
print("Default: 160Mhz")
#machine.freq(160000000) # set the CPU frequency to 160 Mhz -- (default)
#machine.freq(240000000) # set the CPU frequency to 240 MHz -- (max)
print()

pass
execfile('code2.py')
