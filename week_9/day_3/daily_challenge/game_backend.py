class Game:
    player="x"
    def __init__(self):
        self.game={1:["x"," ","Q"," ","x"," ","x"," "],
                   2:[" ","x"," ","x"," ","x"," ","x"],
                   3:["x"," ","x"," "," "," ","x"," "],
                   4:[" "," "," "," "," "," "," "," "],
                   5:[" "," "," "," "," "," "," "," "],
                   6:[" ","o"," ","o"," ","o"," ","o"],
                   7:["o"," ","o"," ","o"," ","o"," "],
                   8:[" ","o"," ","o"," ","o"," ","o"]}        
        
    def display_game(self):
        print("    0    1    2    3    4    5    6    7")
        for row,cols in self.game.items():
            print(row,cols)
        print("\n")
            
    def validate_move(self,start_pos,end_pos):
            piece_belongs_to=""
            if self.game[start_pos[0]][start_pos[1]] == "x" or self.game[start_pos[0]][start_pos[1]]=="K":
                piece_belongs_to="x"

            elif self.game[start_pos[0]][start_pos[1]] == "o" or self.game[start_pos[0]][start_pos[1]]=="Q":
                piece_belongs_to="o"

                
            if Game.player!=piece_belongs_to:
                print("Error. There is either no piece in your start position, or the opponent's piece is there.")
                return False

            if self.game[end_pos[0]][end_pos[1]]!=" ":
                print("Invalid move. Your end position is occupied by another piece.")
                return False

            return True

    def change_pos(self,start_pos,end_pos,piece):
        self.game[start_pos[0]][start_pos[1]]=" "
        self.game[end_pos[0]][end_pos[1]]=piece

    def take_opponent(self,row,col):
        print("here, take opponent")
        print(self.game[row][col])
        self.game[row][col]=" "
            
    def implement_move(self,start_pos,end_pos):
        
        if not self.validate_move(start_pos,end_pos):
            return "invalid move"


        #implement a regular move
        if Game.player=="x":
            if end_pos[0]==start_pos[0]+1 and(end_pos[1]==start_pos[1]-1 or end_pos[1]==start_pos[1]+1):
                return "regular move"

            elif self.game[start_pos[0]][start_pos[1]]=="K":
                if end_pos[0]==start_pos[0]-1 and(end_pos[1]==start_pos[1]-1 or end_pos[1]==start_pos[1]+1):
                    return "regular king move"


        if Game.player=="o":
            if end_pos[0]==start_pos[0]-1 and (end_pos[1]==start_pos[1]-1 or end_pos[1]==start_pos[1]+1):
                return "regular move"
            
            elif self.game[start_pos[0]][start_pos[1]]=="Q":
                if end_pos[0]==start_pos[0]+1 and(end_pos[1]==start_pos[1]-1 or end_pos[1]==start_pos[1]+1):
                    return "regular king move"                

        if Game.player=="x":
            opponent="o"
            king_opponent="Q"
        if Game.player=="o":
            opponent="x"
            king_opponent="K"

        #implement a regular jump
        if Game.player=="x":
            if end_pos[0]==start_pos[0]+2 and(end_pos[1]==start_pos[1]-2):
                if self.game[start_pos[0]+1][start_pos[1]-1]==opponent or self.game[start_pos[0]+1][start_pos[1]-1]==king_opponent:
                    self.take_opponent(start_pos[0]+1,start_pos[1]-1)
                    return "regular jump"
            elif end_pos[0]==start_pos[0]+2 and(end_pos[1]==start_pos[1]+2):
                if self.game[start_pos[0]+1][start_pos[1]+1]==opponent or self.game[start_pos[0]+1][start_pos[1]+1]==king_opponent:
                    self.take_opponent(start_pos[0]+1,start_pos[1]+1)
                    return "regular jump"

            if self.game[start_pos[0]][start_pos[1]]=="K":
                if end_pos[0]==start_pos[0]-2 and(end_pos[1]==start_pos[1]-2):
                    if self.game[start_pos[0]-1][start_pos[1]-1]==opponent or self.game[start_pos[0]-1][start_pos[1]-1]==king_opponent:
                        self.take_opponent(start_pos[0]-1,start_pos[1]-1)
                        return "regular king jump"
                elif end_pos[0]==start_pos[0]-2 and(end_pos[1]==start_pos[1]+2):
                    if self.game[start_pos[0]-1][start_pos[1]+1]==opponent or self.game[start_pos[0]-1][start_pos[1]+1]==king_opponent:
                        self.take_opponent(start_pos[0]-1,start_pos[1]+1)
                        return "regular king jump"
                
                

        if Game.player=="o":
            if end_pos[0]==start_pos[0]-2 and(end_pos[1]==start_pos[1]-2):
                if self.game[start_pos[0]-1][start_pos[1]-1]==opponent or self.game[start_pos[0]-1][start_pos[1]-1]==king_opponent:
                    self.take_opponent(start_pos[0]-1,start_pos[1]-1)
                    return "regular king jump"
            elif end_pos[0]==start_pos[0]-2 and(end_pos[1]==start_pos[1]+2):
                if self.game[start_pos[0]-1][start_pos[1]+1]==opponent or self.game[start_pos[0]-1][start_pos[1]+1]==king_opponent:
                    self.take_opponent(start_pos[0]-1,start_pos[1]+1)
                    return "regular king jump"

            if self.game[start_pos[0]][start_pos[1]]=="Q":
                if end_pos[0]==start_pos[0]+2 and(end_pos[1]==start_pos[1]-2):
                    if self.game[start_pos[0]+1][start_pos[1]-1]==opponent or self.game[start_pos[0]+1][start_pos[1]-1]==king_opponent:
                        self.take_opponent(start_pos[0]+1,start_pos[1]-1)
                        return "regular king jump"
                elif end_pos[0]==start_pos[0]+2 and(end_pos[1]==start_pos[1]+2):
                    if self.game[start_pos[0]+1][start_pos[1]+1]==opponent or self.game[start_pos[0]+1][start_pos[1]+1]==king_opponent:
                        self.take_opponent(start_pos[0]+1,start_pos[1]+1)
                        return "regular king jump"

        #implement a double jump
        if Game.player=="x":
            if end_pos[0]==start_pos[0]+4 and(end_pos[1]==start_pos[1]-4):
                if (self.game[start_pos[0]+1][start_pos[1]-1]==opponent and self.game[start_pos[0]+3][start_pos[1]-3]==opponent) or (self.game[start_pos[0]+1][start_pos[1]-1]==king_opponent and self.game[start_pos[0]+3][start_pos[1]-3]==king_opponent):
                    self.take_opponent(start_pos[0]+1,start_pos[1]-1)
                    self.take_opponent(start_pos[0]+3,start_pos[1]-3)
                    return "double jump"
            elif end_pos[0]==start_pos[0]+4 and(end_pos[1]==start_pos[1]+4):
                if (self.game[start_pos[0]+1][start_pos[1]+1]==opponent and self.game[start_pos[0]+3][start_pos[1]+3]==opponent) or (self.game[start_pos[0]+1][start_pos[1]+1]==king_opponent and self.game[start_pos[0]+3][start_pos[1]+3]==king_opponent):
                    self.take_opponent(start_pos[0]+1,start_pos[1]+1)
                    self.take_opponent(start_pos[0]+3,start_pos[1]+3)
                    return "double jump"
            elif end_pos[0]==start_pos[0]+4 and(end_pos[1]==start_pos[1]):
                if (self.game[start_pos[0]+1][start_pos[1]+1]==opponent and self.game[start_pos[0]+3][start_pos[1]+1]==opponent) or (self.game[start_pos[0]+1][start_pos[1]+1]==king_opponent and self.game[start_pos[0]+3][start_pos[1]+1]==king_opponent):
                    self.take_opponent(start_pos[0]+1,start_pos[1]+1)
                    self.take_opponent(start_pos[0]+3,start_pos[1]+1)
                    return "double jump"
                elif (self.game[start_pos[0]+1][start_pos[1]-1]==opponent and self.game[start_pos[0]+3][start_pos[1]-1]==opponent) or (self.game[start_pos[0]+1][start_pos[1]-1]==king_opponent and self.game[start_pos[0]+3][start_pos[1]-1]==king_opponent):
                    self.take_opponent(start_pos[0]+1,start_pos[1]-1)
                    self.take_opponent(start_pos[0]+3,start_pos[1]-1)
                    return "double jump"

            if self.game[start_pos[0]][start_pos[1]]=="K":
                if end_pos[0]==start_pos[0]-4 and(end_pos[1]==start_pos[1]-4):
                    if (self.game[start_pos[0]-1][start_pos[1]-1]==opponent and self.game[start_pos[0]-3][start_pos[1]-3]==opponent) or (self.game[start_pos[0]-1][start_pos[1]-1]==king_opponent and self.game[start_pos[0]-3][start_pos[1]-3]==king_opponent):
                        self.take_opponent(start_pos[0]-1,start_pos[1]-1)
                        self.take_opponent(start_pos[0]-3,start_pos[1]-3)
                        return "double king jump"
                elif end_pos[0]==start_pos[0]-4 and(end_pos[1]==start_pos[1]+4):
                    if (self.game[start_pos[0]-1][start_pos[1]+1]==opponent and self.game[start_pos[0]-3][start_pos[1]+3]==opponent) or (self.game[start_pos[0]-1][start_pos[1]+1]==king_opponent and self.game[start_pos[0]-3][start_pos[1]+3]==king_opponent):
                        self.take_opponent(start_pos[0]-1,start_pos[1]+1)
                        self.take_opponent(start_pos[0]-3,start_pos[1]+3)
                        return "double king jump"
                elif end_pos[0]==start_pos[0]-4 and(end_pos[1]==start_pos[1]):
                    if (self.game[start_pos[0]-1][start_pos[1]+1]==opponent and self.game[start_pos[0]-3][start_pos[1]+1]==opponent) or (self.game[start_pos[0]-1][start_pos[1]+1]==king_opponent and self.game[start_pos[0]-3][start_pos[1]+1]==king_opponent):
                        self.take_opponent(start_pos[0]-1,start_pos[1]+1)
                        self.take_opponent(start_pos[0]-3,start_pos[1]+1)
                        return "double king jump"
                    elif (self.game[start_pos[0]-1][start_pos[1]-1]==opponent and self.game[start_pos[0]-3][start_pos[1]-1]==opponent) or (self.game[start_pos[0]-1][start_pos[1]-1]==king_opponent and self.game[start_pos[0]-3][start_pos[1]-1]==king_opponent):
                        self.take_opponent(start_pos[0]-1,start_pos[1]-1)
                        self.take_opponent(start_pos[0]-3,start_pos[1]-1)
                        return "double king jump"

            

        if Game.player=="o":
            if end_pos[0]==start_pos[0]-4 and(end_pos[1]==start_pos[1]-4):
                if self.game[start_pos[0]-1][start_pos[1]-1]==opponent and self.game[start_pos[0]-3][start_pos[1]-3]:
                    self.take_opponent(start_pos[0]-1,start_pos[1]-1)
                    self.take_opponent(start_pos[0]-3,start_pos[1]-3)
                    return "double jump"
            elif end_pos[0]==start_pos[0]-4 and(end_pos[1]==start_pos[1]+4):
                if self.game[start_pos[0]-1][start_pos[1]+1]==opponent and self.game[start_pos[0]-3][start_pos[1]+3]==opponent:
                    self.take_opponent(start_pos[0]-1,start_pos[1]+1)
                    self.take_opponent(start_pos[0]-3,start_pos[1]+3)
                    return "double jump"
            elif end_pos[0]==start_pos[0]-4 and(end_pos[1]==start_pos[1]):
                if self.game[start_pos[0]-1][start_pos[1]+1]==opponent and self.game[start_pos[0]-3][start_pos[1]+1]==opponent:
                    self.take_opponent(start_pos[0]-1,start_pos[1]+1)
                    self.take_opponent(start_pos[0]-3,start_pos[1]+1)
                    return "double jump"
                elif self.game[start_pos[0]-1][start_pos[1]-1]==opponent and self.game[start_pos[0]-3][start_pos[1]-1]==opponent:
                    self.take_opponent(start_pos[0]-1,start_pos[1]-1)
                    self.take_opponent(start_pos[0]-3,start_pos[1]-1)
                    return "double jump"

            if self.game[start_pos[0]][start_pos[1]]=="Q":
                if end_pos[0]==start_pos[0]+4 and(end_pos[1]==start_pos[1]-4):
                    if self.game[start_pos[0]+1][start_pos[1]-1]==opponent and self.game[start_pos[0]+3][start_pos[1]-3]:
                        self.take_opponent(start_pos[0]+1,start_pos[1]-1)
                        self.take_opponent(start_pos[0]+3,start_pos[1]-3)
                        return "double king jump"
                elif end_pos[0]==start_pos[0]+4 and(end_pos[1]==start_pos[1]+4):
                    if self.game[start_pos[0]+1][start_pos[1]+1]==opponent and self.game[start_pos[0]+3][start_pos[1]+3]==opponent:
                        self.take_opponent(start_pos[0]+1,start_pos[1]+1)
                        self.take_opponent(start_pos[0]+3,start_pos[1]+3)
                        return "double king jump"
                elif end_pos[0]==start_pos[0]+4 and(end_pos[1]==start_pos[1]):
                    if self.game[start_pos[0]+1][start_pos[1]+1]==opponent and self.game[start_pos[0]+3][start_pos[1]+1]==opponent:
                        self.take_opponent(start_pos[0]+1,start_pos[1]+1)
                        self.take_opponent(start_pos[0]+3,start_pos[1]+1)
                        return "double king jump"
                    elif self.game[start_pos[0]+1][start_pos[1]-1]==opponent and self.game[start_pos[0]+3][start_pos[1]-1]==opponent:
                        self.take_opponent(start_pos[0]+1,start_pos[1]-1)
                        self.take_opponent(start_pos[0]+3,start_pos[1]-1)
                        return "double king jump"
                    
            print("Invalid move.")
            return "invalid move"

    def check_for_king(self,pos):
        if Game.player=="x":
            if pos[0]==8:
                print("x should be king")
                self.king_me(pos,"K")
                return True
        if Game.player=="o":
            if pos[0]==1:
                self.king_me(pos,"Q")
                return True

    def king_me(self,pos,char):
        print("Congratulations, {}! You're kinged!".format(Game.player))
        self.game[pos[0]][pos[1]]=char

    def switch_players(self):
        if Game.player=="x":
            Game.player="o"
        elif Game.player=="o":
            Game.player="x"
            

    def check_win(self):
        o_won=True
        x_won=True
        for row,cols in self.game.items():
            for col in range(len(cols)):
                if self.game[row][col]=="x" or self.game[row][col]=="K":
                    o_won=False
                if self.game[row][col]=="o" or self.game[row][col]=="Q":
                    x_won=False
                if not o_won and not x_won:
                    return "noone won"
        if o_won:
            return "o won"
        if x_won:
            return "x won"



