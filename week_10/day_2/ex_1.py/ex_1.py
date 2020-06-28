# Exercise 1
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

print(sampleJson)

employee_info=json.loads(sampleJson)

print(employee_info["company"]["employee"]["payable"]["salary"])


# Exercise 2

person={"id" : 1, "name" : "value2", "age" : 29}
sampleJson2=json.dumps(person,sort_keys=True)


print(sampleJson2)
