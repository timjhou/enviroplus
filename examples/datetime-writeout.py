import datetime
import csv
import time

def dateTime(): #return datestamp as a string
    currenttime = datetime.datetime.now()
    now = currenttime.strftime('%Y-%m-%d %H:%M:%S')
    return now

# Write the result to a txt file
try:
    while True:
        with open("writeoutput.txt", "a") as file:
            file.write(dateTime())
            file.write('\n')
            print(dateTime())
            time.sleep(1)
except KeyboardInterrupt:
    pass