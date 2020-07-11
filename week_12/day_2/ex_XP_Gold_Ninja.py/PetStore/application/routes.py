import flask
from . import app
from . import pets_class
from . import cart_class

@app.route("/", methods=['GET','POST'])
def homepage():

    return flask.render_template("index.html")

@app.route("/pets", methods=['GET','POST'])
def all_pets():
    pets_obj=pets_class.Pet()
    pet_list=pets_obj.get_all_pets()
    if flask.request.method=="POST":
        filter_country_id=int(flask.request.form['filter_country'])
        if -1<filter_country_id<10:
            pet_list_by_country=pets_obj.get_pets_by_country_id(filter_country_id)
            country_name=pets_class.get_country_by_id(filter_country_id)
            flask.flash(f"Your list has been filtered by the country {country_name}.")
            return flask.render_template("pets.html",pet_list=pet_list_by_country)
        else:
            flask.flash(f"Your list is not filtered.")
            return flask.render_template("pets.html",pet_list=pet_list)
    return flask.render_template("pets.html",pet_list=pet_list)


@app.route("/pet", methods=['GET','POST'])
def one_pet():
    global selected_pet
    global selected_pet_id
    pets_obj=pets_class.Pet()
    pet_list=pets_obj.get_all_pets()

    try:
        selected_pet_id=flask.request.form['view']
    except:
        if flask.request.method=="POST":
            add_obj=cart_class.Cart()
            if selected_pet not in add_obj.get_cart():
                add_obj.add_to_cart(selected_pet)
                flask.flash(f"{selected_pet['name']} was added to your cart!")
            return flask.redirect(flask.url_for('all_pets'))
    for pet in pet_list:
        if int(selected_pet_id)==int(pet['id']):
             selected_pet=pet



    return flask.render_template("pet.html",pet=selected_pet)

@app.route("/cart", methods=['GET','POST'])
def cart():
    cart_obj=cart_class.Cart()
    pets_in_cart=cart_obj.get_cart()
    total=cart_obj.get_total()
    return flask.render_template("cart.html",pet_list=pets_in_cart,total=total)

