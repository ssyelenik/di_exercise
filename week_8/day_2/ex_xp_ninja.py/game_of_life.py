class Grid:
    grid={}

    def __init__(self):
        new_grid={}
        for x in range(10):
            temp=[]
            for y in range(10):
                temp.append("O")
            new_grid[x]=temp
        Grid.grid=new_grid

    def display_grid(self):
        for key,value in Grid.grid.items():
            if key<10:
                print(key,"",value)
            else:
                print(key,value)
        print("\n\n")
                
    def update_grid(self,cell,letter):
        Grid.grid[cell[0]][cell[1]]=letter

    def play_game(self):
        for q in range(20):
            for key,value in Grid.grid.items():
                neighbors=[]
                for index,live in enumerate(value):
                    if key>0 and index>0 and key<9 and index<9:
                        neighbors.append([key-1,index-1])
                        neighbors.append([key-1,index])
                        neighbors.append([key-1,index+1])
                        neighbors.append([key,index-1])
                        neighbors.append([key,index+1])
                        neighbors.append([key+1,index-1])
                        neighbors.append([key+1,index])
                        neighbors.append([key+1,index+1])                

                    live_neighbors=0
                    for neighbor in neighbors:
                        if Grid.grid[neighbor[0]][neighbor[1]]=="X":
                            live_neighbors+=1
                            
                    if value[index]=="X" and (live_neighbors==2 or live_neighbors==3):
                        pass
                    else:
                        if value[index]=="X" and live_neighbors<2:
                            letter="O"
                            self.update_grid([key,index],letter)
                        elif value[index]=="X" and live_neighbors>3:
                            letter="O"
                            self.update_grid([key,index],letter)
                        elif value[index]=="O" and live_neighbors==3:
                            letter="X"
                            self.update_grid([key,index],letter)
                    neighbors.clear()
            self.display_grid()    
        
class Cell(Grid):
    def __init__(self):
        import random
        cells=[]
        x=random.randint(0,9)
        y=random.randint(0,9)
        cell=[x,y]
        if cell not in cells:
            cells.append(cell)
            Grid.update_grid(self,cell,"X")
        

game_grid=Grid()
game_grid.display_grid()

for z in range(25):
    start_cell=Cell()

game_grid.display_grid()

game_grid.play_game()
                
