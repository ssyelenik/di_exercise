import json
import flask

class Customer:

    def register_customer(self,first_name,last_name):
        with open("customer.json","r") as f:
            customers=json.load(f)
        if not customers:
            id=0
        else:
            id=len(customers)
        for customer in customers:
            if customer['first_name']==first_name and customer['last_name']==last_name:
                flask.flash("You are already a registered customer!")
                return customer['id']
        new_customer={'id':id,'first_name':first_name,'last_name':last_name}
        customers.append(new_customer)
        with open("customer.json","w") as f:
            json.dump(customers,f)
        return id

