#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time

GPIO.setup('P9_14', GPIO.OUT)
GPIO.output('P9_14', GPIO.HIGH)
#GPIO.output('P9_14', GPIO.LOW)
GPIO.cleanup()
time.sleep(0.5)
ADC.setup()
f = open('data.txt', 'a')
x = 1
while True:
    value = ADC.read("P9_38")
    print(value)
    f.write(str(round(x, 1)) + ' ' + str(value) + '\n')
    f.flush()
    x += 3
    time.sleep(0.2)
    