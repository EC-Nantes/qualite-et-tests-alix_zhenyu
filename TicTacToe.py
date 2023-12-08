import numpy as np

class Tic_tac_toe():
    
    def __init__(self):
        self.grille = np.zeros((3,3))
        self.player = -1 #1 or -1
    
    def next_move(self, x, y):
        x, y = int(x), int(y)
        if self.grille[x,y] == 0:
            self.grille[x, y] = self.player
            self.player *= -1
    
    def show(self):

        symb = lambda i, j: ' ' if self.grille[i,j] == 0 else ('X' if self.grille[i,j] == 1 else 'O')

        print(f"{symb(0,0)} | {symb(0,1)} | {symb(0,2)}")
        print("---------")
        print(f"{symb(1,0)} | {symb(1,1)} | {symb(1,2)}")
        print("---------")
        print(f"{symb(2,0)} | {symb(2,1)} | {symb(2,2)}")
    
    def winner(self):
        """Returns -1, 1 for the winner or 0 if there is no winenr yet.
        """
        for k in range(3):
            if np.sum(self.grille[k,:]) == 3 or np.sum(self.grille[:,k]) == 3:
                return 'X'
            if np.sum(self.grille[k,:]) == -3 or np.sum(self.grille[:,k]) == -3:
                return 'O'
        diag1 = self.grille[0,0]+self.grille[1,1]+self.grille[2,2]
        diag2 = self.grille[0,2]+self.grille[1,1]+self.grille[2,0]
        if diag1 == 3 or diag2 == 3:
            return 'X'
        if diag1 == -3 or diag2 == -3:
            return 'O'
        return 0
    
    def is_finished(self):
        return self.winner() != 0



if __name__ == "__main__":

    game = Tic_tac_toe()
    game.show()
    while not game.is_finished():
        x, y = input().split(' ')
        game.next_move(x, y)
        game.show()
    print("The winner is:", game.winner())