import flask, flask_login, flask_mail
from werkzeug.utils import secure_filename
from . import forms
import film_project
import os
from . import models
from .auth.models import User
from . import db, login_mgr, mail_mgr


main_blueprint=flask.Blueprint('main',__name__)

def set_role():
    print("IN SET_ROLE")
    if flask_login.current_user.is_authenticated:
        print("USER IS AUTHENTICATED")
        print(flask_login.current_user.id)
        user_obj=User.query.filter_by(id=flask_login.current_user.id).first()
        print(user_obj.permission.name)
        return user_obj.permission.name
    else:
        print("NO USER")
        return None


@main_blueprint.route("/", methods=['GET','POST'])
def homepage():

    role=set_role()
    films=models.Film.query.all()
    print(films[0].film_rating)
    print(films[0].film_rating[0].comment)
    return flask.render_template("homepage.html",films=films,role=role)

@main_blueprint.route("/addFilm", methods=['GET','POST'])
def addFilm():
    role=set_role()
    form=forms.AddFilm()
    countries=models.Country.query.all()
    categories=models.Category.query.all()
    directors=models.Director.query.all()
    country_list=[]
    for country in countries:
        country_list.append(country.name)
    form.country_of_origin.choices=country_list

    country_m_list=[]
    for country in countries:
        country_m_list.append((country.name,country.name))
    form.available_in_countries.choices=country_m_list

    category_list=[]
    for category in categories:
        category_list.append((category.name,category.name))
    form.category.choices=category_list

    director_list=[]
    for director in directors:
        print(director)
        dir=director.first_name+" "+director.last_name
        print(dir)
        director_list.append((director.id,dir))

    form.director.choices=director_list

    if flask.request.method=="POST":
        title=form.title.data

        films=models.Film.query.all()
        for film in films:
            if title==film.title:
                flask.flash(f'{title} is already registered as a film.')
                return flask.redirect(flask.url_for("main.homepage"))
        release_date=form.release_date.data
        country_of_origin=form.country_of_origin.data
        country_o_obj=models.Country.query.filter_by(name=country_of_origin).first()

        cat_obj_list=[]
        category=form.category.data
        for cat in category:
            category_obj=models.Category.query.filter_by(name=cat).first()
            cat_obj_list.append(category_obj)

        dir_obj_list=[]
        director=form.director.data
        for dir in director:
            dir_obj=models.Director.query.filter_by(id=dir).first()
            dir_obj_list.append(dir_obj)

        country_a_obj=[]
        available_in_countries=form.available_in_countries.data
        for country in available_in_countries:
            print(country)
            c=models.Country.query.filter_by(name=country).first()
            print(c)
            country_a_obj.append(c)
        f=form.photo.data
        print(f)
        filename=secure_filename(f.filename)
        basedir = os.path.abspath(
             os.path.dirname(__file__)
        )
        path_name=os.path.join('static',filename)
        f.save(os.path.join(basedir,'static',filename))

        photo_obj=models.Photo(photo=path_name,explanation_img=form.explanation.data)
        new_film=models.Film(title=title,release_date=release_date,pho=photo_obj,film_cat=cat_obj_list,available_in=country_a_obj,origin=country_o_obj,film_dir=dir_obj_list)
        db.session.add(new_film)
        db.session.commit()
        flask.flash(f'{title} was added to our list of films.')
        return flask.redirect(flask.url_for("main.homepage"))
    return flask.render_template("/film/addFilm.html",form=form,role=role)

@main_blueprint.route("/addDirector", methods=['GET','POST'])
def addDirector():
    role=set_role()
    form=forms.AddDirector()
    films=models.Film.query.all()
    film_list=[]
    for film in films:
        film_list.append(film.title)
    form.film.choices=film_list
    if flask.request.method=="POST":

        first_name=form.first_name.data
        last_name=form.last_name.data

        directors=models.Director.query.all()
        for director in directors:
            if first_name==director.first_name and last_name==director.last_name:
                flask.flash(f'{first_name} {last_name} is already registered as a director.')
                return flask.redirect(flask.url_for("main.homepage"))

        film=form.film.data
        film_obj=models.Film.query.filter_by(title=film).first()
        film_list=[]
        film_list.append(film_obj)
        dir_obj=models.Director(first_name=first_name,last_name=last_name,dir_film=film_list)

        db.session.add(dir_obj)
        db.session.commit()
        flask.flash(f'{first_name} {last_name} is a new director.')
        return flask.redirect(flask.url_for("main.homepage"))
    return flask.render_template("/director/addDirector.html",form=form,role=role)

