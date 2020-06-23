# Exercise 1
import datetime as dt
import holidays

print(dt.date.today())

# Exercise 2

today=dt.date.today()

next_Jan_1=dt.date(2021,1,1)

count_down=next_Jan_1-today

print(count_down)
print("There are {} until next January.".format(count_down))

#isoWeekDay=next_Jan_1.isoweekday()
#print("The number of the weekday on Jan 1, where Mon=1 and Sun=7".format(dt.isoweekday(2021,1,1)))

# Exercise 3

print(dt.datetime.today().weekday())
find_next_holiday=0
prev_holidays=0
for date, name in sorted(holidays.IL(years=2020).items()):
    find_next_holiday+=1
    if date<today:
        prev_holidays+=1
    elif find_next_holiday==prev_holidays+1: 
        print("The next holiday will be",date,name)
        print(name,"will be in",date-today)
    









