from abc import ABC, abstractmethod
class Temperature(ABC):
    def __init__(self,temperature,version):
        self.temperature=temperature
        self.version=version

    def temp_to(self,to_version):
        pass

    def __repr__(self,new_temp,version):
        return "{} degrees {} in {} is {}".format(self.temperature,self.version,version,new_temp)


class Celsius_Conversions(Temperature):
    def __init__(self,temperature,version):
        super().__init__(temperature,version)

    def temp_to(self,to_version):
        if to_version=="kelvin":
            degree = self.temperature + 273.15
        if to_version=="farenheit":
            degree = (self.temperature * 9/5) + 32
        print(self.__repr__(degree,to_version))

class Kelvin_Conversions(Temperature):
    def __init__(self,temperature,version):
        super().__init__(temperature,version)

    def temp_to(self,to_version):
        if to_version=="celcius":
            degree = self.temperature - 273.15
        if to_version=="farenheit":
            degree = self.temperature * 9/5 - 459.67
        print(self.__repr__(degree,"farenheit"))

class Farenheit_Conversions(Temperature):
    def __init__(self,temperature,version):
        super().__init__(temperature,version)

    def temp_to(self,to_version):
        if to_version=="kelvin":
            degree = (self.temperature + 459.67) * 5/9
        if to_version=="celcius":
            degree = (self.temperature - 32) * 5/9
        print(self.__repr__(degree,"celcius"))

c=Celsius_Conversions(27,"celcius")
c.temp_to("kelvin")
c.temp_to("farenheit")

f=Farenheit_Conversions(72,"farenheit")
f.temp_to("kelvin")
f.temp_to("celcius")

k=Kelvin_Conversions(100,"kelvin")
k.temp_to("celcius")
k.temp_to("farenheit")

    
