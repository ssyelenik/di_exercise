import flask
from faker import Faker
import random
 
resume = flask.Flask(__name__)
fake=Faker()

@resume.route('/index')
def index():
    return flask.render_template('home.jin/index.html',name=fake.name(),address=fake.address(),empl_name=[fake.name(),fake.name(),fake.name()],empl_address=[fake.address(),fake.address(),fake.address()],text=[fake.text(),fake.text(),fake.text()])

   

@resume.route("/pic", methods=['GET', 'POST'])
def pic_func():
    pic_num=random.randint(1,11)
    sharon_pic="/static/Sharon"+ str(pic_num)+".jpg"
    if flask.request.method == 'POST':
        return redirect(flask.url_for('index'))
    return flask.render_template('home.jin/pic.html',sharon_pic=sharon_pic)

resume.run()





