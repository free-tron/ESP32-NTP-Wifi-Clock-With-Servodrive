# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
#import webrepl
#webrepl.start()
import esp32
import machine
import utime
import time
import os

onboardled = machine.Pin(2, machine.Pin.OUT)

onboardled.value(0)
print("")
print("----------------------------------------")
print("Running boot.py")
print("----------------------------------------")
print()
print("Current core frequency:",machine.freq(),"hz") # get the current frequency of the CPU
print("Default: 160Mhz")
#machine.freq(160000000) # set the CPU frequency to 160 Mhz -- (default)
#machine.freq(240000000) # set the CPU frequency to 240 MHz -- (max)
print()
# define a function to convert the raw temperature value
# returned by esp32.raw_temperature() to celsius degrees
def celsius(raw):
        return (raw - 32) / 1.8
# read the raw temperature value using esp32.raw_temperature()
raw_value = esp32.raw_temperature()
# convert the raw temperature value to celsius degrees
temperature = celsius(raw_value)
# print the temperature value
print('CPU Temperature(Both Cores): {:.2f} deg C'.format(temperature))
print()

print("Connecting to wifi")

try:
    def connect():
        import network
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            sta_if.active(True)
            sta_if.connect('SSID', 'KEY')
            while not sta_if.isconnected():
                pass # wait till connection
        print("WiFi Connected")
        print()
        print("ESP32-IP | SUBNET | GATEWAY | DNS/DHCP")
        print(sta_if.ifconfig())
        
    connect()
    print()
    print("Done booting, WiFi Connected 8-D")
    onboardled.value(1)
except:
    print()
    print("Done booting, WiFi NOT Connected 8-(")
    onboardled.value(1)
    time.sleep(0.125)
    onboardled.value(0)
    time.sleep(0.125)
    onboardled.value(1)
    time.sleep(0.125)
    onboardled.value(0)  
pass
execfile("code.py")
