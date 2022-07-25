from datetime import date
import calendar


d0 = date(2017, 8, 18)
d1 = date(2017, 10, 26)
delta = d1 - d0
# print(delta.days)

#  formats the input into something that can be used in dateTime
def get_month(d1):
    m1 = list(calendar.month_abbr).index(d1[2])
    return(m1)
cd one
#  find the amount of days in between the two given times
def day_delta(d1, d2):

    d1 = d1.split()
    d2 = d2.split()
    print(type(get_month(d1)))

    df = date(int(d1[3]),get_month(d1), int(d1[1]))
    di = date(int(d2[3]),get_month(d2), int(d2[1]))

    delta = abs(df - di)
    return(delta)


# def hor_delta(h1, h2):


# print(get_month("Sun 10 May 2015 13:54:36 -0700"))

print(day_delta("Sun 12 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 0000"))
