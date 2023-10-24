import calendar

# print(calendar.month(2023, 10, w=3, l=1))
# print(calendar.calendar(2023, w=0, l=0, c=30, m=5))

# print(calendar.weekday(2023, 10, 24))

# print(calendar.isleap(2024))
#
# print(calendar.leapdays(2000, 2021))

# print(calendar.HTMLCalendar().formatyear(2023))

# import time
#
# start = time.time()
# # time.sleep(5)
#
# print(time.asctime())
# print(time.gmtime())
# print(time.localtime()[7])
#
# stop = time.time()
#
# print(stop - start)

import datetime

# d = datetime.date(1988, 3, 16)
# print(d)
# print(type(d))

# today = datetime.date.today()
# print(today)
#
# # print(d - today)
#
# print(today.weekday())
# print(today.isoweekday())
# print(today.year)
# print(today.month)
# print(today.day)
#
# print(type(today - d))
# print(today - d)

# date1 - date2 = timedelta
# date1 -/+ timedelta = date2

# tdelta = datetime.timedelta(days=7, minutes=2881, seconds=12056)
# print(tdelta)
# print(type(tdelta))
# print(today - tdelta)

# next_birthday = datetime.date(2024, 3, 16)
# until_birthday = next_birthday - today

# t = datetime.time(13, 24, 43, 123)
# print(t.microsecond)
# print(type(t))

# dt = datetime.datetime(2023, 10, 24, 17, 23, 45)
# print(dt.date())
# print(dt.time())
# tdelta = datetime.timedelta(days=5, hours=12, minutes=37)

# print((dt - tdelta).time())

# today = datetime.datetime.now()
# print(today)
#
# ts = 574525800
# ts_date = datetime.date.fromtimestamp(ts)
# ts_datetime = datetime.datetime.fromtimestamp(ts)
# print(ts_datetime)
#
# today_ts = today.timestamp()
# # today_ts = datetime.datetime.timestamp(today)
# print(today_ts)


today = datetime.datetime.today()
today_str = today.strftime('%A, %d. %B %Y, %Y, %Y')
print(today_str)

# date_str = '24.10.23 20:20:15'
# d = datetime.datetime.strptime(date_str, '%d.%m.%y %H:%M:%S')

date_str = 'Июнь 23, 2023'
date_str = date_str.replace('Июнь', 'June')
d = datetime.datetime.strptime(date_str, '%B %d, %Y')

print(d)
print(type(d))