# Exercise 1
def get_random_temp(season):
    import random
    if season=="winter":
        random_temp=random.randint(-10,16)
    elif season=="spring":
        random_temp=random.randint(17,23)
    elif season=="summer":
        random_temp=random.randint(24,40)
    elif season=="fall":
        random_temp=random.randint(17,23)
    

    return random_temp




def main():
    season=input("What's the season? Enter winter, spring, summer, or fall: ")
    while not (season == "winter" or season == "spring" or season == "summer" or season == "fall"):
        season=input("Invalid entry. Please enter the season again: (winter, spring, summer, or fall) ")
    temp=get_random_temp(season)
    print("The temperature right now is",temp,"degrees Celsius.") 
    if temp<0:
        print("Brrr, that's freezing! Wear some extra layers today!")
    elif 0<temp<16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16<temp<23:
        print("This is sweater weather.")
    elif 24<temp<32:
        print("The weather is perfect!")
    elif 32<temp<40:
        print("Now it's really hot!")

main()

# Exercise 2
def throw_dice():
    import random
    roll=random.randint(1,6)

    return roll

def throw_until_doubles():
    num_rolls=0
    while True:
        roll1=throw_dice()

        roll2=throw_dice()

        num_rolls+=1
        if roll1==roll2:
            return num_rolls

def main():
    num_rolls=[]
    for i in range(0,100):
        num_rolls.append(throw_until_doubles())

    print("It took", sum(num_rolls), "rolls to throw 100 doubles.")
    print("It took an average of", float(sum(num_rolls)/100), "rolls to get each double.") 

main()


        
    
