import flask
import random

guess_num_game=flask.Flask("guess_num_game")



@guess_num_game.route('/guess_num')
def guess_num():
    message=""
    guess=input("Input a number between 1 and 100: ")
    while True:
        try:
            guess=int(guess)
        except:
            print("Invalid number. Try again.")
            guess=input("Input a number between 1 and 100: ")
            pass
        if int(guess)>0 and int(guess)<101:
            break
        else:
            print("Your number must be between 1 and 100.")
            guess=input("Input a number between 1 and 100: ")
    
    random_num=random.randint(1,100)
    if guess==random_num:
        message="You guessed the right number!!!"
    else:
        message="You didn't guess the right number :-("
        
    html=flask.render_template("bin/index.html",message=message, guess=guess, random_num=random_num)
    return html

guess_num_game.run()
    
