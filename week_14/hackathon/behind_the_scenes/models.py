from . import db
from flask_sqlalchemy import SQLAlchemy

class Man(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String)
    last_name=db.Column(db.String)
    alias=db.Column(db.String(60),unique=True)
    password=db.Column(db.String)
    status=db.Column(db.String)
    age_group=db.Column(db.String)
    phone=db.Column(db.String)
    email=db.Column(db.String)
    city=db.Column(db.String)
    state=db.Column(db.String)
    country=db.Column(db.String)
    hobbies=db.Column(db.String)
    profession=db.Column(db.String)
    personality=db.Column(db.String)
    in_extrovert=db.Column(db.String)
    image=db.Column(db.String)
    personal_comment=db.Column(db.String)
    man_dp=db.relationship("Date",back_populates='man_dc')
    man_sp=db.relationship("Msghimtoher",back_populates='man_sc')
    man_rp=db.relationship("Msghertohim",back_populates='man_rc')

class Woman(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String)
    last_name=db.Column(db.String)
    alias=db.Column(db.String(60),unique=True)
    password=db.Column(db.String,unique=True)
    image=db.Column(db.String)
    status=db.Column(db.String)
    age_group=db.Column(db.String)
    phone=db.Column(db.String)
    email=db.Column(db.String)
    city=db.Column(db.String)
    state=db.Column(db.String)
    country=db.Column(db.String)
    hobbies=db.Column(db.String)
    profession=db.Column(db.String)
    personality=db.Column(db.String)
    in_extrovert=db.Column(db.String)
    #picture
    personal_comment=db.Column(db.String)
    woman_dp=db.relationship('Date',back_populates="woman_dc")
    woman_sp=db.relationship("Msghertohim",back_populates="woman_sc")
    woman_rp=db.relationship("Msghimtoher",back_populates="woman_rc")




class Msghimtoher(db.Model):
    msg_id=db.Column(db.Integer,primary_key=True)
    man_sender_id=db.Column(db.Integer,db.ForeignKey('man.id'))
    message=db.Column(db.String)
    # active=db.Column(db.Boolean)
    woman_receiver_id=db.Column(db.Integer,db.ForeignKey('woman.id'))
    man_sc=db.relationship("Man",back_populates="man_sp")
    woman_rc=db.relationship("Woman",back_populates="woman_rp")

class Date(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    man_id=db.Column(db.Integer,db.ForeignKey('man.id'))
    woman_id=db.Column(db.Integer,db.ForeignKey('woman.id'))
    active=db.Column(db.Boolean)
    comment=db.Column(db.String)
    man_dc=db.relationship("Man",back_populates='man_dp')
    woman_dc=db.relationship("Woman",back_populates='woman_dp')

class Msghertohim(db.Model):
    msg_id=db.Column(db.Integer,primary_key=True)
    woman_sender_id=db.Column(db.Integer,db.ForeignKey('woman.id'))
    message=db.Column(db.String)
    # active=db.Column(db.Boolean)
    man_receipeint_id=db.Column(db.Integer,db.ForeignKey('man.id'))
    woman_sc=db.relationship("Woman",back_populates="woman_sp")
    man_rc=db.relationship("Man",back_populates="man_rp")
