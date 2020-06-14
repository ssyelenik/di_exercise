# Exercise 1
class MenuManager:
    def __init__(self,name,price,spice_level,gluten_index):
        temp_menu={"Name":name,"Price":price,"Spice Level":spice_level,"Gluten Index":gluten_index}
        self.menu=[]
        self.menu.append(temp_menu)


    def add_item(self,name,price,spice_level,gluten_index):
        temp_menu={"Name":name,"Price":price,"Spice Level":spice_level,"Gluten Index":gluten_index}
        self.menu.append(temp_menu)

    def update_item(self,nname,nprice,nspice,ngluten):
        save_index=self.found_item(nname)
        if save_index==-1:
            print("The menu doesn't contain {}.".format(nname))
        else:
            self.menu[save_index]["Name"]=nname
            self.menu[save_index]["Price"]=nprice
            self.menu[save_index]["Spice Level"]=nspice
            self.menu[save_index]["Gluten Index"]=ngluten

    def found_item(self,nname):
        found=-1
        for index,menu_item in enumerate(self.menu):            
            if menu_item["Name"]==nname:
                found=index
        return found

    def remove_item(self,name):
        save_index=self.found_item(name)
        if save_index==-1:
            print("The menu doesn't contain {}.".format(name))
        else: 
            del self.menu[save_index] 
        
        

Holy_Bagels=MenuManager("Soup",10,"B",False)

print(Holy_Bagels.menu)

Holy_Bagels.add_item("Iced Coffee",7,"A",True)

print(Holy_Bagels.menu)

Holy_Bagels.update_item("Iced Coffee",15,"A",False)

print(Holy_Bagels.menu)

Holy_Bagels.remove_item("Bread")

print(Holy_Bagels.menu)
