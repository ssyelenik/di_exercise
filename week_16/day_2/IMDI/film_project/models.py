from . import db, login_mgr, mail_mgr
import flask_mail,flask
from flask_login import UserMixin
from .auth.models import User


# @login_mgr.user_loader
# def user_loader(user_id):
#     return User.query.get(user_id)
#
# class User(db.Model, UserMixin):
#     id=db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(64),unique=True,nullable=False)
#     email = db.Column(db.String(64),unique=True,nullable=False)
#     password = db.Column(db.String(64),unique=True,nullable=False)


class Country(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True,nullable=False)
    film_created_location=db.relationship("Film",backref="origin")
    film_available_location=db.relationship("Film",secondary='film_country',back_populates="available_in")

class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True,nullable=False)
    cat_film=db.relationship("Film",secondary='film_cat',back_populates="film_cat")

class Film(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,unique=True,nullable=False)
    release_date=db.Column(db.String,nullable=False)
    country_of_origin=db.Column(db.Integer,db.ForeignKey('country.id'))
    film_cat=db.relationship("Category",secondary='film_cat',back_populates="cat_film")
    film_dir=db.relationship("Director",secondary='film_dir',back_populates="dir_film")
    available_in=db.relationship("Country",secondary='film_country',back_populates="film_available_location")
    photo_id=db.Column(db.Integer,db.ForeignKey('photo.id'))
    avg_rating=db.Column(db.Integer)
    film_rating=db.relationship("FilmRating",backref="rated")

class Photo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    photo=db.Column(db.String,unique=True)
    explanation_img=db.Column(db.String,unique=True)
    film_photo=db.relationship("Film",uselist=False,backref="pho")

class Director(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String)
    last_name=db.Column(db.String)
    dir_film=db.relationship("Film",secondary='film_dir',back_populates="film_dir")

film_cat=db.Table("film_cat",
                  db.Column('film_id',db.Integer,db.ForeignKey('film.id')),
                  db.Column('cat_id',db.Integer,db.ForeignKey('category.id'))
                  )

film_dir=db.Table("film_dir",
                  db.Column('film_id',db.Integer,db.ForeignKey('film.id')),
                  db.Column('dir_id',db.Integer,db.ForeignKey('director.id'))
                  )

film_country=db.Table("film_country",
                  db.Column('film_id',db.Integer,db.ForeignKey('film.id')),
                  db.Column('country_id',db.Integer,db.ForeignKey('country.id'))
                  )

class FilmRating(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    film_id=db.Column(db.Integer,db.ForeignKey('film.id'))
    rating=db.Column(db.Integer)
    comment=db.Column(db.String)