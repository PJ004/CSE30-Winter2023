# author: Pranav Jha
# date: Feb 5, 2023
# file: player.py a Python module that implements a player for a tic-tac-toe game
# input: None
# output: Player class

from random import choice

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            return self.sign
      def get_name(self):
            return self.name
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = [ 'A1', 'B1', 'C1', 
                              'A2', 'B2', 'C2', 
                              'A3', 'B3', 'C3']
            while True: 
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:').upper()
                  if cell in valid_choices :
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              break
                        else:
                              pass
                  else:
                        pass
                 
class AI:
      def __init__(self, name, sign, board):
            self.board = board
            self.name = name  # AI's name
            self.sign = sign  # AI's sign O or X
      def get_sign(self):
            return self.sign
      def get_name(self):
            return self.name
      def choose(self, board):
            valid_choices = [ 'A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            while True:
                  cell = choice(valid_choices)
                  if cell in valid_choices :
                        if self.board.isempty(cell):
                              self.board.set(cell, self.sign)
                              break
                        else:
                              pass
                  else:
                        pass

class MiniMax:
      def __init__(self, name, sign, board):
            AI.__init__(self, name, sign, board)
            self.board = board
            self.name = name  # AI's name
            self.sign = sign  # AI's sign O or X
            self.opponent_sign = 'X' if self.sign == 'O' else 'O'

      def choose(self, board):
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            cell = MiniMax.minimax(self, board, True, True)
            print(cell)
            board.set(cell, self.sign)

      def get_sign(self):
            return self.sign

      def get_name(self):
            return self.name
      
      def minimax(self, board, self_player, start):
            # check the base conditions
            if board.isdone():
                  if board.get_winner() == self.sign:
                        return 1
                        self.board.reset()
                  elif board.get_winner() == "":
                        return 0
                        self.board.reset()
                  else:
                        return -1
                        self.board.reset()
            # make a move (choose a cell) recursively
            maxscore = float('-inf')
            minscore = float('inf')
            move = ''

            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            empty_cells = [cell for cell in valid_choices if self.board.isempty(cell)]

            for cell in empty_cells:
                  #call minimax recursively
                  if self_player:
                        self.board.set(cell, self.sign)
                        score = MiniMax.minimax(self, board, False, False)
                        self.board.set(cell, " ")
                        if score > maxscore:
                              maxscore = score
                              move = cell
                  else:
                        self.board.set(cell, self.opponent_sign)
                        score = MiniMax.minimax(self, board, True, False)
                        self.board.set(cell, " ")
                        if score < minscore:
                              minscore = score
            if start:
                  return move
            elif self_player:
                  return maxscore
            else:
                  return minscore