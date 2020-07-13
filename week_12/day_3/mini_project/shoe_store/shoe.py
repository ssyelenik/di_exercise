import json

class Shoes:
    def get_shoes_per_city(self,city):

        shoe_list=[]

        with open ("inventory.json","r") as f:
            inventory=json.load(f)

        all_shoes=inventory['products']
        all_stores=inventory['stores']
        my_store=""
        for store in all_stores:
            if store['city']==city:
                my_store=store
        inventory=my_store['shoes_available']
        for shoe in inventory:
            if shoe['num available']>0:
                for shoe_details in all_shoes:

                    if shoe['id']==shoe_details['id']:
                        shoe['brand']=shoe_details['brand']
                        shoe['name']=shoe_details['name']
                        shoe['price']=shoe_details['price']
                        shoe['image']=shoe_details['image']
                        shoe_list.append(shoe)

        return shoe_list

    def get_shoe_details(self,id):
        with open ("inventory.json","r") as f:
            inventory=json.load(f)

        all_shoes=inventory['products']
        for shoe in all_shoes:
            if int(shoe['id'])==int(id):
                return shoe

    def update_inventory(self):

         with open ("inventory.json","r") as f:
             inventory=json.load(f)
         with open ("order.json","r") as g:
             orders=json.load(g)
         current_order=len(orders)-1
         order=orders[current_order]
         print("my order",order)
         cit=order['city']
         for i in range(len(inventory['stores'])):
             if inventory['stores'][i]['city']==cit:
                 ix=i
                 break
         print("found the right city in inventory:",inventory['stores'][i])
         for shoe in order['shoes']:
             shoe_id=shoe['id']
             amount=int(shoe['amount'])
             for x in range(len(inventory['stores'][ix]['shoes_available'])):
                 if inventory['stores'][ix]['shoes_available'][x]['id']==shoe_id:
                     ips=x
                     break
             print("found the shoe to update in inventory: ", inventory['stores'][ix]['shoes_available'][x])
             print("this is the shoe I bought: ",shoe)
             print("number of those shoes available   ", inventory['stores'][ix]['shoes_available'][ips]['id'],inventory['stores'][ix]['shoes_available'][ips]['num available'])
             inventory['stores'][ix]['shoes_available'][ips]['num available']-=amount
             print("updated amount",inventory['stores'][ix]['shoes_available'][ips]['num available'])

             if inventory['stores'][ix]['shoes_available'][ips]['num available']<0:
                 for products in inventory['products']:
                     if products['id']==inventory['stores'][ix]['shoes_available'][ips]['id']:
                         name=products['name']
                         break

                 return name

         with open ("inventory.json","w") as n:
             print("file open")
             json.dump(inventory,n)
         return "order_complete"






