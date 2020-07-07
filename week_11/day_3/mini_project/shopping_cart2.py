import flask as f
import shopping_cart_backend as scb
import json
import ast

buy_products=[]
shopping=f.Flask(__name__)

@shopping.route("/homepage", methods=['GET','POST'])
def homepage():
    if f.request.method=="POST":
        search_items=[]
        button=f.request.form
        search_word=f.request.form['search_item']
        if "search_item" in button:
            available_products=scb.get_available_products()
            for prod in available_products:
                for key in prod:
                    if search_word in key or search_word in prod[key]:
                        search_items.append(prod)
            if search_items=="":
                pass
            else:
                num=len(search_items)
                print("HERE")
                return f.render_template("home.bin/view_search_products.html",search_products=search_items, num=num)

    return f.render_template("home.bin/homepage.html")

@shopping.route("/view_search_products", methods=['GET','POST'])
def view_search_products(search_products,num):
##    print("MIRACLE HERE")
##    num=len(search_products)
##    print("***WEIRD HERE1***")
    if f.request.method=="POST":
##        print("***WEIRD HERE2***")
##        button = f.request.form
##        if "view_product" in button:
##            view_product=f.request.form['view_product'] 
##            return f.render_template("home.bin/view_single_product.html",product=search_products[int(view_product)])
##        elif "buy_product" in button:
##
##            buy_product=f.request.form['buy_product']
##            try:
##                buy_products.append(search_products[int(buy_product)])
##            except:
##                buy_product=ast.literal_eval(buy_product)
##                buy_products.append(buy_product)
##    print("NOW IT SHOULD OPEN IN VIEW SEARCH")
##    print(search_products)
            return f.render_template("home.bin/view_search_products.html",search_products=search_products, num=num)

@shopping.route("/view_all_products", methods=['GET','POST'])
def view_all_products():
    global available_products
    available_products=[]
    available_products=scb.get_available_products()
    global buy_products

    num=len(available_products)
    if f.request.method=="POST":
        button = f.request.form
        if "view_product" in button:
            view_product=f.request.form['view_product'] 
            return f.render_template("home.bin/view_single_product.html",product=available_products[int(view_product)])
        elif "buy_product" in button:
            buy_product=f.request.form['buy_product']
            try:
                buy_products.append(available_products[int(buy_product)])
            except:
                buy_product=ast.literal_eval(buy_product)
                buy_products.append(buy_product)
        
    return f.render_template("home.bin/view_all_products.html",available_products=available_products, num=num)

@shopping.route("/view_single_product", methods=['GET','POST'])
def view_single_product(view_product):
    global buy_products
    if f.request.method=="POST":
        button = f.request.form
        if 'product_to_buy' in button:
            
            product_to_buy=f.request.form['product_to_buy']
            buy_products.append(buy_product)
            
    return f.render_template("home.bin/view_single_product.html",product=view_product)

@shopping.route("/shopping_cart")
def shopping_cart():
    global buy_products
                         
    num=len(buy_products)
    if num==0:
        return f.render_template("home.bin/shopping_cart.html",message="You haven't selected any items yet.",num=num)
    else:
        return f.render_template("home.bin/shopping_cart.html",message="",buy_products= buy_products,num=num)


shopping.run()
