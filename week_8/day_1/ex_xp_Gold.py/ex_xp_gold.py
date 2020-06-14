# Exercise 1

class Circle:
    def __init__(self,radius=1.0):
        self.radius=radius
        self.circumference=self.get_circumference()
        self.area=self.get_area()

    def get_circumference(self):
        import math
        return 2*math.pi*self.radius

    def get_area(self):
        import math
        return math.pi*self.radius**2

    def print_equasion(self,x_coordinate,y_coordinate):
        op_x="-"
        op_y="-"
        if x_coordinate<0:
            x_coordinate=-1*x_coordinate
            op_x="+"
        if y_coordinate<0:
            y_coordinate=-1*y_coordinate
            op_y="+"
        print("(x{}{})^2 + (y{}{})^2 = {}".format(op_x,x_coordinate,op_y,y_coordinate,self.radius**2))


cir=Circle(3)

print(cir.radius,cir.circumference,cir.area)

cir.print_equasion(7,-2)



# Exercise 2

class MyList:
    def __init__(self,temp_list):
        self.stuff=temp_list.split(" ")

    def reverse(self):
        reverse_list=[]
        i=len(self.stuff)-1
        while i>=0:
            reverse_list.append(self.stuff[i])
            i-=1
        return reverse_list

    def get_sorted(self):
        sorted_list=sorted(self.stuff)
        return sorted_list
            

temp=[]
temp=input("Enter a list or items separated by a space: ")
while not temp:
    temp=input("Empy list. Please enter a list or items separated by a space: ")
    
my_list=MyList(temp)
print(my_list.stuff)

print(my_list.reverse())

print(my_list.get_sorted())


# Exercise 3

class QuantumParticle:
    def __init__(self,position_x,momentum_y):
        self.position_x=position_x
        self.momentum_y=momentum_y
        self.spin_p=self.get_spin()

    def get_position(self):
        import random
        self.position_x=random.randint()
        print("Quantum Interferences!!")
        
    def get_momentum(self):
        import random
        self.position_y=random.random()
        print("Quantum Interferences!!")

    def get_spin(self):
        import random
        choice=random.randint(1,2)
        if choice==1:
            get_spin=self.spin_p=-1/2
        if choice==2:
            get_spin=self.spin_p=1/2
        return get_spin

    def entangle(self,p2):
        p2.spin_p=-(self.spin_p)
        print("Spooky Action at a Distance !!")

p1=QuantumParticle(position_x=1,momentum_y=5.0)
p2=QuantumParticle(position_x=2,momentum_y=5.0)

print(p1.position_x,p1.momentum_y,p1.spin_p)
print(p2.position_x,p2.momentum_y,p2.spin_p)

try:
    p1.entangle(p2)
except Exception as e:
    print("Invalid class.", str(e))

print(p1.position_x,p1.momentum_y,p1.spin_p)
print(p2.position_x,p2.momentum_y,p2.spin_p)

