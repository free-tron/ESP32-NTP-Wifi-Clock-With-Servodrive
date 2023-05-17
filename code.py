import os
import math
import time
import re
import utime
import esp32
import machine

try:
    def connect():
        import network
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            sta_if.active(True)
            sta_if.connect('TriOptimum', '17980A148051')
            while not sta_if.isconnected():
                pass # wait till connection
        print("WiFi Connected")
        print()
        print("ESP32-IP | SUBNET | GATEWAY | DNS/DHCP")
        print(sta_if.ifconfig())
        
    connect()
    print()
    print("WiFi Connected 8-D")
    onboardled.on()
except:
    print()
    print("WiFi NOT Connected 8-(")
pass

while True:

    print()
    print("Machine RTC Before Synchronisation:",time.localtime())

#anti-ban sleep
    print()
    print("Waiting 15secs for anti-ban connection...")
    time.sleep(15)
    print()

    try:
        import ntptime
    except:
        print("Failed retrieving NTP TimeData. Wifi OK? IP Banned? Undervoltage brownout? Check proper power, then credentials and/or reboot this ESP32.")
    pass    

    print("Adjusted timezone offset (UTC -0hr) for GMT")
    UTC_OFFSET = 0 * 60 * 60   # change the '-1' according to your timezone -1=GMT
    actual_time = time.localtime(time.time() + UTC_OFFSET)

#blink led to indicate update.
    onboardled.off()
    time.sleep(0.5)
    onboardled.on()
    
    txt = (actual_time)
    txt2 = str(txt)

##(2000, 1, 1, 0, 4, 10, 5, 1) # yours will be different
##The format of this tuple is (year, month, month-day, hour, min, second, weekday, year-day)

#original format

    txtproc1 = txt2.replace("(","")
    txtproc2 = txtproc1.replace(")","")
    txtproc3 = txtproc2.replace(","," ")
    txtproc4 = txtproc3.replace(" ","-----")

##debug
##print(txtproc1)
##print(txtproc2)
##print(txtproc3)
##print()
##print(txtproc4)

    year = txtproc4[0:8].replace("-","")
    month = txtproc4[10:17].replace("-","")
    monthproc = month
    monthlookup = int(txtproc4[10:17].replace("-",""))
    day = txtproc4[18:32].replace("-","")
    dayproc = day
    daylookup = day
    hour = txtproc4[35:42].replace("-","")
    minute = txtproc4[46:54].replace("-","")
    second = txtproc4[58:65].replace("-","")
    weekday = txtproc4[70:76].replace("-","")
    yearday = txtproc4[80:90].replace("-","")

    print()
    print("NTP TIME UPDATED")
    print()
    print("Actual NTP time data RECEIVED:",actual_time)
    print()
    print("Machine RTC After Synchronisation:",time.localtime())
    print()
    print("Format of incoming data tuple is: (year, month, month-day, hour, min, second, weekday, year-day)")
    print()
    print("year:",year)
    print("month:",month)
    print("monthday:",day)
    print("hour:",hour)
    print("minutes:",minute)
    print("second:",second)
    print("weekday:",weekday)
    print("yearday",yearday)

#calculate written month
    if month.replace(" ","") == "1":
            month = "January"
    elif month.replace(" ","") == "2":
       month = "February"
    if month.replace(" ","") == "3":
            month = "March"
    elif month.replace(" ","") == "4":
       month = "April"
    if month.replace(" ","") == "5":
            month = "May"
    elif month.replace(" ","") == "6":
       month = "June"
    if month.replace(" ","") == "7":
            month = "July"
    elif month.replace(" ","") == "8":
       month = "August"
    if month.replace(" ","") == "9":
            month = "September"
    elif month.replace(" ","") == "10":
       month = "October"
    if month.replace(" ","") == "11":
            month = "November"
    elif month.replace(" ","") == "12":
       month = "December"
    pass
    print("Month:",month)

#calculate written day
    if weekday.replace(" ","") == "0":
            weekday = "Monday"
    elif weekday.replace(" ","") == "1":
       weekday = "Tuesday"
    if weekday.replace(" ","") == "2":
            weekday = "Wednesday"
    elif weekday.replace(" ","") == "3":
       weekday = "Thursday"
    if weekday.replace(" ","") == "4":
            weekday = "Friday"
    elif weekday.replace(" ","") == "5":
       weekday = "Saturday"
    if weekday.replace(" ","") == "6":
            weekday = "Sunday"
    pass
    print("Weekday:",weekday)
    print()
    print("Time NOW:",weekday,day,month,year,",",hour,":",minute,":",second,"GMT")
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
    execfile("code2.py")
