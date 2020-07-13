import json
from . import shoe as sh

class Order():

    def start(self,city):
        orders=get_orders()
        id=len(orders)
        new_order={'order_id':id,'city':city,'shoes':[]}
        print("******Here in start the order",new_order)
        orders.append(new_order)
        with open("order.json","w") as f:
            json.dump(orders,f)

    def add_shoe(self,amount,shoe_id):
        orders=get_orders()
        current_order=len(orders)-1
        orders[current_order]['shoes'].append({'id':int(shoe_id),'amount':int(amount)})
        print(orders[current_order])
        with open("order.json","w") as f:
            json.dump(orders,f)

    def get_current_order(self):
        orders=get_orders()
        current_order=len(orders-1)
        return orders[current_order]

    def get_shoes_ordered(self):
        shoe_info=sh.Shoes()
        orders=get_orders()
        order_num=len(orders)-1
        current_order=orders[order_num]
        shoes_ordered=current_order['shoes']
        shoe_details=[]
        for shoe in shoes_ordered:
            one_shoe=shoe_info.get_shoe_details(shoe['id'])
            shoe['name']=one_shoe['name']
            shoe['image']=one_shoe['image']
            shoe['brand']=one_shoe['brand']
            shoe['price']=one_shoe['price']
            shoe_details.append(shoe)
        return shoe_details

    def calc_total(self,shoe_details):
        total=0
        for shoe in shoe_details:
            amount=int(shoe['amount'])
            cost_per_shoe=int(shoe['price'])
            total_per_shoe=amount*cost_per_shoe
            total+=total_per_shoe
        return total

    def cancel_order(self):
        orders=get_orders()
        print("in cancel order func")
        cancel=[]
        if len(orders)==1:
            cancel=[]
        if len(orders)>1:
            for i in range(len(orders)-1):
                cancel.append(orders[i])
        with open("order.json","w") as f:
            json.dump(cancel,f)

    def add_customer(self,id):
        orders=get_orders()
        current_order=len(orders)-1
        orders[current_order]['customer_id']=id
        with open("order.json","w") as f:
            json.dump(orders,f)

    def record_total(self,total):
        orders=get_orders()
        current_order=len(orders)-1
        orders[current_order]['total']=total
        with open("order.json","w") as f:
            json.dump(orders,f)



def get_orders():
    with open ("order.json","r") as f:
           orders=json.load(f)
    return orders








