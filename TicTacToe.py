class Tic_tac_toe():
    pass



if __name__ == "__main__":
    game = Tic_tac_toe()
    while not game.is_finished():
        game.next_move(input())
        game.show()
    game.winner()