import flask
import datetime

app=flask.Flask("date_time")



@app.route('/see_time')
def see_time():
        now = datetime.datetime.now()
        print(now)
        html=flask.render_template("bin/index.html",now=now)
        return html

app.run()
    
