# data and time format as described : Sun May 29 02:26:23 IST 2018

from datetime import datetime

now = datetime.now()

day = now.strftime("%A")
short_day = day[0:3]

month = now.strftime("%B")
short_month = month[0:3]

date = now.strftime("%d")
time = now.strftime("%I:%M:%S %p")

year = now.strftime("%Y")

print(short_day, short_month, date, time, "IST", year)
