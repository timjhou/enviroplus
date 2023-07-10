#!/usr/bin/env python3

import time
import mysql.connector
from datetime import datetime
from pms5003 import PMS5003, ReadTimeoutError
from bme280 import BME280


try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp


pms5003 = PMS5003()
time.sleep(1.0)

try:
    while True:
        temperature = round((bme280.get_temperature() * 9 / 5) + 32, 2)
        pressure = bme280.get_pressure()
        humidity = bme280.get_humidity()
        readings = pms5003.read()
        pm25 = readings.pm_ug_per_m3(2.5)
        pm10 = readings.pm_ug_per_m3(10.0)

        mydb = mysql.connector.connect(
            host="192.168.86.169",
            user="pi",
            password="badpass123",
            database="test")

        now = datetime.now()
        timenow=now.strftime('%Y-%m-%d %H:%M:%S')

        mycursor = mydb.cursor()
        sql = "INSERT INTO aqi (date, temp, humidity, pressure, pm25, pm10) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (timenow, temperature, humidity, pressure, pm25, pm10)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        print('temp is: ', temperature)

        time.sleep(5)
except KeyboardInterrupt:
    pass
