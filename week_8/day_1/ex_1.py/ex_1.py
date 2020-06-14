# Exercise 1
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
    def make_list(*args):
        for item in args:
            cat_list.append(item)

        return cat_list

    
    def find_oldest(cat_list):
        oldest=0
        for i,x in enumerate(cat_list):
            if cat_list[i].age>oldest:              
                oldest=cat_list[i].age
        return oldest

        


cat1=Cat("Curly",1)
cat2=Cat("Tiger",10)
cat3=Cat("Sandwich",7)
cat_list=[]
cat_list=Cat.make_list(cat1,cat2,cat3)

oldest=Cat.find_oldest(cat_list)
print("Your oldest cat is {} years old.".format(oldest)) 

# Exercise 2

class Dog:
    def __init__(self,nameDog,heightDog):
        self.name=nameDog
        self.height=heightDog

    def talk(self):
        print("Woof!")

    def jump(self):
        print("{}'s height when he jumps is {}.".format(self.name,self.height*2))

Davids_dog=Dog("Rex",50)
Davids_dog.talk()
Davids_dog.jump()

Sarahs_dog=Dog("Teacup",20)
Sarahs_dog.talk()
Sarahs_dog.jump()

if Davids_dog.height>Sarahs_dog.height:
    Davids_dog.winner=True
    Sarahs_dog.winner=False
elif Sarahs_dog.height>Davids_dog.height:
    Davids_dog.winner=False
    Sarahs_dog.winner=True
elif Sarahs_dog.height==Davids_dog.height:
    Davids_dog.winner=True
    Sarahs_dog.winner=True

print(Davids_dog.winner, Sarahs_dog.winner)

# Exercise 3
class Zoo:
    def __init__(self,zoo_name):
        self.animals=[]
        self.name=zoo_name

    def add_animal(self,new_animal):
        if new_animal in self.animals:
            print("{}s are already included in your list.".format(new_animal))
        else:
            self.animals.append(new_animal)
            
    def get_animals(self):
        print("These are the animals in the zoo, {}:".format(self.name))
        for x in self.animals:
              print(x)
            
    def animal_sold(self,animal_sold):
        print("Goodbye, {}. You were sold.".format(animal_sold))
        self.animals.remove(animal_sold)

    def sort_animals(self):
        pens={}
        group=[]
        for first,x in enumerate(self.animals):
            x.lower()
            for second,y in enumerate(self.animals):
                y.lower()
                if not x==y:
                    if y>x:
                        self.animals[first]=y
                        self.animals[second]=x
                        break
        z=0
        last="no"
        pen_num=1
        while z<len(self.animals):
            group.append(self.animals[z])
            if z<len(self.animals)-1 and not self.animals[z][0]==self.animals[z+1][0]:
                last="yes"
            elif z==len(self.animals)-1:
                last="yes"
            if last=="yes":
                pens.update({pen_num:[group]})
                group=[]
                last="no"
                pen_num+=1
            z+=1
            
        return pens

    def get_pen(self,pens):
        for key,value in pens.items():
            print(key,value)
  
        
biblical_zoo=Zoo("Biblical Zoo")
biblical_zoo.add_animal("bear")
biblical_zoo.add_animal("ape")
biblical_zoo.add_animal("baboon")
biblical_zoo.add_animal("lion")

biblical_zoo.get_animals()

biblical_zoo.animal_sold("lion")

biblical_zoo.get_animals()

biblical_zoo.sort_animals()

biblical_zoo.get_animals()

pens=biblical_zoo.sort_animals()

biblical_zoo.get_pen(pens)


    
        


