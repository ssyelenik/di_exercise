# Exercise 1
fruit_string=input("Enter a list of your favorite fruits separated by a space: ")
fruit_string.lower()
fruit_list=fruit_string.split(" ")
i=0
fruit_format_list=[]
for k in fruit_list:
    if i<len(fruit_list)-1:
        fruit_format_list.append(k)
    elif i==len(fruit_list)-1:
        fruit_format_list.append("and")
        fruit_format_list.append(k)
    i=i+1
for g in fruit_format_list:
    print(g," ", end = "")
print("")
one_fruit=input("Enter the name of a fruit: ")
one_fruit.lower()
match="no"
for x in fruit_list:
    if x==one_fruit:
        match="yes"
        break
if match=="yes":
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it too!")
    
    
