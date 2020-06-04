from datetime import date

def fix_missing(birth_date):
    while len(birth_date)<3:
        print("Invalid birth date.")
        birth_date=input_date()
    return birth_date
        

def input_date():
    raw_date=input("Enter your birth date in the format yyyy/mm/dd: ")
    birth_date=raw_date.split("/")
    birth_date=fix_missing(birth_date)
    return birth_date


def fix_non_digits(birth_date):
    print(birth_date[0],birth_date[1],birth_date[2])
    
    try:
        for index,item in enumerate(birth_date):
            birth_date[index]=int(birth_date[index])
        return birth_date
    except:
        print("Invalid birth date. Please reenter.")
        birth_date=input_date()
        fix_non_digits(birth_date)
        
    return(birth_date)

def ask_for_date():
    birth_date=input_date()
    print(birth_date[0],birth_date[1],birth_date[2])
 
    birth_date=fix_non_digits(birth_date)

        
    while birth_date[0]>2020 or birth_date[0]<1900:
        print("Invalid year. Enter your birthdate with a reasonable birth year")
        birth_date=input_date()
  
        birth_date=fix_non_digits(birth_date)

            
    while birth_date[1]>12 or birth_date[1]<1:
        print("Invalid month. Enter a birthdate with a reasonable birth month")
        birth_date=input_date()
 
        birth_date=fix_non_digits(birth_date)
    
    while birth_date[2]>31 or birth_date[2]<1:
        print("Invalid day. Enter your birth date with a reasonable birth day")
        birth_date=input_date()
 
        birth_date=fix_non_digits(birth_date)
        
    print(birth_date)
    return(birth_date)


def get_age(born):
    
    today = date.today()
    print(today)
    extra_year = 1 if ((today.month, today.day) < (born[1], born[2])) else 0
    
    return today.year - born[0] - extra_year

def can_retire(age,gender):
    if gender=="m":
        if age>=67:
            print("Congratulations! You can retire!")
        else:
            print("Sorry! You can't retire yet!")
    elif gender=="f":
        if age>=62:
            print("Congratulations! You can retire!")
        else:
            print("Sorry! You can't retire yet!")


    

gender=input("Enter your gender: (m or f) ")
gender.islower()
while not (gender=="m" or gender=="f"):
    gender=input("Invalid entry. Enter your gender: (m or f) ")

birth_date=ask_for_date()
print("in main",birth_date)
age=get_age(birth_date)

print("Your birth date is",birth_date,"and you are", age,"years old.")

can_retire(age,gender)


