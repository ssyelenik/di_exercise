import flask
import os
import json
from pathlib import Path
import random

class Pet():
    def get_all_pets(self):
        data_folder=Path("C:/BootCamp/di_exercise/week_12/day_2/ex_XP_Gold_Ninja.py/PetStore/")
        file_to_open=data_folder / "all_pets.json"
        with open(file_to_open,"r") as pet_file:
            all_pets=json.load(pet_file)
        return all_pets

    def get_one_pet(self,pet_id):
        all_pets=self.get_all_pets()
        for pet in all_pets["pets"]:
            if pet_id==pet['id']:
                return pet.update()


    def get_pets_by_country_id(self,filter_country_id):
        pet_list=self.get_all_pets()
        pet_by_country=[]
        for pet in pet_list:
            if filter_country_id==pet["country_id"]:
                pet_by_country.append(pet)
        print("pet by country",pet_by_country)
        return pet_by_country

def get_country_by_id(id):
    data_folder=Path("C:/BootCamp/di_exercise/week_12/day_2/ex_XP_Gold_Ninja.py/PetStore/")
    file_to_open=data_folder / "countries.json"
    with open(file_to_open,"r") as c:
            all_countries=json.load(c)
    for country in all_countries:
        if id==country['id']:
            country_name=country['name']
    return country_name

def assign_country():
    data_folder=Path("C:/BootCamp/di_exercise/week_12/day_2/ex_XP_Gold_Ninja.py/PetStore/")
    file_to_open=data_folder / "all_pets.json"
    with open(file_to_open,"r") as pet_file:
            all_pets=json.load(pet_file)
    new_all_pets=[]
    print(all_pets)
    for pet in all_pets:
        if 'country_id' not in pet.keys():
            pet['country_id']=random.randint(0,9)
        new_all_pets.append(pet)
    with open(file_to_open,"w") as pet_file:
            json.dump(new_all_pets,pet_file)
    return new_all_pets



pets_with_countries=assign_country()























pet=Pet()

