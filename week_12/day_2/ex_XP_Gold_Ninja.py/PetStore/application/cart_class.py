import flask
import os
import json
from pathlib import Path

class Cart():
    total=0;
    def add_to_cart(self,pet):
        data_folder=Path("C:/BootCamp/di_exercise/week_12/day_2/ex_XP_Gold_Ninja.py/PetStore/")
        file_to_open=data_folder / "cart.json"
        print(file_to_open)
        with open(file_to_open,"r") as c:
            cart_pets=json.load(c)
        cart_pets.append(pet)
        with open(file_to_open,"w") as c:
            json.dump(cart_pets,c)

    def get_cart(self):
        data_folder=Path("C:/BootCamp/di_exercise/week_12/day_2/ex_XP_Gold_Ninja.py/PetStore/")
        file_to_open=data_folder / "cart.json"
        with open(file_to_open,"r") as c:
            cart_pets=json.load(c)
        return cart_pets


    def get_total(self):
        cart_pets=self.get_cart()
        Cart.total=0
        for pet in cart_pets:
            Cart.total+=pet["price"]
        return Cart.total


