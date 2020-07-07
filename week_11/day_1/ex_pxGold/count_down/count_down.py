import flask
import datetime as dt
import holidays

count_down=flask.Flask("count_down")

@count_down.route("/count_down")
def count():
    today=dt.date.today()
    find_next_holiday=0
    prev_holidays=0
    for date, name in sorted(holidays.IL(years=2020).items()):
        find_next_holiday+=1
        if date<today:
            prev_holidays+=1
        elif find_next_holiday==prev_holidays+1: 
            next_holiday=name
            next_holiday_date=date
            count=date-today
    html=flask.render_template("bin/index.html",next_holiday=next_holiday,next_holiday_date=next_holiday_date,count=count)
    return html

count_down.run()
    
