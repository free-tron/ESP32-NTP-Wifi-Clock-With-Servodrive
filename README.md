# ESP32-NTP-Wifi-Clock-With-StepperDrive
ESP32 NTP Wifi Clock With Servodrive

ESP32 (ESP32S WROOM-32) running MicroPython Wifi Clock that synchronizes the interal RTC via wifi connection to the NTP pool.
End goal is to have the internal RTC then interrupt the running code to instruct the multiple stepper motor drive system to move the clock hands about the clock face.

Homing for each motor will be achieved by either microswitches, brass pins or other metal contact contrivance.

Homing will be achieved by either ESP32 h4x or by the stepper motor driver IC.

Stepper motor control will be in either step and dir mode or uart depending on available pins.

Whilst a seperate display would be useful it will detract from the otherwise *timeless* look of the device. 
  It's *supposed* to look really old but with up-to-date functions such as convenience (no need to set the time) and accuracy.

Case would look good in either high quality ply with layers exposed or English hardwood, beech, ash, birch, oak etc.
  A dark stain is preferable though by no means necessary.
Good quality lacquer or compounded varnish finish is a must to prevent dust sticking.

Accent stripe could be brass, fruit, teak, lignum vitae, ebony, purpleheart or rosewood inlays.

Stepper motors are to be the 1.8 degree 200 step variety.

This is currently in early development and the motor drive hardware has not yet been assembled for testing. Live tests on the ESP32 are common however. 
Non functional ESP32 compatible MicroPython code will NOT be pushed into the dev stream. It has to function.

<strike>Code2.py exists because of a watchdog issue, bouncing in and out of files is a dirty way to prevent continous reboots by the ESP32.
  If the watchdog has a fit in this code it means a reflash is necessary as reading and writing to the ESP32 is extremely unstable otherwise.</strike>

Licensed GNU-GPLV3.
