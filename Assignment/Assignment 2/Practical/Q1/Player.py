from Board import BoardUtility
from alpha_beta import minimax, minimax_prob
import random


class Player:
    def __init__(self, player_piece):
        self.piece = player_piece

    def play(self, board):
        return 0


class RandomPlayer(Player):
    def play(self, board):
        return random.choice(BoardUtility.get_valid_locations(board))


class HumanPlayer(Player):
    def play(self, board):
        move = int(input("input the next column index 1 to 9:")) - 1
        row = move // 3
        col = move % 3
        return row, col


class MiniMaxPlayer(Player):
    def __init__(self, player_piece, depth=5):
        super().__init__(player_piece)
        self.depth = depth

    def play(self, board):
        """
        Inputs : 
           board : 3*3 numpy array. 0 for empty cell, 1 and 2 for cells contains a piece.
        return the next move (i,j) of the player based on minimax algorithm.
        """
        # Todo: implement minimax algorithm with alpha beta pruning
        value, move = ..., ...
        return move


class MiniMaxProbPlayer(Player):
    def __init__(self, player_piece, depth=5, prob_stochastic=0.1):
        super().__init__(player_piece)
        self.depth = depth
        self.prob_stochastic = prob_stochastic

    def play(self, board):
        """
        Inputs : 
           board : 3*3 numpy array. 0 for empty cell, 1 and 2 for cells contains a piece.
        same as above but each time you are playing as max choose a random move instead of the best move
        with probability self.prob_stochastic.
        """
        # Todo: implement minimax algorithm with alpha beta pruning
        value, move = ..., ...
        return move
