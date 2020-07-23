import flask
from . import app
from . import db
from . import models
from . import forms
from . import daters
from . import search

global gender
global alias
global password
global active
active=False
alias=""
gender=""
password=""

@app.route("/", methods=['GET','POST'])
def index():
    global gender
    global alias
    global password

    if flask.request.method=="POST":
        try:
            gender=flask.request.form["gender"]
            alias=flask.request.form["alias"]
            password=flask.request.form["password"]
        except:
            flask.flash("Your login was unsuccessful. Please fill in all fields.")
            flask.redirect(flask.url_for('index'))

        if gender=="man":
            man_obj=daters.Man(password,alias)
            all_men=man_obj.get_all_men()
            for man in all_men:
                if man.alias==alias and man.password==password:
                    return flask.redirect(flask.url_for('dater_view',dater=man))
            return flask.redirect(flask.url_for('dating_survey'))

        if gender == "woman":
            woman_obj=daters.Woman(password,alias)
            all_women=woman_obj.get_all_women()
            for woman in all_women:
                if woman.alias==alias and woman.password==password:
                    return flask.redirect(flask.url_for('dater_view',dater=woman))
            return flask.redirect(flask.url_for('dating_survey'))
    return flask.render_template("index.html")

@app.route("/dating_survey", methods=['GET','POST'])
def dating_survey():
    global gender
    global alias
    global password

    form=forms.DatingSurvey()
    if flask.request.method=="POST":
        first_name=flask.request.form['first_name'].encode()
        last_name=flask.request.form['last_name'].encode()
        status=flask.request.form['status'].encode()
        phone=flask.request.form['phone'].encode()
        email=flask.request.form['email'].encode()
        city=flask.request.form['city'].encode()
        state=flask.request.form['state'].encode()
        age_group=flask.request.form['age_group'].encode()
        country=flask.request.form['country'].encode()
        hobbies=flask.request.form['hobbies'].encode()
        profession=flask.request.form['profession'].encode()
        personality=flask.request.form['personality'].encode()
        in_extrovert=flask.request.form['in_extrovert'].encode()
        image=flask.request.form['image'].encode()
        personal_comment=flask.request.form['personal_comment'].encode()
        if gender=="man":
            man_obj=models.Man(alias=alias, age_group=age_group,password=password,first_name=first_name,last_name=last_name,status=status,phone=phone,email=email,city=city,state=state,country=country,hobbies=hobbies,profession=profession,personality=personality,in_extrovert=in_extrovert,image=image,personal_comment=personal_comment)
            print(man_obj.first_name)
            db.session.add(man_obj)
            db.session.commit()
            flask.flash(f'Congratulations, {first_name} {last_name}. You just became a member of "Behind the Scenes"!')
        elif gender=="woman":
            woman_obj=models.Woman(alias=alias, age_group=age_group,password=password,first_name=first_name,last_name=last_name,status=status,phone=phone,email=email,city=city,state=state,country=country,hobbies=hobbies,profession=profession,personality=personality,in_extrovert=in_extrovert,image=image,personal_comment=personal_comment)
            db.session.add(woman_obj)
            db.session.commit()
            flask.flash(f'Congratulations, {first_name} {last_name}. You just became a member of "Behind the Scenes"!')
        return flask.redirect(flask.url_for('dater_view'))
    return flask.render_template("dating_survey.html",form=form)

def save_msg(msg,recipient):
    global alias
    global active
    active=True
    if gender=="man":
        print(msg,recipient)
        sender_obj=models.Man.query.filter_by(alias=alias).first()
        new_msg=models.Msghimtoher(message=msg)
        new_msg.woman_rc=models.Woman.query.filter_by(alias=recipient).first()
        sender_obj.man_sp.append(new_msg)
        db.session.commit()
        flask.flash(f"{alias},Your message was successfully send to {recipient}.")
    else:
        sender_obj=models.Woman.query.filter_by(alias=alias).first()
        new_msg=models.Msghertohim(message=msg)
        new_msg.man_rc=models.Man.query.filter_by(alias=recipient).first()
        sender_obj.woman_sp.append(new_msg)
        db.session.commit()
        flask.flash(f"{alias},Your message was successfully send to {recipient}.")

