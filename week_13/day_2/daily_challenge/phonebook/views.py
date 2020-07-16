import flask
from . import app,db
from . import models,forms

global matching_entry


@app.route("/add_person", methods=['GET','POST'])
def add_person():
    form=forms.AddPerson()
    if flask.request.method=="POST":

        phone_num=str(flask.request.form['phone_num'])
        name=str(flask.request.form['name'])
        email=str(flask.request.form['email'])
        address=str(flask.request.form['address'])
        nat_name=(flask.request.form['nationality'])
        print(nat_name)
        nat_obj=models.Nationality.query.filter_by(name=nat_name).first()
        print(nat_obj.name)
        p=models.Person(phone_num=phone_num,name=name,email=email,address=address,nat=nat_obj)
        db.session.add(p)
        db.session.commit()
        my_friend=models.Person.query.filter_by(name="Daniel").first()
        print(my_friend.nat.name)
        Israeli=models.Nationality.query.filter_by(name="Israeli").first()
        print(Israeli.people)
        for i in range(len(Israeli.people)):
            print(Israeli.people[i].name)
        flask.flash(f'{name} was added to the phone book with nationality {nat_name}.')
        flask.redirect(flask.url_for('index'))
    return flask.render_template('add_person.html',form=form)

@app.route("/", methods=['GET','POST'])
def index():
    global matching_entry
    matching_entry=""
    form = forms.SetSearch()
    if flask.request.method=="POST":
        name="empty"
        phone_num="empty"
        print("here")
        try:
            name=flask.request.form['name']
            print(name)
            matching_entry=models.Person.query.filter_by(name=name).first()
            print(matching_entry)
            if not matching_entry==None:
                return flask.redirect(flask.url_for('display'))

            elif not name=='':
                flask.flash("Your search was not found in the phone book.")
                return flask.redirect(flask.url_for('index'))
        except:
            pass

        try:
            phone_num=flask.request.form['phone_num']
            matching_entry=models.Person.query.filter_by(phone_num=phone_num).first()
            if not matching_entry==None:
                return flask.redirect(flask.url_for('display'))

            elif not phone=='':
                flask.flash("Your search was not found in the phone book.")
                return flask.redirect(flask.url_for('index'))
        except:
            pass

        if phone_num=="" and name=="":
            flask.flash("You didn't enter a search parameter")
            return flask.redirect(flask.url_for('index'))

    return flask.render_template("index.html",form=form)

@app.route("/display", methods=['GET','POST'])
def display():
    global matching_entry
    form=forms.Display()
    if flask.request.method=="POST":
        return flask.redirect(flask.url_for('index'))

    return flask.render_template("display.html",matching_entry=matching_entry)

@app.route("/add_nationality", methods=['GET','POST'])
def add_nationality():
    global matching_entry
    if flask.request.method=="POST":
        nationality=flask.request.form['nationality']

        # nat=models.Nationality(name=nationality)
        # print("*****************",matching_entry.name,matching_entry.id)
        # per=models.Person(id=matching_entry.id)
        # per.people_nationalities.append(nat)
        # db.session.add(per)
        # db.session.commit()

        flask.flash(f'The nationality {nationality} was added to {matching_entry.name}')
        try:
            button=flask.request.form['stop']
            return flask.redirect(flask.url_for('index'))
        except:
            return flask.redirect(flask.url_for('add_nationality'))
    return flask.render_template("add_nationality.html",matching_entry=matching_entry)

@app.route("/search_by_nat", methods=['GET','POST'])
def search_by_nat():


    return flask.render_template("search_by_nat.html")

@app.route("/display_nat", methods=['GET','POST'])
def display_nat():
    search_nat=flask.request.form['nationality']
    nat_obj=models.Nationality.query.filter_by(name=search_nat).first()
    ppl=nat_obj.people
    print(ppl)
    return flask.render_template('display_nat.html',ppl=ppl)
