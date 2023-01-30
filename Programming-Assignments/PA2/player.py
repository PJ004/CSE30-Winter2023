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
      def __init__(self, name, sign):
            self.name = name  # AI's name
            self.sign = sign  # AI's sign O or X
      def get_sign(self):
            return self.sign
      def get_name(self):
            return self.name
      def choose(self, board):
            valid_choices = [ 'A1', 'B1', 'C1', 
                              'A2', 'B2', 'C2', 
                              'A3', 'B3', 'C3']
            