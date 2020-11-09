

import time, re

# function: read and parse sensor data file
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

f = open('temperature.txt', 'a')
# read sensor data
x = 1
while True:
    for path in pathes:
      data = read_sensor(path)
      print(data)
      f.write(str(x)+' '+data+'\n')
      f.flush()
      x += 1
      time.sleep(2)
      