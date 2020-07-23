from . import db
from . import app
from . import models

class Man():
    alias=None
    password=None
    def __init__(self,password,alias):
        Man.alias=alias
        Man.password=password
        self.alias=alias
        self.password=password

    def get_all_men(self):
        men=models.Man.query.all()
        return men

    def get_current_man(self,alias):
        man=models.Man.query.filter_by(alias=alias).first()
        return man

class Woman():
    alias=None
    password=None
    def __init__(self,password,alias):
        Woman.alias=alias
        Woman.password=password
        self.alias=alias
        self.password=password

    def get_all_women(self):
        women=models.Woman.query.all()
        return women

    def get_current_woman(self,alias):
        woman=models.Woman.query.filter_by(alias=alias).first()
        return woman