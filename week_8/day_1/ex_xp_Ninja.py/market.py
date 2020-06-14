class Farm:
    def __init__(self,name):
        self.name=name
        self.animals={}
        import os
        print(" python",os.path.basename(__file__))
        print("{}'s farm".format(self.name))

    def add_animal(self,animal,num=2):
        if num>1:
            if animal!="sheep" and animal!="deer":
                animal=animal+"s"     
        temp_animals=animal,num
        self.animals.update({temp_animals})
        return len(self.animals)
        
    def get_info(self):
        get_animals=[]
        for key,value in self.animals.items():
            print("{:5}:{:>10}".format(key,value))
            get_animals.append(key)
        msg="E-I-E-I-O!"
        print("   {}".format(msg))

    def get_animal_types(self):
        temp_get_animals=[]
        for key,value in self.animals.items():
            temp_get_animals.append(key)
        get_animals=sorted(temp_get_animals)
        return get_animals

    def get_short_info(self):
        info_list=self.get_animal_types()
        info=""
        info=", ".join(info_list)
        print(info)
        print("{}'s farm has {}.".format(self.name,info))
        


macdonald=Farm("McDonald")
macdonald.add_animal("cow",5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat",12)

macdonald.get_info()

print(macdonald.get_animal_types())
macdonald.get_short_info()
        