@app.route("/dater_view", methods=['GET','POST'])
def dater_view():
    if flask.request.method=="POST":
        global gender
        global alias
        msg=flask.request.form['msg']
        recipient=flask.request.form['msg_recipient']
        save_msg(msg,recipient)
    return flask.render_template("dater_view.html",alias=alias)

@app.route("/messaging", methods=['GET','POST'])
def messaging():
    if gender=="man":
        man_r=models.Man.query.filter_by(alias=alias).first()
        msgs=models.Msghertohim.query.filter_by(man_receipeint_id=man_r.id).all()
        women_s=models.Woman.query.all()
        dict={}
        all_messages=[]
        for msg in msgs:
            for wo_s in women_s:
                if wo_s.id==msg.woman_sender_id:
                    dict={'sender':wo_s.alias,'message':msg.message}
                    all_messages.append(dict)
                    break
    else:
        woman_r=models.Woman.query.filter_by(alias=alias).first()
        msgs=models.Msghimtoher.query.filter_by(woman_receiver_id=woman_r.id).all()
        men_s=models.Man.query.all()
        dict={}
        all_messages=[]
        for msg in msgs:
            for m_s in men_s:
                if m_s.id==msg.man_sender_id:
                    dict={'sender':m_s.alias,'message':msg.message}
                    all_messages.append(dict)
                    break
    if all_messages=="":
        flask.flash(f"{alias}, you have no messages at the moment.")
        return flask.redirect(flask.url_for("dater_view"))

    if flask.request.method=="POST":
        new_msg=flask.request.form['msg_text']
        recipient=flask.request.form['sender']
        print(recipient)
        save_msg(new_msg,recipient)
        return flask.redirect(flask.url_for('dater_view'))
    return flask.render_template("messaging.html",all_messages=all_messages,alias=alias)



@app.route("/searching", methods=['GET','POST'])
def searching():
    return flask.render_template("searching.html",alias=alias)

@app.route("/view_dates", methods=['GET','POST'])
def view_dates():
    global active
    if active:
        flask.flash(f"{alias}, you are in active communication with someone.")
        flask.flash("Please deactivate your communication if you would like to search the database again.")
        return flask.redirect(flask.url_for('dater_view'))
    search_method=flask.request.form['search']
    people_found=[]
    if gender=="man":
        man_obj=daters.Man(password,alias)
        all_women=models.Woman.query.all()
        current_man=man_obj.get_current_man(alias)
        if search_method=="view_all":
            people_found=all_women

        if search_method=="view_auto":
            print("view_auto")
            score=0
            for woman in all_women:
                if current_man.age_group==woman.age_group:
                    score+=5
                if current_man.status==woman.status:
                    score+=3
                if current_man.country==woman.country and current_man.state==woman.state and current_man.city==woman.city:
                    score+=5
                if current_man.hobbies==woman.hobbies:
                    score+=3
                if current_man.profession==woman.profession:
                    score+=2
                if current_man.in_extrovert==woman.in_extrovert:
                    score+=3
                man_comment=current_man.personal_comment
                woman_comment=woman.personal_comment
                word_count=0
                for word in man_comment:
                    if word in woman_comment:
                        word_count+=1
                if word_count>6:
                    score+=4
                if score>10:
                    print("appending",woman.alias)
                    people_found.append(woman)


        if search_method=="view_age":
            for woman in all_women:
                if woman.age_group==current_man.age_group:
                    people_found.append(woman)

        if search_method=="view_interests":
            for woman in all_women:
                if woman.hobbies==current_man.hobbies or woman.in_extrovert==current_man.in_extrovert:
                    people_found.append(woman)

        if search_method=="view_profession":
            for woman in all_women:
                if woman.hobbies==current_man.hobbies:
                    people_found.append(woman)




    if gender=="woman":
        woman_obj=daters.Woman(password,alias)
        all_men=models.Man.query.all()
        current_woman=woman_obj.get_current_woman(alias)
        if search_method=="view_all":
            people_found=all_men
        if search_method=="view_auto":
            score=0
            for man in all_men:
                if current_woman.age_group==man.age_group:
                    score+=5
                if current_woman.status==man.status:
                    score+=3
                if current_woman.country==man.country and current_woman.state==man.state and current_woman.city==man.city:
                    score+=5
                if current_woman.hobbies==man.hobbies:
                    score+=3
                if current_woman.profession==man.profession:
                    score+=2
                if current_woman.in_extrovert==man.in_extrovert:
                    score+=3
                woman_comment=current_woman.personal_comment
                man_comment=man.personal_comment
                word_count=0
                for word in man_comment:
                    if word in woman_comment:
                        word_count+=1
                if word_count>6:
                    score+=4
                if score>17:
                    people_found.append(man)

        if search_method=="view_age":
            for man in all_men:
                if current_woman.age_group==man.age_group:
                    people_found.append(man)

        if search_method=="view_interests":
            for man in all_men:
                if man.hobbies==current_woman.hobbies or man.in_extrovert==current_woman.in_extrovert:
                    people_found.append(man)

        if search_method=="view_profession":
            for man in all_men:
                if man.hobbies==current_woman.hobbies:
                    people_found.append(man)
    print(people_found,len(people_found))
    if len(people_found)==0:
        print("here")
        flask.flash("Your search had no matches. Try another search!")
    return flask.render_template("view_dates.html",alias=alias,people_found=people_found)



