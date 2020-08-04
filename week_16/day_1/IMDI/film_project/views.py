import flask
import flask_login

from . import app
from . import forms
from . import models
from . import db

@app.route("/", methods=['GET','POST'])
def homepage():
    films=models.Film.query.all()
    for film in films:
        print(film.film_cat[0].name)
    return flask.render_template("homepage.html",films=films)

@app.route("/addFilm", methods=['GET','POST'])
def addFilm():

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
                return flask.redirect(flask.url_for("homepage"))
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
        print("****HERE****",country_a_obj)

        new_film=models.Film(title=title,release_date=release_date,film_cat=cat_obj_list,available_in=country_a_obj,origin=country_o_obj,film_dir=dir_obj_list)
        db.session.add(new_film)
        db.session.commit()
        flask.flash(f'{title} was added to our list of films.')
        return flask.redirect(flask.url_for("homepage"))
    return flask.render_template("/film/addFilm.html",form=form)

@app.route("/addDirector", methods=['GET','POST'])
def addDirector():
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
                return flask.redirect(flask.url_for("homepage"))

        film=form.film.data
        film_obj=models.Film.query.filter_by(title=film).first()
        film_list=[]
        film_list.append(film_obj)
        dir_obj=models.Director(first_name=first_name,last_name=last_name,dir_film=film_list)

        db.session.add(dir_obj)
        db.session.commit()
        flask.flash(f'{first_name} {last_name} is a new director.')
        return flask.redirect(flask.url_for("homepage"))
    return flask.render_template("/director/addDirector.html",form=form)

global t
@app.route("/film/modifyFilm/<title>", methods=['GET','POST'])
def modifyFilm(title):
    global t
    t=title

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

    return flask.render_template("/film/modifyFilm.html",form=form,film=film)

global d

@app.route("/film/modifyDirector/<dir>", methods=['GET','POST'])
def modifyDirector(dir):
    global d
    d=dir
    director=models.Director.query.filter_by(id=d).first()
    form=forms.ModifyDirector()

    if flask.request.method=="POST":
        director=models.Director.query.filter_by(id=d).first()
        director.first_name=form.first_name.data
        director.last_name=form.last_name.data
        db.session.commit()
        flask.flash(f"Director's name was modified to {director.first_name} {director.last_name}")
        return flask.redirect(flask.url_for("homepage"))
    return flask.render_template("/director/modifyDirector.html",form=form,director=director)