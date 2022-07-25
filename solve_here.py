from datetime import date, datetime
import calendar


d0 = date(2017, 8, 18)
d1 = date(2017, 10, 26)
delta = d1 - d0
# print(delta.days)

#  formats the input into something that can be used in dateTime
def get_month(d1):
    m1 = list(calendar.month_abbr).index(d1[2])
    return(m1)


#  find the amount of days in between the two given times 
#  intput = d1:day1, d2:day2
#  return =  difference in days
def day_delta(d1, d2):


    d1 = d1.split()
    d2 = d2.split()
    print(type(get_month(d1)))

    df = date(int(d1[3]),get_month(d1), int(d1[1]))
    di = date(int(d2[3]),get_month(d2), int(d2[1]))

    delta_days = abs(df - di)
    return(delta_days)

#  input= t1:timestamp, t2:timestamp
#  output= time difference between timestamps t1-t2 (in seconds)
def hour_delta(h1, h2):
    h1 = h1.split()
    h2 = h2.split()
    t1 = datetime.strptime(h1[4], "%H:%M:%S")
    t2 = datetime.strptime(h2[4], "%H:%M:%S")


    delta_time = t1-t2
    print(delta.total_seconds())


# print(get_month("Sun 10 May 2015 13:54:36 -0700"))


# print(day_delta("Sun 12 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 0000"))

hour_delta("Sun 12 May 2015 14:24:36 -0700", "Sun 10 May 2015 13:54:36 0000")
