import flask
from datetime import date,timedelta
from . import app
from . import shoe
from . import pages
from . import order as o
from . import employee
from . import customer
import json

@app.route("/", methods=['GET','POST'])
def homepage():
    return flask.render_template("homepage.html")


@app.route("/main", methods=['GET','POST'])
def main():
    global shoe_list
    global start_order
    try:
        filter_city=flask.request.form['filter_city']
        print("filter city",filter_city)
        start_order=o.Order()
        start_order.start(filter_city)
        shoes=shoe.Shoes()
        shoe_list=shoes.get_shoes_per_city(filter_city)
    except:
        pass
    if flask.request.method=="POST":
        try:
            amount=flask.request.form['amount']
            shoe_id=flask.request.form['shoe_id']
            start_order.add_shoe(amount,shoe_id)
        except:
            pass
    return flask.render_template("main.html",shoe_list=shoe_list)

@app.route("/order", methods=['GET','POST'])
def order():
    current_order=o.Order()
    shoe_details=current_order.get_shoes_ordered()
    total=current_order.calc_total(shoe_details)
    current_order.record_total(total)
    if flask.request.method=="POST":
        try:
            button=flask.request.form['confirm']
            return flask.redirect(flask.url_for('confirm_order'))
        except:
            pass
        try:
            button=flask.request.form['cancel_order']
            if button=="cancel_order":
                current_order.cancel_order()
                flask.flash("Your order was canceled. Start a new one!")
                return flask.render_template("homepage.html")
        except:
            pass
    return flask.render_template('order.html',shoe_details=shoe_details,total=total)


@app.route("/confirm_order",methods=['GET','POST'])
def confirm_order():
    form=pages.confirm_order()
    # if form.validate_on_submit():
    #     first_name=form.first_name.data
    #     last_name=form.last_name.data

    if flask.request.method=="POST":
        try:
            butt=flask.request.form['confirm']
            first_name=flask.request.form['first_name']
            last_name=flask.request.form['last_name']
            cust=customer.Customer()
            cust_id=cust.register_customer(first_name,last_name)
            ord=o.Order()
            ord.add_customer(cust_id)
            sho=shoe.Shoes()
            order_complete=sho.update_inventory()
            print(order_complete)
            if not order_complete=="order_complete":
                flask.flash(f"Your order did not go through because you exceeded the number of {order_complete}s available in your city")
                flask.flash("Start a new order!")

            else:
                today=date.today()
                delivery = date.today() + timedelta(days=5)
                flask.flash(f"Your order was placed! It will arrive by {delivery}.")
                flask.flash("Start a new order!.")
            print("ready to render homepage")
            return flask.redirect(flask.url_for('homepage'))
        except:
            pass

        try:
            butt=flask.request.form['cancel_order']
            ord=o.Order()
            ord.cancel_order()
            flask.flash("Your order was canceled. Start a new one!")
            return flask.render_template("homepage.html")
        except:
            pass

    return flask.render_template('confirm_order.html',form=form)

@app.route("/employee_sign_in",methods=['GET','POST'])
def employee_sign_in():
    form=pages.employee_sign_in()
    if flask.request.method=="POST":
        all_orders=o.get_orders()
        password=flask.request.form['password']
        empl=employee.Employee()
        status=empl.get_status(password)
        if status=="invalid_employee":
            flask.flash("Invalid employee password.")
            return flask.redirect(flask.url_for('homepage'))
        if status=="employee":
            return flask.redirect(flask.url_for('employee_view'))
        elif status=="admin":
            return flask.redirect(flask.url_for("admin_view"))
    return flask.render_template('employee_sign_in.html',form=form)

@app.route("/employee_view",methods=['GET','POST'])
def employee_view():
    all_orders=o.get_orders()
    return flask.render_template('employee_view.html',all_orders=all_orders)

@app.route("/admin_view",methods=['GET','POST'])
def admin_view():
    all_orders=o.get_orders()
    return flask.render_template("admin_view.html",all_orders=all_orders)
