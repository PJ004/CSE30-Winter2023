# author: Pranav Jha
# date: Feb 5, 2023
# file: tictac.py a Python module that implements a tic-tac-toe board
# input: None
# output: a tic-tac-toe board

class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""

      def get_size(self): 
            return self.size

      def get_winner(self):
            return self.winner

      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            index = valid_choices.index(cell)
            self.board[index] = sign
            
      def isempty(self, cell):
            # return True if the cell is empty (not marked with X or O)
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            index = valid_choices.index(cell)
            return True if self.board[index] == " " else False
      
      def isfull(self):
            # return True if the board is full (marked with X or O)
            cells = [cell for cell in self.board if cell == " "]
            return True if cells == [] else False

            
      def isdone(self):
            done = False
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            cells = {}
            for index, cell in enumerate(valid_choices):
                  cells[cell] = self.board[index]
            if cells['A1'] == cells['A2'] == cells['A3'] != " " or cells['B1'] == cells['B2'] == cells['B3'] != " " or cells['C1'] == cells['C2'] == cells['C3'] != " ":
                  if cells['A1'] == cells['A2'] == cells['A3']: self.winner = cells['A1']
                  elif cells['B1'] == cells['B2'] == cells['B3']: self.winner = cells['B1']
                  elif cells['C1'] == cells['C2'] == cells['C3']: self.winner = cells['C1']
                  done = True
            elif cells['A1'] == cells['B1'] == cells['C1'] != " " or cells['A2'] == cells['B2'] == cells['C2'] != " " or cells['A3'] == cells['B3'] == cells['C3'] != " ":
                  if cells['A1'] == cells['B1'] == cells['C1']: self.winner = cells['A1']
                  elif cells['A2'] == cells['B2'] == cells['C2']: self.winner = cells['A2']
                  elif cells['A3'] == cells['B3'] == cells['C3']: self.winner = cells['A3']
                  done = True
            elif cells['A1'] == cells['B2'] == cells['C3'] != " " or cells['A3'] == cells['B2'] == cells['C1'] != " ":
                  if cells['A1'] == cells['B2'] == cells['C3']: self.winner = cells['B2']
                  elif cells['A3'] == cells['B2'] == cells['C1']: self.winner = cells['B2']
                  done = True
            else:
                  for cell in valid_choices:
                        if self.isempty(cell):
                              done = False
                              break
                        done = True
            return done
            
      def reset(self):
            for cell in range(9):
                self.board[cell] = " "

      def show(self):
            # draw the board
            # need to complete the code
            print('   A   B   C') 
            print(' +---+---+---+')
            print('1| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))
            print(' +---+---+---+')
            print('2| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]))
            print(' +---+---+---+')
            print('3| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8]))
            print(' +---+---+---+')

               