global t
@main_blueprint.route("/film/modifyFilm/<title>", methods=['GET','POST'])
def modifyFilm(title):
    global t
    global role
    t=title

    role=set_role()

    form=forms.ModifyFilm()
    film=models.Film.query.filter_by(title=t).first()
    form.title.placeholder=film.title
    countries=models.Country.query.all()
    categories=models.Category.query.all()

    country_list=[]
    for country in countries:
        country_list.append(country.name)
    form.country_of_origin.choices=country_list


    category_list=[]
    for category in categories:
        category_list.append((category.name,category.name))
    form.category.choices=category_list


    if flask.request.method=="POST":

        update_film=models.Film.query.filter_by(title=t).first()
        new_title=form.title.data
        new_release_date=form.release_date.data

        new_country=form.country_of_origin.data
        new_country_obj=models.Country.query.filter_by(name=new_country).first()

        new_cat_obj_list=[]
        new_category=form.category.data
        for cat in new_category:
            new_category_obj=models.Category.query.filter_by(name=cat).first()
            new_cat_obj_list.append(new_category_obj)

        update_film.title=new_title
        update_film.release_date=new_release_date
        update_film.film_cat=new_cat_obj_list
        update_film.origin=new_country_obj

        db.session.commit()
        flask.flash(f'{title} was updated.')
        return flask.redirect(flask.url_for("homepage"))

    return flask.render_template("/film/modifyFilm.html",form=form,film=film,role=role)

global d

@main_blueprint.route("/film/modifyDirector/<dir>", methods=['GET','POST'])
def modifyDirector(dir):
    global d
    d=dir
    director=models.Director.query.filter_by(id=d).first()
    role=set_role()
    form=forms.ModifyDirector()

    if flask.request.method=="POST":
        director=models.Director.query.filter_by(id=d).first()
        director.first_name=form.first_name.data
        director.last_name=form.last_name.data
        db.session.commit()
        flask.flash(f"Director's name was modified to {director.first_name} {director.last_name}")
        return flask.redirect(flask.url_for("homepage"))
    return flask.render_template("/director/modifyDirector.html",form=form,director=director,role=role)

@main_blueprint.route("/director/deleteDirector/", methods=['GET','POST'])
def deleteDirector():
    role=set_role()
    form=forms.DeleteDirector()
    director_obj=models.Director.query.all()
    director_list=[]
    for dir in director_obj:
        first_name=dir.first_name
        last_name=dir.last_name
        name=first_name+" "+last_name
        id=dir.id
        director_list.append((id,name))
    form.director.choices=director_list
    if flask.request.method=="POST":
        dir_del_obj=models.Director.query.filter_by(id=form.director.data).first()
        db.session.delete(dir_del_obj)
        db.session.commit()
        return flask.redirect(flask.url_for("main.homepage"))
    return flask.render_template("/director/deleteDirector.html",form=form,role=role)

@main_blueprint.route("/film/deleteFilm/", methods=['GET','POST'])
def deleteFilm():
    role=set_role()
    form=forms.DeleteFilm()
    film_obj=models.Film.query.all()
    film_list=[]
    for f in film_obj:
        film_list.append((f.title,f.title))
    form.title.choices=film_list
    if flask.request.method=="POST":
        film_del_obj=models.Film.query.filter_by(title=form.title.data).first()
        db.session.delete(film_del_obj)
        db.session.commit()
        return flask.redirect(flask.url_for("main.homepage"))
    return flask.render_template("/film/deleteFilm.html",form=form,role=role)

@main_blueprint.route("/film/rateFilm/<title>", methods=['GET','POST'])
def rateFilm(title):
    global t
    t=title
    film=models.Film.query.filter_by(title=t).first()
    form=forms.FilmRating()
    form.num.choices=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
    if flask.request.method=="POST":
        film_obj=models.Film.query.filter_by(title=t).first()
        rating_obj=models.FilmRating(comment=form.comment.data, rating=form.num.data, film_id=film_obj.id)
        db.session.add(rating_obj)
        db.session.commit()
        sum=0
        num=0
        for rat in film_obj.film_rating:
            print("RATING",rat.rating)
            print("SUM",sum)
            print("NUM ITERATIONS",num)
            if not rat.rating==None:
                sum+=rat.rating
                num+=1
            else:
                pass
        if sum>0 and num>0:
            raw_avg_rating=sum/num
        else:
            raw_avg_rating=0
        if raw_avg_rating<.5:
            avg_rating=0
        elif raw_avg_rating>=.5 and raw_avg_rating<1.5:
            avg_rating=1
        elif raw_avg_rating>=1.5 and raw_avg_rating<2.5:
            avg_rating=2
        elif raw_avg_rating>=2.5 and raw_avg_rating<3.5:
            avg_rating=3
        elif raw_avg_rating>=3.5 and raw_avg_rating<4.5:
            avg_rating=4
        else:
            avg_rating=5
        print(avg_rating)
        film_obj.avg_rating=avg_rating
        print("HOPE IT WENT TO THE OBJECT",film_obj.title,film_obj.avg_rating)
        db.session.commit()
        return flask.redirect(flask.url_for('main.homepage'))
    return flask.render_template("film/rateFilm.html",form=form,film=film)
