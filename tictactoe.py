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
    if not(0 <= action[0] <= 2) or not(0 <= action[1] <= 2):
        raise NameError("Invalid action on board")
    
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
    # Horizontal Check
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == "X":
                return "X"
            if board[i][0] == "O":
                return "O"
    
    # Vertical Check
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == "X":
                return "X"
            if board[0][i] == "O":
                return "O"

    # Leading Diagonal Check
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[1][1] == "X":
            return "X"
        if board[1][1] == "O":
            return "O"

    # Non-leading Diagonal Check
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[1][1] == "X":
            return "X"
        if board[1][1] == "O":
            return "O"
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    boardFilled = True
    for x in range(3):
        for y in range(3):
            if board[x][y] == EMPTY:
                boardFilled = False

    return boardFilled


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
