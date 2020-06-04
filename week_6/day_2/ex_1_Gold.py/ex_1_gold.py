# Exercise 1
#student_details=[("Sharon",44,95), ("Abraham", 50, 87), ("Tim",19,66),("Francine", 16,80)]

raw_student_details = input("Enter a list in the following format: (name1,age1,score1),(name2,age2,score2):")
student_details = []

for tup in raw_student_details.split('),('):
    #tup looks like `(a,a` or `b,b`
    tup = tup.replace(')','').replace('(','')
    #tup looks like `a,a` or `b,b`
    single_student=tuple(tup.split(','))
    print(single_student)
    name,age,score=single_student
    
    age=int(age)
    score=float(score)
    single_student_fix=(name,age,score)
    student_details.append(single_student_fix)

print(student_details)




student_details_by_name=sorted(student_details)
print("Student details in alphabetical order:",student_details_by_name)
from operator import itemgetter
student_details_by_age=sorted(student_details, key=itemgetter(1))
print("Student details in age order:",student_details_by_age)
student_details_by_score=sorted(student_details, key=itemgetter(2))
print("Student details in score order:",student_details_by_score)


# Exercise 2

customer_name=input("Please enter the customer's name:")

waiter_name=input("Please enter the name of the waiter:")

item_name=input("Please enter the item ordered:")

item_price=input("Please enter the price of the item:")
item_price=float(item_price)

item_number=input("Please enter the number of items ordered:")
item_number=int(item_number)

item_discount=input("Please enter the percent discount:")
item_discount=int(item_discount)

bill=item_price*item_number*((100-item_discount)/100)
print("***********************************")
print("Customer name: {}" .format(customer_name))
print("Waiter name: {}" .format(waiter_name))
print("***********************************")
print("Item ordered: {}    Price: {}    Number of items: {}" .format(item_name,item_number,item_price))
print("Discount: {} %" .format(item_discount))
print("***********************************")
print("Your total, {}, is {}." .format(customer_name, bill))
print("***********Have a nice day!***************")


# Exercise 3
nums=input("Enter three numbers separated by commas:")

a, b, c = (int(x) for x in nums.split(','))
nums_list=(a,b,c)
nums_list=sorted(nums_list)
print("The numbers in order:",nums_list)
d,e,f=nums_list
print("The biggest number is:",f)

# Exercise 4

letter=input("Enter a letter in the alphabet:")
letter=letter.lower()
alphabet="abcdefghijklmnopqrstuvwxyz"
#check letter
while len(letter) != 1 or alphabet.count(letter)<1:
    letter=input("Invalid entry. Enter a letter in the alphabet:")
vowels="aeiou"
if vowels.count(letter)==1:
    print(letter,"is a vowel.")
else:
    print(letter,"is a consonant.")

# Exercise 5
import random
random_num=random.randint(1,9)
turns=0
check="no"
while turns<5 and check=="no":
    guess=input("Guess a number:")
    guess=int(guess)
    if guess==random_num:
        check="yes"
        print("You guessed the number! It's",random_num)
    else:
        if turns<5:
            print("Wrong number!")
        turns=turns+1
if check=="no":
    print("Sorry, you didn't guess the number. The number was",random_num)
          

# Exercise 6

for x in range(20):
  print(x+1)

# Exercise 7 & 8
million=[]
for z in range(1,1000001):
    million.append(z)

print(min(million))
print(max(million))
print(sum(million))

#for m in million:
#   print(m)
    
# Exercise 9
item_list=["red","orange","yellow","green","blue","purple","red","orange","yellow"]
index_list = [i for i, value in enumerate(item_list) if value == "orange"]
print("The list is:",item_list)
print("red is found in the following indeces:",index_list)

# Exercise 10
list_odd=[1,3,5,9,11]
list_even=[2,4,6,8,10]
done="no"
i=0
full_list=[]
while i<len(list_odd)+len(list_even):
    if i<len(list_odd):
        full_list.append(list_odd[i])
    else:
        full_list.append(list_even[i-(len(list_odd))])
    i=i+1
print("List of odd nums:",list_odd)
print("LIst of even nums:",list_even)
print("List of all nums:",full_list)
