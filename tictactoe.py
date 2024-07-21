"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xNum = 0
    oNum = 0

    for row in board:
        for square in row: 
            if square == "X":
                xNum += 1
            elif square == "O":
                oNum += 1
    
    if xNum <= oNum:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for x in range(3):
        for y in range(3):
            if board[x][y] == EMPTY:
                actions.add((x, y))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = deepcopy(board)

    if newBoard[action[0]][action[1]] == EMPTY:
        newBoard[action[0]][action[1]] = player(newBoard)
        return newBoard
    else:
        raise NameError("Invalid action on board")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
