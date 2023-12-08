import numpy as np

class Tic_tac_toe():
    
    def __init__(self):
        self.grille = np.zeros((3,3))
        self.player = -1 #1 or -1
    
    def show(self):

        symb = lambda i, j: ' ' if self.grille[i,j] == 0 else ('X' if self.grille[i,j] == 1 else 'O')

        print(f"{symb(0,0)} | {symb(0,1)} | {symb(0,2)}")
        print("---------")
        print(f"{symb(1,0)} | {symb(1,1)} | {symb(1,2)}")
        print("---------")
        print(f"{symb(2,0)} | {symb(2,1)} | {symb(2,2)}")


if __name__ == "__main__":

    game = Tic_tac_toe()
    game.show()
    """
    while not game.is_finished():
        game.next_move(input())
        game.show()
    game.winner()"""