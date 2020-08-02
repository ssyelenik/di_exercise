from . import db
from flask_login import UserMixin
from . import login_mngr

@login_mngr.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,nullable=False)
    email = db.Column(db.String(64),unique=True,nullable=False)
    password = db.Column(db.String(64),unique=True,nullable=False)
    my_blog=db.relationship("Blog",backref='author')

class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    headline=db.Column(db.String(200),unique=True,nullable=False)
    body=db.Column(db.Text,nullable=False)
    pic=db.Column(db.String)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    my_tag=db.relationship("Tag",secondary='tag_blog',back_populates="my_blog")

tag_blog=db.Table("tag_blog",
                  db.Column('blog_id',db.Integer,db.ForeignKey('blog.id')),
                  db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'))
                  )

class Tag(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    tag_name=db.Column(db.String,nullable=False,unique=True)
    my_blog=db.relationship("Blog",secondary='tag_blog',back_populates="my_tag")



