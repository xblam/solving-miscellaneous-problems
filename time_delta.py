from datetime import date, datetime
import calendar


# datetime1 = date(2004, 3,17)
# datetime2 = date(2004,5,17)
# sec_days =  int(datetime1 - datetime2)
# print(sec_days*3600*24)

#  formats the input into something that can be used in dateTime
def get_month(month):
    m1 = list(calendar.month_abbr).index(month)
    return(m1)


#  find the amount of days in between the two given datetime
#  intput = two days
#  return =  difference in days (day1 - day2)
def day_delta(datetime1, datetime2):

    d1 = datetime1
    d2 = datetime2
    
    delta_days = (d1 - d2)
    return(delta_days.total_seconds())



#  input= ts1:timestamp1, ts2:timestamp2
#  output= time difference between timestamps t1-t2 (in seconds)
def hour_delta(ts1, ts2):
    t1 = datetime.strptime(ts1, "%H:%M:%S")
    t2 = datetime.strptime(ts2, "%H:%M:%S")
    delta_time = t1 - t2
    return(delta_time.total_seconds())



#  finds seconds given difference in GMT time
#  input= gmt1:gmt zone 1, gmt2:gmt zone 2
#  output= difference between the time zones in seconds (gmt1-gmt2)
def gmt_delta(gmt1,gmt2):
    hours1 = -(gmt1//100*3600)
    hours2 = -(gmt2//100*3600)
    minutes1 = -(gmt1%100*60)
    minutes2 = -(gmt2%100*60)
    total_sec = hours1+minutes1-hours2-minutes2
    return total_sec




def time_delta(t1, t2):
    t1 = t1.split()
    t2 = t2.split()

    #  turn month into abbreviation so it fits into datetime format
    month1 = get_month(t1[2])
    month2 = get_month(t2[2])

    #  date1 and date2 datetime format for day_delta
    datetime1 = date(int(t1[3]), month1, int(t1[1]))
    datetime2 = date(int(t2[3]), month2, int(t2[1]))
    sec_days = day_delta(datetime1,datetime2)

    #  timestamps for hour_delta
    ts1 = t1[4]
    ts2 = t2[4]
    sec_hours = (hour_delta(ts1,ts2))

    gmt1 = int(t1[5])
    gmt2 = int(t2[5])
    sec_gmt = gmt_delta(gmt1,gmt2)

    
    
    
    total_secs = sec_days + sec_hours + sec_gmt
    return(str((abs(int(total_secs)))))




print(time_delta('Sat 09 Jun 1979 12:33:03 +0200',
'Sat 28 Dec 2120 16:55:13 +0500'))


