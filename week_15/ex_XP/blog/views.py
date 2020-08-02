import flask
from . import app
import flask_login
from . import models,forms
from . import db
from . import photos

global start
global limit


@app.route("/", methods=['GET','POST'])
def index():
    global start
    global limit
    limit=5
    start=0
    bg=models.Blog.query.all()
    for b in bg:
        print("blogs in the database:",b)
    auth=flask_login.current_user.is_authenticated
    if auth:
        username=flask_login.current_user.username
    else:
        username=""

    if limit<=len(bg):
        limit=5
    else:
        limit=len(bg)
    print("limit",limit)
    if flask.request.method=="POST":
        auth=flask_login.current_user.is_authenticated
        if auth:
            username=flask_login.current_user.username
        else:
            username=""
        bg=models.Blog.query.all()
        limit_req=int(flask.request.form['limit'])
        if limit_req<=len(bg):
            limit=limit_req
        else:
            limit=len(bg)
        print("LIMIT",limit)
        try:
            nav=flask.request.form['prev']
            if start==0:
                pass
            else:
                start-=limit
        except:
            pass

        try:
            nav=flask.request.form['next']
            print("start",start)
            print("limit",limit)
            if start+limit>len(bg) or start+limit==len(bg):
                pass
            else:
                start+=limit
                end=start+limit_req
                if end>len(bg):
                    limit=len(bg)
                else:
                    limit=end

        except:
            pass
        return flask.render_template('index.html',blogs=bg,start=start,limit=limit,auth=auth,username=username)
    return flask.render_template("index.html",blogs=bg,start=start,limit=limit,auth=auth,username=username)


@app.route("/add", methods=['GET','POST'])
def add():
    form=forms.AddUser()
    auth=flask_login.current_user.is_authenticated
    if auth:
        username=flask_login.current_user.username
    else:
        username=""
    if flask.request.method=="POST":
        auth=flask_login.current_user.is_authenticated
        if auth:
            username=flask_login.current_user.username
        else:
            username=""
        user = models.User.query.all()
        for u in user:
            if u.username==flask.request.form['username'] or u.email==flask.request.form["email"] or u.password==flask.request.form["password"]:
                flask.flash("Your details have already been taken. Please try again.", category="error")
                return flask.redirect(flask.url_for("index"))
        username=form.username.data
        email=form.email.data
        password=form.password.data
        new_user=models.User(username=username,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        flask.flash(f'New user {username} has been added to the database.')
        return flask.redirect(flask.url_for('index'))
    return flask.render_template("add.html",form=form,auth=auth,username=username)

@app.route("/login", methods=['POST', "GET"])
def login():
    form=forms.Login()
    auth=flask_login.current_user.is_authenticated
    if auth:
        username=flask_login.current_user.username
    else:
        username=""
    if auth:
        flask.flash(f'{flask_login.current_user} is logged in')
        return flask.redirect(flask.url_for('index'))
    if flask.request.method=="POST":
        auth=flask_login.current_user.is_authenticated
        if auth:
            username=flask_login.current_user.username
        else:
            username=""
        user=models.User.query.filter_by(username=form.username.data).first()
        if user is None or not user.password==form.password.data:
            flask.flash("Invalid username or password")
            return flask.redirect(flask.url_for('login'))
        flask_login.login_user(user)
        flask.flash(f'User {user.username} is logged in.')

        return flask.redirect(flask.url_for("index"))
    return flask.render_template('login.html',form=form,auth=auth,username=username)

@app.route("/view_profile")
@flask_login.login_required
def view_profile():
    auth=flask_login.current_user.is_authenticated
    if auth:
        username=flask_login.current_user.username
    else:
        username=""
    user=models.User.query.filter_by(username=flask_login.current_user.username).first()
    num_articles=len(user.my_blog)
    print("num of articles user posted", num_articles)
    tags=[]
    common_tag=""
    for blog in user.my_blog:
        for tag in blog.my_tag:
            tags.append(tag.tag_name)

    biggest=0
    for tag in tags:
        num=0
        for compare_tag in tags:
            if tag==compare_tag:
                num+=1
        if num>biggest:
            biggest=num
            common_tag=tag

    return flask.render_template("view_profile.html",user=user,common_tag=common_tag,num_articles=num_articles,auth=auth,username=username)

@app.route("/logout")
def logout():
    if flask_login.current_user.is_authenticated:
        flask.flash(f'Goodbye, {flask_login.current_user.username}.')
        flask_login.logout_user()
    return flask.redirect(flask.url_for('index'))

@app.route("/post_blog", methods=['POST', "GET"])
@flask_login.login_required
def post_blog():
    auth=flask_login.current_user.is_authenticated
    if auth:
        username=flask_login.current_user.username
    else:
        username=""
    form=forms.PostBlog()

    tag_obj=models.Tag.query.all()
    tag_list=[]
    for tag in tag_obj:
        tag_list.append((tag.tag_name,tag.tag_name))
    form.tags.choices = tag_list
    if flask.request.method=="POST":

        auth=flask_login.current_user.is_authenticated
        if auth:
            username=flask_login.current_user.username
        else:
            username=""


        filename=photos.save(form.photo.data)
        file_url=photos.url(filename)

        headline=form.headline.data
        body=form.body.data
        user=models.User.query.filter_by(username=flask_login.current_user.username).first()
        blog_obj=models.Blog(headline=headline,body=body,pic=file_url,author=user)
        db.session.add(blog_obj)
        db.session.commit()

        raw_tags=form.new_tags.data
        new_tags=raw_tags.split()

        tags=form.tags.data

        blog=models.Blog.query.filter_by(headline=headline).first()
        tag_list=models.Tag.query.all()
        old=False
        for new_t in new_tags:
            print("new tag",new_t)
            for old_t in tag_list:
                print("old tag",old_t,old_t.tag_name)
                if new_t==old_t.tag_name:
                    print("here---match")
                    tag_obj=models.Tag.query.filter_by(tag_name=t).first()
                    blog.my_tag.append(tag_obj)
                    print(blog.my_tag)
                    db.session.commit()
                    old=True
                    break

            if not old:
                new_tag_obj=models.Tag(tag_name=new_t)
                db.session.add(new_tag_obj)
                db.session.commit()
                nt_o=models.Tag.query.filter_by(tag_name=new_t).first()
                blog.my_tag.append(nt_o)
                db.session.commit()

        if tags:
            for ot in tags:
                tag_obj=models.Tag.query.filter_by(tag_name=ot).first()
                blog.my_tag.append(tag_obj)
                db.session.commit()
        return flask.redirect(flask.url_for("index"))
        # else:
        #     flash.flask("Attempt to load new blog failed.")
        #     return flask.redirect(flask.url_for("index"))

    return flask.render_template("post_blog.html", form=form,auth=auth,username=username)

@app.route("/view_blog", methods=['POST', "GET"])
@flask_login.login_required
def view_blog():
    auth=flask_login.current_user.is_authenticated
    if auth:
        username=flask_login.current_user.username
    else:
        username=""
    headline=flask.request.form['view_blog']
    blog=models.Blog.query.filter_by(headline=headline).first()
    print(blog.pic)
    return flask.render_template("view_blog.html",blog=blog,auth=auth,username=username)