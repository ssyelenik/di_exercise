# Exercise 1
cars_available=100
passengers_per_car=4
num_drivers=30
passengers_waiting=90

print("The number of cars available is:",cars_available)
print("The number of drivers registered today is:",num_drivers)
print("The number of empty cars today is:", cars_available-num_drivers)
print("The number of passangers that can be transported today is:",num_drivers*4)
print("The average number of passengers to put in each car is:", int(passengers_waiting/num_drivers))

# Exercise 2

letter=input("Please enter a letter: ")
if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u" or letter=="A" or letter=="E" or letter=="I" or letter=="O" or letter=="U":
    print("The letter is a vowel.")
else:
    print("The letter is a consonant.")


# Exercise 3

check_lower=0;
digit=0;
check_upper=0;
check_special=0;
check_length=0;

password=input("Please enter a password:")
while check_lower==0 and digit==0 and check_upper==0 and check_special==0 and check_length==0:

    if password.upper()==password:
        password=input("You must include at least one lowercase letter. Please enter a different password:")
        check_lower=0;
    else:
        check_lower=1;

    for x in password:
        if x.isdigit():
            digit=1
    if digit==0:
        password=input("You must include at least one digit. Please enter a different password:")
        

    if password.lower()==password:
        password=input("You must include at least one uppercase letter. Please enter a different password:")
        check_upper=0
    else:
        check_upper=1

    for z in password:
        if z=="$" or z=="#" or z=="@":
            check_special=1
    if check_special==0:
        password=input("You must include at least one special character ($, #, or @). Please enter a different password:")

            
    if len(password)<6 or len(password)>12:
        check_length=0
        password=input("Your password must be between 6 and 12 characters. Please enter a different password:")
    else:
        check_length=1
else:
  print("Your password was accepted!")
        
            
# Exercise 4
my_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
my_text.replace(" ", "")
length=len(my_text)
print("The length of the paragraph is",length)

# Exercise 5
my_paragraph=input("Try to enter a paragraph without the letter A in it:")
found_lower= "a" in my_paragraph
found_upper= "A" in my_paragraph

if found_lower or found_upper:
    print("You failed!")
else:
    my_paragraph.replace(" ", "")
    paragraph_len=len(my_paragraph)
    print("Congratulations! You wrote",paragraph_len,"without an A")
    
# Exercise 6
full_name=input("Please enter your full name:")
alert_num=0
space=0
check_caps=0
num=0

while num==0 or space>1 or check_caps==0:
    alert_num=0
    for x in full_name:
        if x.isdigit():
            alert_num=1
    if alert_num==1:
        full_name=input("Your name can't have any numbers in it. Please enter your name again:")
        num=0
    else:
        num=1
  
    space=0
    for y in full_name:
        if y==" ":
            space=space+1
    if space>1:
        full_name=input("Your name contains too many spaces. Please enter your name again:")
    

    if full_name!=full_name.title():
        full_name=input("Please capitalize the first letter of your first and last name. Enter your name again:")
        check_caps=0
    else:
        check_caps=1
else:
    print("Your name is valid.")
        






            
