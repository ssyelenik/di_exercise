exec(open("game_backend.py",encoding="utf8").read())


def validate_positions(place):
    while True:
        pos_temp=input("Enter the {} position with a row number then a column number separated by a space:".format(place))
        pos=pos_temp.split(" ")
        try:
            pos[0]=int(pos[0])
            pos[1]=int(pos[1])
            return pos
        except:
            pass
        print("Incorrect input. Try again.")


    
game=Game()

while True:
    while True:
        game.display_game()
        print("Go ahead, {}. Your turn.".format(Game.player))

        start_pos=validate_positions("start")
        end_pos=validate_positions("end")

        check=game.implement_move(start_pos,end_pos)
        if not check=="invalid move":
            game.change_pos(start_pos,end_pos, game.game[start_pos[0]][start_pos[1]])
            game.check_for_king(end_pos)
            break
    

    if game.check_win()=="o won":
        game.display_game()
        print("Congratulations, o!!!! You won the game!")
        break
    if game.check_win()=="x won":
        game.display_game()
        print("Congratulations, x!!!! You won the game!")
        break

    game.switch_players()
