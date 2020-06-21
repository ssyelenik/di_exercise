class Game:
    def get_user_item(self):
        #Ask the user to select an item (rock/paper/scissors).
        #Keep asking until the user has selected one of the items –
        #use data validation and looping. Return the item at the end of the function.
        user_item=input("Select (r)ock, (p)aper, or (s)cissors: ").lower()
        while True:
            if user_item == "r" or user_item == "p" or user_item == "s":
                return user_item
            else:
                user_item=input("Invalid entry. Try again.\nSelect (r)ock, (p)aper, or (s)cissors: ").lower()

    def get_computer_item(self):
        #Select rock/paper/scissors at random for the computer.
        #Return the item at the end of the function.
        import random
        play=["r","p","s"]
        return random.choice(play)

    def get_game_result(self, user_item, computer_item):
        #Determine the result of the game.

        #Parameters:
            #user_item – the user’s chosen item (rock/paper/scissors)
            #computer_item – the computer’s chosen (random) item (rock/paper/scissors)
            #Return either win, draw, or loss.
        if (user_item=="r" and computer_item=="s") or (user_item=="p" and computer_item=="r") or (user_item=="s" and computer_item=="p"):
            return "win"

        elif user_item==computer_item:
            return "draw"
        
        elif (user_item=="r" and computer_item=="p") or (user_item=="p" and computer_item=="s") or (user_item=="s" and computer_item=="r")     :
            return "loss"
        

    def play(self):
        #the function that will be called from outside the class (ie. from rock-paper-scissors.py).
        #It will do 3 things:

            #Get the user’s item (rock/paper/scissors) and remember it
            #Get a random item for the computer (rock/paper/scissors) and remember it
            #Determine the results of the game by comparing the user’s item and the computer’s item
            #Print the output of the game; something like this:
                #“You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”
            #Return the results of the game as a string:
                #win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item,
                #and loss means that the user has lost.

        user_item=self.get_user_item()
        computer_item=self.get_computer_item()
        game_result=self.get_game_result(user_item,computer_item)
        print("You selected {}. The computer selected {}. You {}!".format(user_item,computer_item,game_result))
        return game_result

