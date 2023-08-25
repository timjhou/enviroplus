#!/usr/bin/env python3

import time
import mysql.connector
import datetime
from pms5003 import PMS5003, ReadTimeoutError
from bme280 import BME280


try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

pms5003 = PMS5003()


def dateTime(): #return datestamp as a string
    currenttime = datetime.datetime.now()
    now = currenttime.strftime('%Y-%m-%d %H:%M:%S')
    return now

def getTemp(): #get temp
    temperature = round((bme280.get_temperature() * 9 / 5) + 32, 2)
    return temperature

def getPressure(): #return pressure
    pressure = bme280.get_pressure()
    return pressure

def getHumidity(): #return humidity
    humidity = bme280.get_humidity()
    return humidity


try:
    while True:
        temperature = round((bme280.get_temperature() * 9 / 5) + 32, 2)
        pressure = bme280.get_pressure()
        humidity = bme280.get_humidity()        
        readings = pms5003.read()
        pm25 = readings.pm_ug_per_m3(2.5)
        pm10 = readings.pm_ug_per_m3(10.0)

        mydb = mysql.connector.connect(
            host="localhost",
            user="Timmy",
            password="password",
            database="aqi")

        timenow=dateTime()

        mycursor = mydb.cursor()
        sql = "INSERT INTO sensor (datetime, temperature, pressure, humidity) VALUES (%s, %s, %s, %s)"
        val = (timenow, temperature, pressure, humidity)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        print('temp is: ', temperature)
        time.sleep(5)

except KeyboardInterrupt:
    pass

