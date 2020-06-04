def display_board(matrix):
    print("    |   |")
    print(" ",matrix['r1']['c1'],"|",matrix['r1']['c2'],"|",matrix['r1']['c3'])
    print("*************")
    print(" ",matrix['r2']['c1'],"|",matrix['r2']['c2'],"|",matrix['r2']['c3'])      
    print("*************")
    print(" ",matrix['r3']['c1'],"|",matrix['r3']['c2'],"|",matrix['r3']['c3'])
    print("    |   |")

def player_input(symbol):
    print("Player",symbol,"enter your move in the following format: r1 c1 ",end="")
    raw_move=input("")
    while not (raw_move=="r1 c1" or raw_move=="r1 c2" or raw_move=="r1 c3" or raw_move=="r2 c1" or raw_move=="r2 c2" or raw_move=="r2 c3" or raw_move=="r3 c1" or raw_move=="r3 c2" or raw_move=="r3 c3"):
        print("Invalid move.","Player",symbol)
        raw_move=input("Enter your move in the following format: r1 c1 ")
    move=raw_move.split(" ")    
    
    while not (matrix[move[0]][move[1]]==" "):
        print("That move's been taken already. Try again!")
        print("Player",symbol,"enter your move in the following format: r1 c1 ",end="")
        raw_move=input("")
        while not (raw_move=="r1 c1" or raw_move=="r1 c2" or raw_move=="r1 c3" or raw_move=="r2 c1" or raw_move=="r2 c2" or raw_move=="r2 c3" or raw_move=="r3 c1" or raw_move=="r3 c2" or raw_move=="r3 c3"):
            print("Invalid move.","Player",symbol)
            raw_move=input("Enter your move in the following format: r1 c1 ")
        move=raw_move.split(" ")


    return move
        
def update_matrix(player,move,matrix):
    if player=="X":
        matrix[move[0]][move[1]]="X"
    elif player=="O":
        matrix[move[0]][move[1]]="O"
    return matrix
    

def check_win(player,matrix):
    if (matrix["r1"]["c1"]==matrix["r1"]["c2"]==matrix["r1"]["c3"]==player) or (matrix["r2"]["c1"]==matrix["r2"]["c2"]==matrix["r2"]["c3"]==player) or (matrix["r3"]["c1"]==matrix["r3"]["c2"]==matrix["r3"]["c3"]==player) or (matrix["r1"]["c1"]==matrix["r2"]["c1"]==matrix["r3"]["c1"]==player) or (matrix["r1"]["c2"]==matrix["r2"]["c2"]==matrix["r3"]["c2"]==player) or (matrix["r1"]["c3"]==matrix["r2"]["c3"]==matrix["r3"]["c3"]==player) or (matrix["r1"]["c1"]==matrix["r2"]["c2"]==matrix["r3"]["c3"]==player) or (matrix["r1"]["c3"]==matrix["r2"]["c2"]==matrix["r3"]["c1"]==player):
        print("Gongratulations, player",player,"! You won!")
        return True




matrix={"r1":{"c1":" ","c2":" ","c3":" "},
        "r2":{"c1":" ","c2":" ","c3":" "},
        "r3":{"c1":" ","c2":" ","c3":" "}}
display_board(matrix)

turns=0
while True:    
    move1=player_input("X")
    matrix=update_matrix("X", move1, matrix)
    display_board(matrix)
    game_over=check_win("X",matrix)
    turns=turns+1
    print(turns)
    if game_over:
        break
    if turns==9:
        break
    
    move2=player_input("O")
    matrix=update_matrix("O", move2, matrix)
    display_board(matrix)
    game_status=check_win("O",matrix)
    turns=turns+1

    if game_over:
        break
    if turns==9:
        break
    
if turns==9 and not game_over:
    print("No one won this game!")

    
    
