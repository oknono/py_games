# Inspired by "Invent Your Own Computer Games with Python
# 2nd Edition" by Al Sweigart

from random import randint
from time import sleep
import copy

class Board(object):
# Eveything that relates to the board - reading, updating, printing, checking
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def print_board(self):
        print  '''
   |   |
 %s | %s | %s
   |   |
-----------
   |   |
 %s | %s | %s
   |   |
-----------
   |   |
 %s | %s | %s
   |   |
''' % (self.board[0], self.board[1], self.board[2], self.board[3], self.board[4],
       self.board[5], self.board[6], self.board[7], self.board[8])

    def make_move(self, move, letter):
         self.board[move] = letter
         return self.board

    def is_empty(self, index):
        return self.board[index] == ' '

    def is_full(self):
        return ' ' not in self.board
            
    # this function will be redundant - we can make a new board object to try move
    def get_copy_board(self):
        return copy.deepcopy(self)

    def win(self, player):
        return ((self.board[0] == self.board[1] == self.board[2] == player) or
                (self.board[3] == self.board[4] == self.board[5] == player) or
                (self.board[6] == self.board[7] == self.board[8] == player) or
                (self.board[0] == self.board[3] == self.board[6] == player) or
                (self.board[1] == self.board[4] == self.board[7] == player) or
                (self.board[2] == self.board[5] == self.board[8] == player) or
                (self.board[0] == self.board[4] == self.board[8] == player) or
                (self.board[2] == self.board[4] == self.board[6] == player))

class Player(object):
# All functions that gets move from player    
    
    def player_move(self, board):
        while True:
            move = raw_input("What move do you want to make? ")
            if move.isdigit():
                move = int(move)
                if move > 0 and move < 10 and board.is_empty(move-1):
                    return (move - 1)
                elif move < 0 or move >= 10:
                    print "That number is off the charts! Try again!"
                else:
                    print "That position is already taken! Try again!"
            else:
                print "Please enter a NUMBER!" 

class AI(object):   
# All functions that get move from computer
    computer_thinking = 2

    def computer_move(self, board, letter):
        if letter == 'X':
            p_letter = 'O'
        else:
            p_letter = 'X'
        return self.win_move(board, letter) or self.block_move(board, p_letter) or self.move_corner(board) or self.move_center(board) or self.move_side(board)

    # 1. Check if computer can make winning move
    def win_move(self, board, letter):
        for index in range(0, 9):
            try_board = board.get_copy_board()
            if try_board.is_empty(index):
                try_board.make_move(index, letter)
                if try_board.win(letter):
                    return str(index)
        else: 
            return False

    # 2. Check if computer can block player from winning
    def block_move(self, board, letter):
        for index in range(0, 9):
            try_board = board.get_copy_board()
            if try_board.is_empty(index):
                try_board.make_move(index, letter)
                if try_board.win(letter):
                    return str(index)
        else: 
            return False

    # 3. Take a corner piece (first one computer finds)
    def move_corner(self, board):
        for index in [0, 2, 6, 8]:
            if board.is_empty(index):
                return str(index)
        else: 
            return False

    # 4. Take center
    def move_center(self, board):
        if board.is_empty(4):
            return str(4)
        else: 
            return False

    # 5. Take side (first one computer finds)
    def move_side(self, board):
        for index in [1, 3, 5, 7]:
            if board.is_empty(index):
                return str(index)
        else: 
            return False

# class Game():
#   All function that not relate to updating board or getting input from player or AI


#play_again = True
#computer_thinking = 2

class Game(object):

    def __init__(self):
        self.play_again = True
    def print_example_board(self):
        print "To play, please enter the number of the field."
        print "See the illustration below"
        print '''
   |   |
 1 | 2 | 3
   |   |
-----------
   |   |
 4 | 5 | 6
   |   |
-----------
   |   |
 7 | 8 | 9
   |   |
'''

    def first_move(self):
        if randint(0, 1) == 0:
            return 'Computer'
        else:
            return 'Player'

    def get_letters(self):
        while True:
            letter = raw_input("Do you want to play"
                               " \"X\" or \"O\"? : ").upper()
            if letter != 'X' and letter != 'O':
                print "Does not compute, please choose again"
            else:
                if letter == 'X':
                    return ['X', 'O']
                else:  
                    return ['O', 'X']

    #def play_again(self):
    #    self.play_again = raw_input("Do you want to play again?"
    #                       "(Y)es/(N)o: ").lower().startswith('y')
    #    return self.play_again

# Main part of game

play_again = True

while play_again:
    new_game = Game()
    new_board = Board()
    new_AI = AI()
    new_player = Player()
    print "\nWelcome to Tic Tac Toe! \n"
    player_letter, computer_letter = new_game.get_letters()
    print "Player is %s, computer is %s" % (player_letter, computer_letter)
    print ("\n")
    new_game.print_example_board()
    print ("\n")
    print "Computer will randomly decided who will make the first move..."
    sleep(AI.computer_thinking)
    turn = new_game.first_move()
    print "%s will make the first move" % turn
    sleep(AI.computer_thinking)
    while True:
        if new_board.is_full():
            print "It's a tie!"
            break
        else:
            if turn == 'Player':
                print "Players turn: ",
                move = new_player.player_move(new_board)
                new_board.make_move(move, player_letter)
                new_board.print_board()
                if new_board.win(player_letter):
                    print "Player wins!"
                    break
                else:
                    turn = 'Computer'
            else:
                print "Computers turn..."
                sleep(AI.computer_thinking)
                move = int(new_AI.computer_move(new_board, computer_letter))
                new_board.make_move(move, computer_letter)
                new_board.print_board()
                if new_board.win(computer_letter):
                    print "Computer wins!"
                    break
                else:
                    turn = 'Player'#

    play_again = raw_input("Do you want to play again?"
                           "(Y)es/(N)o: ").lower().startswith('y')
