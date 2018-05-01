#!/usr/bin/python
from max31855 import MAX31855, MAX31855Error
from time import sleep

cs_pin = 18            #15
clock_pin = 16         #29
data_pin = 15          #31
units = "f"
thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units)
running = True
while(running):
    try:
        try:
            tc = thermocouple.get()
        except MAX31855Error as e:
            tc = "Error: " + e.value
        print("Temperature: " + str(tc))
        sleep(1.0)
    except KeyboardInterrupt:
        running = False
thermocouple.cleanup()
