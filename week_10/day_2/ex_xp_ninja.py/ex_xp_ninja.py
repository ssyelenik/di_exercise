import re
nums=re.findall(r'\d+', 'hello 42 I\'m a 32 string 30')
print(nums)


# Exercise 2

class SpaceAge:
    def __init__(self,seconds):
        self.seconds=seconds
        self.earth_year=31557600.0
        self.periods={
            "Earth":1,
            "Mercury":0.2408467,
            "Venus":.061519726,
            "Mars":1.8808158,
            "Jupiter":11.862615,
            "Saturn":29.447498,
            "Uranus":84.016846,
            "Neptune":164.79132,
            }

    def calc_age(self,planet):
        age=self.seconds/(self.earth_year*self.periods[planet])
        self.planet=planet
        return age

me=SpaceAge(1387584000)

my_age=me.calc_age("Mercury")
print("You are {} years old on {}.".format(my_age,me.planet))


# Exercise 3
import random
class Character:
    def __init__(self):
        self.abilities={
            "strength":0,
            "dexterity":0,
            "constitution":0,
            "intelligence":0,
            "wisdom":0,
            "charisma":0
            }

class Game(Character):
    def __init__(self):
        super().__init__()
        for key in self.abilities:
            self.set_ability(key)
            
    def set_ability(self,ability):
        roll=[]
        for i in range(4):
            temp=(self.roll_dice())
            print("You rolled a {}!".format(temp))
            roll.append(temp)
        lowest_roll,lowest_ix=self.get_lowest(roll)
        print("Your lowest roll was {}.".format(lowest_roll))
        roll.pop(lowest_ix)
        power=self.calc_power(roll)
        print("The sum of your other three rolls is {}.".format(power))
        self.abilities[ability]=power
        print("The value of your {} ability is {}.".format(ability,self.abilities[ability]))

    def roll_dice(self):
        roll=random.randint(1,6)
        return roll

    def get_lowest(self,roll):
        lowest_roll=6
        for x in range(4):
            if roll[x] < lowest_roll:
                lowest_roll=roll[x]
                lowest_ix=x
        return lowest_roll,lowest_ix
    
    def calc_power(self,roll):
        sum_rolls=0
        for z in range(3):
            sum_rolls+=roll[z]
        return sum_rolls
            

Mikey=Game()



            
        
            
            
