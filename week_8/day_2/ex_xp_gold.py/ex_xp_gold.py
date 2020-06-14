# Exercise 1
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pets.animals.append(self.name)

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self,sounds):
        return f'{sounds}'

Benji=Bengal("Benji",2)
Cookie=Chartreux("Cookie",3)
Martha=Siamese("Martha",1)

my_cats=[Benji,Cookie,Martha]

for i in my_cats:
    print(i.sing("WOOOH"))

print(Pets.animals)

# Exercise 2

class Bank:
    accounts=[]
    bank_total=0

    def _init_(self,name):
        self.name=name

    def check_capacity():
        if len(Bank.accounts)>10:
            print("A new account could not be created.")
        else:
            return "not_full"

    def check_activities(type,owner,amount):
        if type=="new_account":
            Bank.bank_total+=amount
            print("A new account has been created by {}.\nAn additional {} has been added to the bank total.\nThe current amount of money in the bank is {}.\n".format(owner,amount,Bank.bank_total))
        elif type=="deposit":
            Bank.bank_total+=amount
            print("A new deposit has been made by {}.\nAn additional {} has been added to the bank total.\nThe current amount of money in the bank is {}.\n".format(owner,amount,Bank.bank_total))
        elif type=="withdrawl":
            Bank.bank_total-=amount
            print("A new withdrawl has been made by {}.\nAn additional {} has been subtracted from the bank total.\nThe current amount of money in the bank is {}.\n".format(owner,amount,Bank.bank_total))

class BankAccount(Bank):
    owner=""
    balance=0

    def __init__(self,owner,balance):
        capacity=Bank.check_capacity()
        if capacity=="not_full":
            BankAccount.owner=owner
            BankAccount.balance=balance
            Bank.accounts.append(owner)
            Bank.check_activities("new_account",BankAccount.owner,balance)

    def deposit(self):
        print("Hi, {}. Your current balance is: {}.\n".format(BankAccount.owner,BankAccount.balance))
        deposit=int(input("How much do you want to deposit? "))
        self.check_deposit_amt(deposit)
        print("Your new balance is: {}\n".format(BankAccount.balance))
        Bank.check_activities("deposit",self.owner,deposit)
        
    def check_deposit_amt(self,deposit):
        if deposit>0:
            BankAccount.balance+=deposit
            return True
        else:
            print("Invalid deposit")
            return False

    def withdraw(self):
        print("Your current balance is: {}".format(BankAccount.balance))
        withdrawl=int(input("Hi, {}. How much do you want to withdraw? ".format(BankAccount.owner)))
        self.check_withdrawl_amt(withdrawl)
 
    def check_withdrawl_amt(self,withdrawl):
        if withdrawl>BankAccount.balance:
            print("You don't have enough money in your account to withraw {}.\n".format(withdrawl))
            return False
        else:
            BankAccount.balance-=withdrawl
            print("Your new balance is: {}.\n".format(BankAccount.balance))
            Bank.check_activities("withdrawl",BankAccount.owner,withdrawl)
            return True
            
class Owner(BankAccount):
    credit_card_num=""
    password=""

    def __init__(self,owner,balance,password):
        super().__init__(owner,balance)
        import random
        Owner.credit_card_num=oct(random.randint(10000,99999))
        print("Your credit card number is: {}".format(Owner.credit_card_num))
        Owner.password=input("Enter a new password: ")
        print("")
        
    def check_owner_info(self):
        temp=[]
        for x in range(2):
            temp.append(input("Enter your credit card number: "))
            temp.append(input("Enter your password: "))
            print("")
            if temp[1]==Owner.password and temp[0]==Owner.credit_card_num:
                return True
            elif x<2:
                print("Invalid password or credit card number. Try again.")
            else:
                print("The card has been eaten by the machine\n and your credit card is now invalid\n")
                Owner.credit_card_num=""
                return False
        
    def deposit(self,check_owner_info):
        if not check_owner_info:
            print("Your account has become invalidated. Please see your local banker.\n")
        else:
            while True:
                twenties=int(input("How many twenties do you want to deposit?"))
                fifties=int(input("How many fifties do you want to deposit?"))
                hundreds=int(input("How many hundreds do you want to deposit?"))
                deposit=twenties*20+fifties*50+100*hundreds
                self.check_deposit_amt(deposit)
                print("Your new balance is: {}\n".format(BankAccount.balance))
                Bank.check_activities("deposit",BankAccount.owner,deposit)
                more_deposit=input('Do you want to make another deposit? Please type "y" or "n"')
                print("")
                if more_deposit=="n":
                    break
                                   
    def withdraw(self,check_owner_info):
        if not check_owner_info:
            print("Your account has become invalidated. Please see your local banker.")
        else:
            twenties=int(input("How many twenties do you want to withdraw?"))
            fifties=int(input("How many fifties do you want to withdraw?"))
            hundreds=int(input("How many hundreds do you want to withdraw?"))
            withdrawl=twenties*20+fifties*50+100*hundreds
            self.check_withdrawl_amt(withdrawl)
            



sharon=BankAccount("Sharon",100)
sharon.deposit()
sharon.withdraw()


daniel=Owner("Daniel",100,"mnisghh")
check_owner_info=daniel.check_owner_info()
daniel.deposit(check_owner_info)

check_owner_info=daniel.check_owner_info()
daniel.withdraw(check_owner_info)
