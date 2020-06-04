friends={"Shira":37,"Bina":16,"Zelda":41}
print(friends)


nums={0: 10, 1: 20}
nums.update({2:30})
print("The dictionary is populated by: ",nums)

all_values = nums.values()
max_value = max(all_values)

print("The maximum value is: ",max_value)

min_value=min(all_values)
print("The minimum value is: ", min_value)


products = {
"SMART WATCH": 550,
"PHONE" : 1000,
"PLAYSTATION": 500,
"LAPTOP" : 1550,
"MUSIC PLAYER" : 600,
"TABLET" : 400
}

for key in products:
    print(key,products[key])



samples_antibiotics_with_duplicates = {'S00541-09': ['Streptomycin', 'Sulfamethoxazole', 'Trimethoprim', 'Spectinomycin', 'Streptomycin', 'Streptomycin', 'Trimethoprim']}
print(samples_antibiotics_with_duplicates)
new_dict = {a:list(set(b)) for a, b in samples_antibiotics_with_duplicates.items()}
print(new_dict)


new_key="IPAD"
check="no"
for k in products:
    if new_key==k:
        check="yes"
if check=="yes":
    print("The key is already in use.")
else:
    print("Your key is unique.")



dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}

full_dic={**dic1,**dic2,**dic3}
print(full_dic)



list1 = ['Rick', 'Donald', 'Mickey' , 'Mario']
list2 = ['Sanchez', 'Duck', 'Mouse', 'Kart']
print(list1)
print(list2)

full_names={}
for k in list1:
    i=list1.index(k)
    z=list2[i]
    full_names.update({k:z})
print(full_names)
    
money=input("How much money do you have?")
money=int(money)
affordable_items=[]
for key in products:
    if products[key]<=money:
        affordable_items.append(key)
print("These are the items you could afford:",affordable_items)



number=input("Enter a number: ")

for digit in number:
    if digit=="0":
        print("zero ", end="", flush=True)
    if digit=="1":
        print("one ", end="", flush=True)
    if digit=="2":
        print("two ", end="", flush=True)
    if digit=="3":
        print("three ", end="", flush=True)
    if digit=="4":
        print("four ", end="", flush=True)
    if digit=="5":
        print("five ", end="", flush=True)
    if digit=="6":
        print("six ", end="", flush=True)
    if digit=="7":
        print("seven ", end="", flush=True)
    if digit=="8":
        print("eight ", end="", flush=True)
    if digit=="9": 
        print("nine ", end="", flush=True)

print("")

times=input("How many numbers should be printed? ")
times=int(times)
squares={}
for b in range(times):
    squares.update({b+1:(b+1)**2})
print(squares)




contacts={"Mario":"0512345678",
"John":"0542815674",
"Eyal":"0586878399"}

contacts.update({"Sharon":"0548402685"})

for k in contacts:
    print(k,contacts[k])

found="no"
phone_num="0548402675"
for z in contacts:
    if contacts[z]==phone_num:
        print(z)
        found="yes"
        break
if found=="no":
    print("We don't have that number.")

count=0
for h in contacts:
    count=count+1


print("There are",count,"contacts in your directory.")


for w in sorted(contacts):
    print(w,contacts[w], end=" ")
print("")


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d_combined={}
for key1 in d1:
    match="no"
    for key2 in d2:
        if key1==key2:
            d_combined.update({key1:d1[key1]+d2[key2]})
            match="yes"
            break
    if match=="no":
        d_combined.update({key1:d1[key1]})


for place2 in d2:
    found="no"
    for place1 in d1:
        if place2==place1:
            found="yes"
            break
    if found=="no":
        d_combined.update({place2:d2[place2]})

print("")
print(d1)
print(d2)
print(d_combined)

    
        
            
            
    
    
    

    

