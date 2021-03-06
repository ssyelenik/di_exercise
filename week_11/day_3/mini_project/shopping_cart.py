import flask as f
import shopping_cart_backend as scb
import json
import ast

buy_products=[]
shopping=f.Flask(__name__)
with open("products2.json","r") as file:
    test_dict=json.load(file)
print(test_dict)

@shopping.route("/homepage", methods=['GET','POST'])
def homepage():
##    if f.request.method=="POST":
##        search_items=[]
##        button=f.request.form
##        search_word=f.request.form['search_item']
##        if "search_item" in button:
##            available_products=scb.get_available_products()
##            for prod in available_products:
##                for key in prod:
##                    if search_word in key or search_word in prod[key]:
##                        search_items.append(prod)
##            if search_items=="":
##                pass
##            else:
##                num=len(search_items)
##                print("HERE")
##                return f.render_template('home.bin/view_search_products.html',search_products=search_items, num=num)
    return f.render_template("home.bin/homepage.html")

@shopping.route("/view_search_products", methods=['GET','POST'])
def view_search_products():
    global search_items
    global num
    global buy_products
    if f.request.method=="POST":
        
        button = f.request.form.to_dict()
        print(button)
        print(type(button))

        for keys in button:
            print("FINDING KEYS IN FORM")

            if keys=="search_item":
                search_items=[]
                search_word=f.request.form['search_item']
                available_products=scb.get_available_products()
                for prod in available_products:
                    for key in prod:
                        if search_word in key or search_word in prod[key]:
                            search_items.append(prod)
                if search_items=="":
                    return f.render_template("home.bin/homepage.html")
                else:
                    num=len(search_items)
        
            if keys=="view_product":
                print("VIEW PRODUCT BUTTON PRESSED")
                view_product=f.request.form['view_product'] 
                return f.render_template("home.bin/view_single_product.html",product=search_items[int(view_product)])

            elif keys=="buy_product":
                print("BUY PRODUCT BUTTON PRESSED")
                buy_product=f.request.form['buy_product']
                print("BUY PRODUCT BUTTON VAL",buy_product)
                
                try:
                    if search_items[int(buy_product)] not in buy_products:
                        buy_products.append(search_items[int(buy_product)])
                        print(buy_products)
                except:
                    buy_product=ast.literal_eval(buy_product)
                    if buy_product not in buy_products:
                        buy_products.append(buy_product)
    return f.render_template('home.bin/view_search_products.html',search_products=search_items, num=num)

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
                if available_products[int(buy_product)] not in buy_products:
                    buy_products.append(available_products[int(buy_product)])
            except:
                buy_product=ast.literal_eval(buy_product)
                if buy_product not in buy_products:
                    buy_products.append(buy_product)
        
    return f.render_template("home.bin/view_all_products.html",available_products=available_products, num=num)

@shopping.route("/view_single_product", methods=['GET','POST'])
def view_single_product(view_product):
    global buy_products
    if f.request.method=="POST":
        print(button)
        button = f.request.form
        if 'product_to_buy' in button:
            if buy_product not in buy_products:
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

@shopping.route("/add_products")
def add_products():
    return f.render_template("home.bin/add_products.html")

@shopping.route("/view_new_product",methods=['POST'])
def view_new_product():
    import flask as f
    global available_products
    available_products=scb.get_available_products()
    if f.request.method=="POST":
        print("HERE HRE RREER",f.request.method,f.request.form)
        product_id=f.request.form['product_id']
        category=f.request.form['category']
        description=f.request.form['description']
        name=f.request.form['name']
        ProductPicUrl=f.request.form['ProductPicUrl']
        status=f.request.form['status']
        print(product_id,category,description,name,ProductPicUrl,status)
        product_dict={
            "ProductId":product_id,
            "Category":category,
            "Description":description,
            "Name":name,
            "ProductPicUrl":ProductPicUrl,
            "Status":status
            }

        available_products.append(product_dict)

        with open("products.json","w") as file:
            json.dump(available_products,file)
            
    return f.render_template("home.bin/view_new_product.html",product=product_dict)
    
    
    
    
shopping.run()
