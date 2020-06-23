# Exercise 1
import datetime as dt
#print(dir(dt))

while True:
    try:
        birthday_str=input("What's your birthday? (Please enter in the format of YYYY MM DD) ")
        birthday=birthday_str.split(" ")
        birthday[0]=int(birthday[0])
        birthday[1]=int(birthday[1])
        birthday[2]=int(birthday[2])
        if 1900<birthday[0]<2021 and 0<birthday[1]<13 and 0<birthday[2]<32:
            break
    except:
        print("Invalid birthdate. Try again.\n")
        
birthdate = dt.date(birthday[0],birthday[1],birthday[2])
print("\nYour birthday is: {}".format(birthdate))
              
today=dt.date.today()

time_since_birth=today-birthdate
minutes=time_since_birth.total_seconds()/60

temp=str(time_since_birth)
time_since_birth=temp.split(",")
print("You were born {} ago.".format(time_since_birth[0]))
print("That is {} minutes ago.\n\n".format(minutes))

# Exercise 2

from faker import Faker
import random

fake=Faker()

languages=["English","French","Hebrew","Arabic","German","Japanese","Chinese","Amharic","Flemish","Swedish","Spanish"]
user=[]
for i in range(4):
    user.append({"name":fake.name(),"address":fake.address(),"languages_spoken":languages[random.randint(0,10)]})

for i in range(4):
    for key,value in user[i].items():
        print(key+":",value)
    print("")


# Exercise 3
from password_generator import PasswordGenerator

pwo = PasswordGenerator()

print("\n\n***Create Password***\n")
length=input("How long must the password be? (between 6 and 30) ")
try:
    length=int(length)
    if length<6 or length>30:
        print("Sorry, invalid length. The default length will be used: 8")
        length=8
except:
    print("Sorry, invalid length. The default length will be used: 8")
    length=8
        
pwo.minlen=length
pwo.maxlen=length

pwo.minnumbers=1
pwo.minuchars=1
pwo.minlchars=1
pwo.minschars=1

new_pwd=pwo.generate()
print("Your new password is: {}\nRemember to put in a safe place!".format(new_pwd))

#Test function
for i in range(100):
    req_len=random.randint(6,30)
    pwo.minlen=req_len
    pwo.maxlen=req_len

    pwo.minnumbers=1
    pwo.minuchars=1
    pwo.minlchars=1
    pwo.minschars=1

    new_pwd=pwo.generate()
    #new_pwd="12345$78z"
    print("Test password #{} is {}".format(i,new_pwd))
    
    #Test length
    if len(new_pwd)==req_len:
        print("The password meets the required length of {} chars.".format(req_len))
    else:
        print("Alert: The password does not meet the required length of {} chars.".format(req_len))

    #Test upper chars
    upper_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for index,x in enumerate(new_pwd):
        if x in upper_letters:
            print("The password has at least one upper case letter.")
            break
        if index==len(new_pwd)-1:
            print("Alert: The password does not have at least one upper case letter.")

    #Test lower chars
    lower_letters="abcdefghijklmnopqrstuvwxyz"
    for index,y in enumerate(new_pwd):
        if y in lower_letters:
            print("The password has at least one lower case letter.")
            break
        if index==len(new_pwd)-1:
            print("Alert: The password does not have at least one lower case letter.")

    #Test digits
    digits="0123456789"
    for index,z in enumerate(new_pwd):
        if z in digits:
            print("The password has at least one numeric char.")
            break
        if index==len(new_pwd)-1:
            print("Alert: The password does not have at least one numeric char.")

    #Test special chars
    special="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for index,a in enumerate(new_pwd):
        if a in special:
            print("The password has at least one special char.")
            break
        if index==len(new_pwd)-1:
            print("Alert: The password does not have at least one special char.")

    #Text all chars
    for index,f in enumerate(new_pwd):
        if not(f in upper_letters or f in lower_letters or f in digits or f in special):
            print("Alert: At least one character in the password is invalid.")
            break
        if index==len(new_pwd)-1:
            print("All characters in the password are valid.\n\n")
    

    
        
