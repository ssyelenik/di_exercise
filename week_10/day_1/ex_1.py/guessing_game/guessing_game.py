from random import randint

answer=randint(1,100)
print(answer)
while True:
    try:
        guess=input("Enter a number between 1 and 100: ")
        guess=int(guess)
        if 0<guess<101:
            if guess==answer:
                print("You guessed it!!!")
                break
    except:
        print("Invalid number. Try again.")
        
        
