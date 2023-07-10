#!/usr/bin/env python3

import time
from bme280 import BME280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

factor = 2.25
cpu_temps = [get_cpu_temperature()] * 5

while True:
    cpu_temp = get_cpu_temperature()
    print("CPU Temp: {} *C".format(cpu_temp))
    # Smooth out with some averaging to decrease jitter
    cpu_temps = cpu_temps[1:] + [cpu_temp]
    print("cpu_temps: {}".format(cpu_temps))
    avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
    print("avg_cpu_temps: {}".format(avg_cpu_temp))
    raw_temp = bme280.get_temperature()
    print("raw temp :{}".format(raw_temp))
    comp_temp = raw_temp - ((avg_cpu_temp - raw_temp) / factor)
    print("comp_temp: {}".format(comp_temp))
    time.sleep(5.0)
