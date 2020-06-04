##sampleDict = { 
##   "class":{ 
##      "student":{ 
##         "name":"Mike",
##         "marks":{ 
##            "physics":70,
##            "history":80
##         }
##      }
##   }
##}
##print(sampleDict["class"]["student"]["marks"]["history"])
##
##
##sampleDict2 = {
##  "name": "Kelly",
##  "age":25,
##  "salary": 8000,
##  "city": "New york"
##
##}
##keysToRemove = ["name", "salary"]
##
##del sampleDict2["name"]
##del sampleDict2["salary"]
##
##print(sampleDict2)


# Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary=dict(zip(keys,values))
print(dictionary)

# Exercise 2
store = {
    'name':'Zara',
    'creation_date':'1975',
    'creator_name':'Amanicio Ortega Gaona',
    'type_of_clothes': ['men','women','children','home'],
    'international_competitors':['Gap','H&M','Benetton'],
    'number_stores':7000,
    'major_color':{'France':'blue','Spain':'red','US':['pink','green']}
    }

# 1 Change the number of stores to 2
store['number_stores']=2

# 2 Print a sentence that explains who the clients of Zara are

# 3 Add country_creation: Spain to the dictionary (it’s a new key)
store['country_creation'] = 'Spain'


# 4 If the key international_competitors is in the dictionary, add the store Desigual
if store.get("international_competitors") != None:
    store['international_competitors'].append('Desigual')


# 5 Delete the information about the date of creation
del store["creation_date"]
print(store)

# 6 Print the last international competitor
print(store["international_competitors"][len(store["international_competitors"])-1])

# 7 Print in a sentence, the major colors in the US
print(store['major_color']['US'][0])
print(store['major_color']['US'][1])
print("The colors of the US are {} and {}." .format(store['major_color']['US'][0],store['major_color']['US'][1]))

# 8 Print the length of the dictionary
print("The length of the dictionary is: ",len(store))\

# 9 Print the keys of the dictionary
print(store.keys())

# 10 Create another dictionary called more_on_store with this information
more_on_store={"creation_date": "1975", 
                "number_stores": 10000}
store.update(more_on_store)
print(store)
print(store["number_stores"])

# Bonus

store["stores_worldwide"]={}


def addStore(country,number):
    if "stores_worldwide" in store.keys():
        store["stores_worldwide"].update( {country : number} )

store['_addStore'] = addStore
store['_addStore']("Israel",15)
print(store["stores_worldwide"])


    
