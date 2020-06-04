import random
list_length=random.randint(50,500)
print(list_length)
i=0
num_list=[]
while i<list_length:
    num_list.append(random.randint(-100,100))
    i=i+1
##    num=input("Enter a number between -100 and 100: ")
##    num=int(num)
##    valid_num="no"
##    while valid_num=="no":
##        try:
##            int(num)
##            valid_num="yes"
##        except:
##            num=input("Invalid entry. Enter a number between -100 and 100: ")
##            num=int(num)
##    
##    while num<-100 or num>100:
##        num=input("Invalid entry. Enter a number between -100 and 100: ")
##        num=int(num)
##    num_list.append(num)
##    i=i+1



print("*********************************************")

print("Here's your list:",num_list)
print("This is the sum of the numbers:",sum(num_list))
print("The first element in the list is:",num_list[0],"and the last element is",num_list[len(num_list)-1])

num_list_unique=list(dict.fromkeys(num_list))
print("This is your list with no duplicates:",num_list_unique)
large_list=[]
small_list=[]
squared_list=[]
for x in num_list:
    if x>50:
        large_list.append(x)
    elif x<10:
        small_list.append(x)
    squared_list.append(x**2)

print("All the numbers larger than 50 are:",large_list)
print("All the numbers smaller than 10 are:",small_list)
print("All the numbers squared are:",squared_list)

average=sum(num_list)/list_length
print("The average of the numbers is:",average)
sorted_list=sorted(num_list)
print("The largest number is:",sorted_list[len(sorted_list)-1])
print("The smallest number is:",sorted_list[0])
        
