
exec(open("game.py",encoding="utf8").read())
def get_user_menu_choice():
    #this should display a simple menu,
    #get the user’s choice (with data validation),
    #and return the choice. No looping should occur here.

    print("    Menu:")
    print("    (g) Play a new game")
    print("    (x) Show scores and exit\n")

    game_choice=input().lower()
    if game_choice=="g" or game_choice=="x":
        return game_choice
    else:
        game_choice="x"
        return game_choice

def print_results(result):
    #this should print the results of the games played.
    #It should have a single parameter named results;
    #which will be a dictionary of the results of the games played.

    #It should display these results in a user-friendly way,
    #and thank the user for playing.

    #Note: results should be in this form: {win: 2,loss: 4,draw: 3}.
    #Bear in mind that this dictionary will need to be created and populated in some other part of our code,
    #and passed in to the print_results function at the right time.
    print("    Game Results:")
    print("      You won {} times".format(result["win"]))
    print("      You lost {} times".format(result["loss"]))
    print("      You drew {} times\n\n".format(result["draw"]))
    print("    Thank you for playing!")

def main():
    
    result={"win":0,"loss":0,"draw":0}
    while True:
        game_choice=get_user_menu_choice()
        if game_choice=="x":
            print_results(result)
            break
        elif game_choice=="g":
            game=Game()
            round_result=game.play()

        if round_result=="win":
            result["win"]+=1
        elif round_result=="loss":
            result["loss"]+=1
        elif round_result=="draw":
            result["draw"]+=1
           

if __name__ == "__main__":
    main()
        
            

