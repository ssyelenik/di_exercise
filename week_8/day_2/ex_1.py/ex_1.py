class Family:
    last_name="Smith"
    def __init__(self):
        self.dictionary=[{"Name":"Michael","Age":35,"Gender":"Male","Is_Child":False},{"Name":"Sarah","Age":32,"Gender":"Female","Is_Child":False}]

    def born(self, **kwargs):
        new_baby={}
        for key,value in kwargs.items():
            new_baby[key]=value
        self.dictionary.append(new_baby)
        print("Congratulations, {}!".format(self.dictionary[len(self.dictionary)-1]["Name"]))

    def is_18(self,name):
        for person in self.dictionary:
            if person["Name"]==name:
                if person["Age"]>18:
                    return True
                else:
                    return False           
        print("{} is not in the {} family.".format(name,Family.last_name))

    def __repr__(self):
        msg="MEMBERS OF THE {} FAMILY:".format(Family.last_name.upper())
        for person in self.dictionary:
            for key,value in person.items():
                if key=="Name":
                    msg="{}\n{}==>{}".format(msg,key,value)
                else:
                    msg="{}\n   {}==>{}".format(msg,key,value)
            msg="{}\n".format(msg)
        return msg

class TheIncredibles(Family):
    last_name=""
    def __init__(self,name):
        self.dictionary=[]
        TheIncredibles.last_name=name
        Family.last_name=name
            
    def add(self,**kwargs):
        new_person={}
        for key,value in kwargs.items():
            new_person[key]=value
        self.dictionary.append(new_person)

    
    def __repr__(self):
        msg="MEMBERS OF THE {} *INCREDIBLE* FAMILY:".format(TheIncredibles.last_name.upper())
        for person in self.dictionary:
            for key,value in person.items():
                if key=="Name":
                    msg="{}\n{}==>{}".format(msg,key,value)
                elif key=="Power":
                    msg="{}\n***{}***==>***{}***".format(msg,key,value)
                elif key=="Incredible_Name":
                    msg="{}\n***{}***==>***{}***".format(msg,key,value)
                else:
                    msg="{}\n   {}==>{}".format(msg,key,value)
            msg="{}\n".format(msg)
        return msg    


family_smith=Family()
family_smith.born(Name="Sam", Age=0, Gender="Male", Is_Child=True)

print(Family.__repr__(family_smith))

family_par=TheIncredibles("Par")
family_par.add(Name="Bob", Age=35, Gender="Male", Is_Child=False, Power="Super strong", Incredible_Name="Mr. Incredible")
family_par.add(Name="Helen", Age=32, Gender="Female", Is_Child=False, Power="Re-shape", Incredible_Name="Elastigirl")
family_par.add(Name="Violet", Age=14, Gender="Female", Is_Child=True, Power="Invisible", Incredible_Name="Vi")

family_par.born(Name="John", Age=0, Gender="Male", Is_Child=True, Power="Unknown Power", Incredible_Name="Jack")

print(Family.__repr__(family_par))
print(TheIncredibles.__repr__(family_par))


