import time
import datetime

today = datetime.date.today()
now = datetime.datetime.today()
print(today)
print(now.hour)
#setting variable for today and now

day = today.weekday()
#0 Monday 6 Sunday
print(day)

day = today.isoweekday()
#1 Monday 7 Sunday
print(day)

timedelta = datetime.timedelta(days=7)
print(today + timedelta)
#will print out what day it is in 7 days

bday = datetime.date(2022, 1, 14)
tillbday = bday - today
print(tillbday)
print(tillbday.total_seconds())
#will print out days till my birthday

while datetime.datetime.today().second > 0:
    print(60 - datetime.datetime.today().second)
    time.sleep(1)
#will print out the amount of seconds left in a minute

start = datetime.time()
#Code
end = datetime.time()
print(end - start)