@app.route("/planning", methods=['GET','POST'])
def planning():
    place_details={}
    param=flask.request.form['param']
    search_results=search.make_plans(param)
    print(search_results)
    place_details['address']=search_results['candidates'][0]['formatted_address']
    print(place_details['address'])
    place_details['name']=search_results['candidates'][0]['name']
    print(place_details['name'])
    try:
        open=search_results['candidates'][0]['opening_hours']
        if open:
            place_details['open']="Open now"
        else:
            place_details['open']="Not open now"
    except:
        place_details['open']="Opening times unknown"
    print(place_details['open'])
    url=str(search_results['candidates'][0]['photos'][0]['html_attributions'])
    print(url)
    start=url.find('="')+2
    end=url.find(">")-1
    place_details['url']=url[slice(start,end)]
    print(place_details)
    return flask.render_template("planning.html",alias=alias,place_details=place_details)

@app.route("/send_msg", methods=['GET','POST'])
def send_msg():
    global gender
    global alias
    global msg_receiver
    name=flask.request.form['msg_recipient']
    if gender=="man":
        msg_receiver=models.Woman.query.filter_by(alias=name).first()
    else:
        msg_receiver=models.Man.query.filter_by(alias=name).first()
    # if flask.request.method=="POST":
    #     new_msg=flask.request.form['msg']
    #     recipient=flask.request.form['recipient']
    #     print(recipient)
    #     save_msg(new_msg,recipient)
    #     flask.flash(f"{alias}, you sent a new message to {recipient}.")
    #     return flask.redirect(flask.url_for('dater_view'))
    return flask.render_template("send_msg.html",person=msg_receiver)

@app.route("/logout", methods=['GET','POST'])
def logout():


    global gender
    global alias
    global password
    flask.flash(f"Goodbye, {alias}! See you next time.")
    gender=""
    alias=""
    password=""
    if flask.request.method=="POST":
        try:
            gender=flask.request.form["gender"]
            alias=flask.request.form["alias"]
            password=flask.request.form["password"]
        except:
            flask.flash("Your login was unsuccessful. Please fill in all fields.")
            flask.redirect(flask.url_for('index'))

        if gender=="man":
            man_obj=daters.Man(password,alias)
            all_men=man_obj.get_all_men()
            for man in all_men:
                if man.alias==alias and man.password==password:
                    return flask.redirect(flask.url_for('dater_view',dater=man))
            return flask.redirect(flask.url_for('dating_survey'))

        if gender == "woman":
            woman_obj=daters.Woman(password,alias)
            all_women=woman_obj.get_all_women()
            for woman in all_women:
                if woman.alias==alias and woman.password==password:
                    return flask.redirect(flask.url_for('dater_view',dater=woman))
            return flask.redirect(flask.url_for('dating_survey'))

    return flask.render_template("logout.html")

@app.route("/deactivate", methods=['GET','POST'])
def deactivate():
    global active
    if flask.request.method=="POST":
        try:
            cancel=flask.request.form['cancel']
            return flask.redirect(flask.url_for('dater_view'))
        except:
            pass
        active=False
        flask.flash(f"{alias}, you just deactivated your communication. You can search the database and contact someone else.")
        return flask.redirect(flask.url_for('dater_view'))
    return flask.render_template("deactivate.html")