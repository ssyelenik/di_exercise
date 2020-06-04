# Exercise 2 & 3 

birthdays={"Daniel":"1970/06/06",
           "Tzvia":"1996/11/17",
           "Shiffy":"1998/09/30",
           "Chaim":"2002/04/24",
           "Shira":"2005/05/29",
           "Hadassah":"2005/05/29",
           "Yosef":"2012/05/30"}

print("Welcome! You can look up the birthday of the people in the list!")

new_name=input("Enter a new name for the dictionary: ")
new_birthday=input("Enter that person's birthday in the format YYYY/MM/DD: ")

birthdays.update({new_name:new_birthday})

print("Here's our list of names:")
for t in birthdays:
    print(t)
    
search=input("Which person’s birthday do you want to see? ")
found=""
for key in birthdays:
    if search==key:
        found=birthdays[key]
        break
if not found=="":
    print(search+"'s birthday is",found)
else:
    print(search,"is not listed in our directory.")

# Exercise 4
i=0
num_list=[]
while i<10:
    num=input("Enter a number between -100 and 100: ")
    num=int(num)
    valid_num="no"
    while valid_num=="no":
        try:
            int(num)
            valid_num="yes"
        except:
            num=input("Invalid entry. Enter a number between -100 and 100: ")
            num=int(num)
    
    while num<-100 or num>100:
        num=input("Invalid entry. Enter a number between -100 and 100: ")
        num=int(num)
    num_list.append(num)
    i=i+1

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

average=sum(num_list)/10
print("The average of the numbers is:",average)
sorted_list=sorted(num_list)
print("The largest number is:",sorted_list[len(sorted_list)-1])
print("The smallest number is:",sorted_list[0])
        
        
             
