import os
import math
import time
import re
import utime
import esp32
import machine
import ntptime

timeupdates = int(0)
updatesperminute = int(0)
updatesperhour = int(0)
bongcount = 0
#watchdog timer import & settings
from machine import WDT
wdt = WDT(timeout = 25000)
wdt.feed() 

onboardled = machine.Pin(2, machine.Pin.OUT)
bongpin = machine.Pin(4, machine.Pin.OUT)
bongvisual = machine.Pin(12, machine.Pin.OUT)
updatepin = machine.Pin(13, machine.Pin.OUT)
synchpin = machine.Pin(15, machine.Pin.OUT)
smokepin = machine.Pin(17, machine.Pin.OUT)

print()
print("----------------------------------------")
print("Running code.py")
print("----------------------------------------")
print()

while True:

# define a function to convert the raw temperature value
# returned by esp32.raw_temperature() to celsius degrees
    def celsius(raw):
        return (raw - 32) / 1.8
# read the raw temperature value using esp32.raw_temperature()
    raw_value = esp32.raw_temperature()
# convert the raw temperature value to celsius degrees
    temperature = celsius(raw_value)
# print the temperature value
    #print('CPU Temperature(Both Cores): {:.2f} deg C'.format(temperature))

    #print()
    #print("RAW Machine Time (RTC) Before Synchronisation:",time.localtime())

#anti-ban sleep
    #print()
    #print("Waiting 15secs for anti-ban connection...")
    wdt.feed()
    pass
    wdt.feed()
    #print()

    #print("Adjusted timezone offset (UTC -0hr) for GMT")
    UTC_OFFSET = 1 * 60 * 60   # change the first digit ('0') according to your timezone -1 or possibly 0 =GMT
    actual_time = time.localtime(time.time() + UTC_OFFSET)
    txt = (actual_time)
    txt2 = str(txt)

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

    wdt.feed()
    #print()
    #print("Actual time data RECEIVED:",actual_time)
    #print()
    #rint("Machine RTC Time After Synchronisation:",time.localtime())
    #print("Format of incoming data tuple is: (year, month, month-day, hour, min, second, weekday, year-day)")
    #print()
    print("Year:",year)
    print("Month:",month)
    print("MonthDay:",day)
    print("Hour:",hour)
    print("Minutes:",minute)
    print("Second:",second)
    print("Weekday:",weekday)
    print("Yearday",yearday)

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
    wdt.feed()

    print()
    print("----------------------------------------")
    print(weekday,day,month,year,",",hour,":",minute,":",second,"GMT")
    print("----------------------------------------")
    
    if month == "January" and year == "2000":
        print("NTP & OB-RTC NOT YET SYNCHRONIZED")
        pass
    else:
        print()
        print("NTC TIME UPDATED AND ACCURATE")
        synchpin.value(1)
        print("Update Count: ",timeupdates)
    pass
    print()
    
    time.sleep(0.5)
    
    if second > "0" and second < "35" and minute < "52" and updatesperminute < 1 and updatesperhour < 1:
        try:
            wdt.feed()
            print("    UPDATING...")
            updatepin.value(1)
            time.sleep(15)
            ntptime.settime()
            timeupdates+=1
            updatesperminute+=1
            updatesperhour+=1
            updatepin.value(0)
        except:
            print("Failed retrieving NTP TimeData. Wifi? IP/MAC Ban? PSU Brownout? Check for proper power and decoupling capacitor, then credentials; else reboot this ESP32.")
            print()
            onboardled.value(0)
            updatepin.value(1)
            time.sleep(0.2)
            updatepin.value(0)
            time.sleep(0.2)
            updatepin.value(1)
            time.sleep(0.2)
            updatepin.value(0)
            time.sleep(0.2)
            updatepin.value(1)
            time.sleep(0.2)
            updatepin.value(0)
            time.sleep(0.2)
            updatepin.value(1)
            time.sleep(0.2)
            updatepin.value(0)
        pass    
    onboardled.value(1)
    
    if second == "0":
        wdt.feed()
        updatesperminute=0
    pass
    
    if minute == "59" and second == "0":
        wdt.feed()
        updatesperhour=0
    pass

    #420light
    if hour == "4" and minute == "20" or hour == "16" and minute == "20":
        wdt.feed()
        smokepin.value(1)
        print("BONGHIT!")
    else:
        smokepin.value(0)
    pass
   
    #if hour == "8" and minute == "0" and second == "0":
    #if second == "0" or second == "15" or second == "30" or second == "45":
    #    bongpin.value(1)
    #    bongvisual.value(1)
    #    time.sleep(0.2)
    #    bongpin.value(0)
    #    bongvisual.value(0)
    #    print("BONGHIT!")
    #    pass
    
    minute = int(minute)
    hour = int(hour)
    second = int(second)
        
    if minute < 1 and second < 1:
        wdt.feed()
        bongvisual
        bongvisual.value(1)
    else:
        bongvisual.value(0)
        pass
    
    #BONGHIT
    if hour > 7 and hour < 21 and minute < 1 and second < 1:
        wdt.feed()
        bongcount = hour
        bongcount = int(bongcount)
        print("bongcount: ",bongcount)
        time.sleep(1)
    pass

    if bongcount > 12:
        wdt.feed()
        bongcount -= 12
        print("bongcount: ",bongcount)
        time.sleep(1)
    pass

    while bongcount > 0:
        wdt.feed()
        bongpin.value(1)
        time.sleep(0.2)
        bongpin.value(0)
        time.sleep(1.8)
        bongcount -= 1
    pass
    wdt.feed()
