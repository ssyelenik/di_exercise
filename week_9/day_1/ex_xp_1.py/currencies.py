# Exercise 1
class Currency:
    def __init__(self,value,label):
        self.value=float(value)
        self.label=label

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def __repr__(self):
        return "* {}: {}".format(self.label,self.value)

    def __add__(self,other):
        if self.label==other.label:
            return self.value+other.value
        else:
            return "Error. Different currencies"

    def subtract(self,other):
        if self.label==other.label:
            return self.value-other.value
        else:
            return "Error. Different currencies"

    def multiply(self,other):
        if self.label==other.label:
            return self.value*other.value
        else:
            return "Error. Different currencies"

    def divide(self,other):
        if self.label==other.label:
            return self.value/other.value
        else:
            return "Error. Different currencies"


shekels=Currency(100,"shekels")
shekels2=Currency(50,"shekels")
dollars=Currency(25,"dollars")

print("string:",str(shekels))
print("int:",int(shekels2))
print(shekels.__repr__())
print("add:",shekels+shekels2)
print("subtract:",shekels.subtract(shekels2))
print("multiply:",shekels.multiply(shekels2))
print("divide:",shekels.divide(shekels2))
print(shekels.subtract(dollars))

print(Currency.__dict__.keys())

# Exercise 2

class Circle:
    def __init__(self,**characteristics):
        for key,value in characteristics.items():
            if key=="radius":
                self.radius=value
                self.diameter=2*value
            elif key=="diameter":
                self.diameter=value
                self.radius=value/2

    def get_area(self):
        import math
        return math.pi*self.radius**2

    def __repr__(self):
        msg=""
        make_cir=3
        for i in range(self.diameter):
            msg=msg+  " " *  int(self.radius-make_cir/2)  +   "*" * make_cir  + "\n"
            if i<self.radius:
                make_cir+=2
            else:
                make_cir-=2

        return msg  

c1=Circle(radius=8)
print(c1.radius,c1.diameter)
print(c1.get_area())
print(repr(c1))
        

        
