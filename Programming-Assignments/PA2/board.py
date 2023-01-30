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
            
      def isdone(self):
            done = False
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            if self.board[0] == self.board[1] == self.board[2] and not self.isempty('A1') or self.board[3] == self.board[4] == self.board[5] and not self.isempty('B1') or self.board[6] == self.board[7] == self.board[8] and not self.isempty('C1'):
                  if self.board[0] == self.board[1] == self.board[2]: self.winner = self.board[0]
                  if self.board[3] == self.board[4] == self.board[5]: self.winner = self.board[3]
                  if self.board[6] == self.board[7] == self.board[8]: self.winner = self.board[6]
                  done = True
            elif self.board[0] == self.board[3] == self.board[6] and not self.isempty('A1') or self.board[1] == self.board[4] == self.board[7] and not self.isempty('A2') or self.board[2] == self.board[5] == self.board[8] and not self.isempty('A3'):
                  if self.board[0] == self.board[3] == self.board[6]: self.winner = self.board[0]
                  if self.board[1] == self.board[4] == self.board[7]: self.winner = self.board[1]
                  if self.board[2] == self.board[5] == self.board[8]: self.winner = self.board[2]
                  done = True
            elif self.board[0] == self.board[4] == self.board[8] and not self.isempty('A1') or self.board[6] == self.board[4] == self.board[2] and not self.isempty('A3'):
                  if self.board[0] == self.board[4] == self.board[8]: self.winner = self.board[0]
                  if self.board[6] == self.board[4] == self.board[2]: self.winner = self.board[6]
                  done = True
            else:
                  for cell in valid_choices:
                        if self.isempty(cell):
                              done = False
                              break
                        done = True
            return done
            
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

               
