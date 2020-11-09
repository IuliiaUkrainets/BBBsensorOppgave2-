import time, re
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC


def read_sensor(path):
  value = "U"
  try:
    f = open(path, "r")
    line = f.readline()
    if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
      line = f.readline()
      m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
      if m:
        value = str(float(m.group(2)) / 1000.0)
    f.close()
  except IOError:
    print(time.strftime("%x %X"), "Error reading", path)
  return value

# define pathes to 1-wire sensor data
pathes = (
  "/sys/bus/w1/devices/28-0000053853f7/w1_slave",
)



GPIO.setup('P9_14', GPIO.OUT)
GPIO.output('P9_14', GPIO.HIGH)
#GPIO.output('P9_14', GPIO.LOW)
GPIO.cleanup()
time.sleep(0.5)
ADC.setup()

f1 = open('data.txt', 'a')
f2 = open('temperature.txt', 'a')

x = 1
while True:
    value = ADC.read("P9_38")
    print(value)
    f1.write(str(round(x, 1)) + ' ' + str(value) + '\n')
    f1.flush()
    if(x % 4 == 0):
        for path in pathes:
          data = read_sensor(path)
          print(data)
          f2.write(str(x*1.5)+' '+str(round(float(data), 1))+'\n')
          f2.flush()
    x += 3
    time.sleep(0.2)
    
