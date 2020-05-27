# Exercise 0

# 1
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)

# 2
basket.remove("Blueberries")
print(basket)

# 3
basket.append("Kiwi")
print(basket)

# 4
basket.insert(0, "Apples")
print(basket)

#5
numApples=basket.count("Apples")
print("The number of apples in the basket is", numApples)

#6 & 7
basket.clear()
print("This is the empty basket:", basket)

# Excerise 1

# 1

my_fav_numbers=[2, 5, 12, 18, 24, 36]
print("My favorite numbers are:", my_fav_numbers)

# 2
my_fav_numbers.append(7)

my_fav_numbers.append(9)

print("All my favorite numbers are:", my_fav_numbers)

# 3
my_fav_numbers.pop()
print("My favorite numbers are except the last are:", my_fav_numbers)

# 4
friend_fav_numbers=[7,10,11,15,17]
print("My friend's favorite numbers are:", friend_fav_numbers)

#5
our_fav_numbers=my_fav_numbers+friend_fav_numbers
print("Our favorite numbers are:",our_fav_numbers)

# Exercise 2

my_best_numbers=(2, 5, 12, 18, 24, 36)
print("My favorite tuple numbers are:", my_best_numbers)

# 2
temp_best_numbers=(7,9)

my_best_numbers1=my_best_numbers+temp_best_numbers


print("All my favorite tuple numbers are:", my_best_numbers1)

# 3

best_num1, best_num2, best_num3, best_num4, best_num5, best_num6, best_num7, best_num8=my_best_numbers1
my_best_numbers2=(best_num1, best_num2, best_num3, best_num4, best_num5, best_num6, best_num7)
print("All my favorite tuple numbers except the last are:", my_best_numbers2)

# 4
friend_best_numbers=(7,10,11,15,17)
print("My friend's favorite tuple numbers are:", friend_best_numbers)

#5

our_best_numbers=my_best_numbers2+friend_best_numbers
print("Our favorite tuple numbers are:",our_best_numbers)

#our_fav_numbers=my_fav_numbers+friend_fav_numbers
#print("Our favorite numbers are:",our_fav_numbers)

# Exercise 3
#2
float_sequence=[float(1.5), float(2), float(2.5), float(3), float(3.5), float(4), float(4.5), float(5)]
print("Floating sequence:",float_sequence)

#4
generate_float=[float(1.5),]
i=1

while(i<8):
    generate_float.append(generate_float[i-1]+float(.5))
    i+=1
else:
    print("The generated floating sequence is:",generate_float)
    

# Exercise 6

family=["Daniel","Sharon","Shimon","Tzvia","Shiffy","Chaim","Shira","Hadassah","Yosef"]
for member in family:
    print(member)


# Exercise 7
yes_no="yes"
cost=0
while(yes_no=="yes"):
    age=input("How old is this member of your family?")
    age=int(age)
    if age>=3 and age<=12:
        print("The ticket is $10")
        cost+=10
    elif age>12:
        print("The ticket is $15")
        cost+=15
    else:
        print("The ticket is free")
    yes_no=input("Is there another family memeber to input? Please enter yes or no.")
    while yes_no.lower()!="yes" and yes_no.lower()!="no":
        print("Invalid entry. Please enter again.")
        yes_no=input("Is there another family memeber to input? Please enter yes or no.")
print("The cost of tickets for the entire family is:",cost)

    
# Exercise 8

even_list=[4, 7, 9, 16, 27, 33, 45, 38, 77, 24]
i=0
while i<len(even_list)-1:
    if i%2==0:
        print(even_list[i])
    i=i+1

# Exercise 9
yes_no="yes"
temp_name=""
allowed_list=[]
while yes_no=="yes":
    temp_name=input("What's your name?")
    age=input("How old are you?")
    age=int(age)
    if age>16 and age<21:
        print("You are allowed to see the movie.")
        allowed_list.append(temp_name)
    else:
        print("You are not allowed to see the movie.")
    yes_no=input("Is there another customer who wants to watch the movie? Please enter yes or no.")
    while yes_no.lower()!="yes" and yes_no.lower()!="no":
        print("Invalid entry. Please enter again.")
        yes_no=input("Is there another family memeber to input? Please enter yes or no.")
print("The following teenagers are allowed to see the movie",allowed_list)
