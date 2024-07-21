from tictactoe import minimax

EMPTY = None

board = [[EMPTY, "X", EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

print(minimax(board))