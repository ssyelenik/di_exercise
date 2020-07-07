import json

def get_available_products():
    with open("products.json","r") as f:
        db_products=json.load(f)
    available_products=[]
    product_details={}
    for product in db_products:
        if product["Status"]=="Available":
            product_details={"ProductId":product["ProductId"],
                             "Category":product["Category"],
                             "Name":product["Name"],
                             "Description":product["Description"],
                             "ProductPicUrl":product["ProductPicUrl"],
                             "Status":"Available"
                             }
        available_products.append(product_details)                 
    return available_products

def get_selected_item():
    pass

def see_shopping_cart():
    pass


