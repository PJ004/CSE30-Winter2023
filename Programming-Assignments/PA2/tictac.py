# author: Pranav Jha
# date: Feb 1, 2023
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

from board import Board
from player import Player
from player import Player, AI, MiniMax #, SmartAI

# main program
print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board()
    #player1 = Player("Max", "X")
    player1 = MiniMax("Max", "X", board)
    #player1 = AI("Bob", "X", board)
    player2 = Player("Alice", "O")
    #player2 = SmartAI("Alice", "O", board)
    turn = True
    while True:
        board.show()
        if turn:
            player1.choose(board)
            turn = False
        else:
            player2.choose(board)
            turn = True
        if board.isdone():
            break
    board.show()
    if board.isfull():
        print("It is a tie!")
    elif board.get_winner() == player1.get_sign():
        print(f"{player1.get_name()} is a winner!")
    elif board.get_winner() == player2.get_sign():
        print(f"{player2.get_name()} is a winner!")
    ans = input("Would you like to play again? [Y/N]\n").upper()
    if (ans != "Y"):
        board.reset()
        break
print("Goodbye!")