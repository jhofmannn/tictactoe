"""
Tic Tac Toe Player
"""

import math
import copy
import sys

sys.setrecursionlimit(3000)

#The player function should take a board state as input, and return which player’s turn it is (either X or O).
#In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
#Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
#The actions function should return a set of all of the possible actions that can be taken on a given board.
#Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
#Possible moves are any cells on the board that do not already have an X or an O in them.
#Any return value is acceptable if a terminal board is provided as input.
#The result function takes a board and an action as input, and should return a new board state, without modifying the original board.
#If action is not a valid action for the board, your program should raise an exception.
#The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
#Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.
#The winner function should accept a board as input, and return the winner of the board if there is one.
#If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
#One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
#You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
#If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.
#The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.
#If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
#Otherwise, the function should return False if the game is still in progress.
#The utility function should accept a terminal board as input and output the utility of the board.
#If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
#You may assume utility will only be called on a board if terminal(board) is True.
#The minimax function should take a board as input, and return the optimal move for the player to move on that board.
#The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
#If the board is a terminal board, the minimax function should return None.


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
    count_of_X = 0
    count_of_O = 0
    for col in range(len(board)):
        for row in range(len(board)):
            if (board[col][row]==X):
                count_of_X += 1
            if (board[col][row]==O):
                count_of_O += 1
    if (count_of_X==count_of_O):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a = set ()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (board[row][col]==None):
                a.add((row,col))
    return a


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    r,c = action
    cpy_board = copy.deepcopy(board)
    for row in range(len(cpy_board)):
        for col in range(len(cpy_board[row])):
            #print("r=",r)
            #print("c=",c)
            #print("row=",row)
            #print("col=",col)
            #print("playa=",player(cpy_board))
            if (cpy_board[row][col]!=EMPTY and row==r and col==c):
                raise Exception("bad result")
            if (cpy_board[row][col]==EMPTY and row==r and col==c):
                cpy_board[row][col]=player(cpy_board)
    #print("cpy_board=",cpy_board)
    return cpy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #horizontal X
    for col in range(len(board)):
        for row in range(len(board)):
            if ((board[row][0]==X) and (board[row][1]==X) and (board[row][2]==X)):
                return X
    #horizontal O
    for col in range(len(board)):
        for row in range(len(board)):
            if ((board[row][0]==O) and (board[row][1]==O) and (board[row][2]==O)):
                return O
    #vertical X
    for row in range(len(board)):
            if ((board[0][row]==X) and (board[1][row]==X) and (board[2][row]==X)):
                return X
    #vertical O
    for row in range(len(board)):
            if ((board[0][row]==O) and (board[1][row]==O) and (board[2][row]==O)):
                return O
    #diag X
    if ((board[0][0]==X) and (board[1][1]==X) and (board[2][2]==X)):
                return X
    #diag O
    if ((board[0][0]==O) and (board[1][1]==O) and (board[2][2]==O)):
                return O
    #diag X
    if ((board[0][2]==X) and (board[1][1]==X) and (board[2][0]==X)):
                return X
    #diag O
    if ((board[0][2]==O) and (board[1][1]==O) and (board[2][0]==O)):
                return O
    #other
    return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)==X:
        return True
    if winner(board)==O:
        return True
    #other
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == None:
                return False
    return True
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif (winner(board)==O):
        return -1
    else:
        return 0

def max_value(board):
    #v = -math.inf
    v = -1000
    if terminal(board):
        return utility(board)
    #print("BOARD_MAXV",board)
    #print("actions_maxv=",actions(board))
    for action in actions(board):
        #print("action=",result(board,action),"\n")
        #v = max(v, min_value(result(board,action)))
    return v

def min_value(board):
    #v = math.inf
    v = 1000
    if terminal(board):
        return utility(board)
    #print("BOARD_MINV=",board)
    #print("actions_minv=",actions(board))
    for action in actions(board):
        #print("action=",result(board,action),"\n")
        #v = min(v, max_value(result(board,action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #Player X we want to maximimze
    if terminal(board):
        return None
    elif player(board)==X:
        #v = -math.inf
        v = -1000
        best = None
        #print("BOARDX=",board)
        for action in actions(board):
            current = min_value(result(board,action))
            if (current > v):
                v = current
                best = action;
        return best
    elif player(board)==O:
        #v = math.inf
        v = 1000
        best = None
        #print("BOARDO=",board)
        for action in actions(board):
            current = max_value(result(board,action))
            if current < v:
                v = current
                best = action
        return best


