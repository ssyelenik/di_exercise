from . import db
from flask_login import UserMixin
from . import login_mgr

@login_mgr.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,nullable=False)
    email = db.Column(db.String(64),unique=True,nullable=False)
    password = db.Column(db.String(64),unique=True,nullable=False)


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