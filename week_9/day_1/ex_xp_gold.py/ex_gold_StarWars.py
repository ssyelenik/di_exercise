from abc import ABC, abstractmethod
import random
class ForceWielder:

    def __init__(self,name):
        self.name=name
        self.power=random.randint(0,16)
        self.wisdom=random.randint(0,16)

    @abstractmethod
    def train(self):
        pass

    def fight_method(self,other):
        print("")
        if self.power==0 or self.wisdom==0:
            return other
        if other.power==0 or other.wisdom==0:
            return self
        self_harmonic_mean=2/((1/self.power)+(1/self.wisdom))
        other_harmonic_mean=2/((1/other.power)+(1/other.wisdom))
        if self.is_jedi()==True:
            print("Jedi {} has {} power points and {} wisdom points.".format(self.name,self.power,self.wisdom))
            print("Sith {} has {} power points and {} wisdom points.".format(other.name,other.power,other.wisdom))
            print("The score is Jedi {}: {} vs. Sith {}: {}!".format(self.name,self_harmonic_mean,other.name,other_harmonic_mean))
        else:
            print("Jedi {} has {} power points and {} wisdom points.".format(other.name,other.power,other.wisdom))
            print("Sith {} has {} power points and {} wisdom points.".format(self.name,self.power,self.wisdom))
            print("The score is Jedi {}: {} vs. Sith {}: {}!".format(other.name,other_harmonic_mean,self.name,self_harmonic_mean))
        if self_harmonic_mean>other_harmonic_mean:
            return self
        else:
            return other

    @abstractmethod
    def is_jedi(self):
        pass

class Jedi(ForceWielder):

    def __init__(self,name):
        super().__init__(name)
        self.wisdom+=10
        if self.wisdom>self.power:
            self.lightsaber_color="green"
        if self.wisdom<self.power:
            self.lightsaber_color="blue"
        if self.wisdom==self.power:
            self.lightsaber_color="violet"

    def train(self):
        self.wisdom+=random.randint(10,20)
        self.power+=random.randint(5,15)
        print("Jedi {} has {} power points and {} wisdom points.".format(self.name,self.power,self.wisdom))            

    def is_jedi(self):
        return True

class Sith(ForceWielder):

    def __init__(self,name):
        super().__init__(name)
        self.name="Darth "+self.name
        self.lightsaber_color="red"
        self.power+=10

    def train(self):
        self.wisdom+=random.randint(5,15)
        self.power+=random.randint(10,20)
        print("Sith {} has {} power points and {} wisdom points.".format(self.name,self.power,self.wisdom))

    def is_jedi(self):
        return False


