#Exercise 1
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

#Exercise 2
a=input("Enter a number:")
b=input("Enter another number:")

if int(a)>int(b):
    print("hello world")

#Exercise 3
month=input("Enter a month: (It must be a number between 1-12)")
if int(month)>=3 and int(month)<=5:
    print("It's Spring!")
elif int(month)>=6 and int(month)<=8:
    print("It's Summer!")
elif int(month)>=9 and int(month)<=11:
    print("It's Autumn!")
else:
    print("It's Winter!")
