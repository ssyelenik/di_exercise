import datetime
birthdays={"Daniel":"1970/06/06",
           "Tzvia":"1996/11/17",
           "Shiffy":"1998/09/30",
           "Chaim":"2002/04/24",
           "Shira":"2005/05/29",
           "Hadassah":"2005/05/29",
           "Yosef":"2012/05/30"}

print("Welcome! You can look up the birthday of the people in the list!")
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
        
        
             
