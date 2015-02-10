# Inspired by "Invent Your Own Computer Games with Python
# 2nd Edition" by Al Sweigart

from random import randint
from time import sleep
import copy

# Change things for assigning letters to players

class Board(object):
#A Tic-Tac-Toe Board
    def __init__(self):
        # create a list like this ' ' * 9
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def print_board(self):
        # Make this function shorter
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
        #make this function shorter
        return ' ' not in self.board
            
    # this function will be redundant - we can make a new board object to try move
    def get_copy_board(self):
        return copy.copy(self.board)


    def win(self, player):
        return ((self.board[0] == self.board[1] == self.board[2] == player) or
                (self.board[3] == self.board[4] == self.board[5] == player) or
                (self.board[6] == self.board[7] == self.board[8] == player) or
                (self.board[0] == self.board[3] == self.board[6] == player) or
                (self.board[1] == self.board[4] == self.board[7] == player) or
                (self.board[2] == self.board[5] == self.board[8] == player) or
                (self.board[0] == self.board[4] == self.board[8] == player) or
                (self.board[2] == self.board[4] == self.board[6] == player))

    # put indexes in vars? row var/columnvar/diag var. Add corner var and side var
#    def row_win(self, player):
#        return ((self.board[0] == self.board[1] == self.board[2] == player) or
#                (self.board[3] == self.board[4] == self.board[5] == player) or
#                (self.board[6] == self.board[7] == self.board[8] == player))
#
#
#    def column_win(self, player):
#        return ((self.board[0] == self.board[3] == self.board[6] == player) or
#                (self.board[1] == self.board[4] == self.board[7] == player) or
#                (self.board[2] == self.board[5] == self.board[8] == player))
#
#
#    def diagonal_win(self, player):
#        return ((self.board[0] == self.board[4] == self.board[8] == player) or
#                (self.board[2] == self.board[4] == self.board[6] == player))


#class Player(object):
    
#    def __init__(self):
#       pass
#       self.letter = ??

def get_letter():
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


def player_move(board):
    while True:
        move = raw_input("What move do you want to make? ")
        if move.isdigit():
            move = int(move)
            if move > 0 and move < 10 and board.is_empty(move-1):
                return int(move) - 1
            elif move < 0 or move >= 10:
                print "That number is off the charts! Try again!"
            else:
                print "That position is already taken! Try again!"
        else:
            print "Please enter a NUMBER!"

# def play_again():

# class AI(object):

def computer_move(board, letter):
    if letter == 'X':
        p_letter = 'O'
    else:
        p_letter = 'X'
    return win_move(board, letter) or block_move(board, p_letter) or move_corner(board) or move_center(board) or move_side(board)

# 1. Check if computer can make winning move
def win_move(board, letter):
    for number in range(0, 9):
        try_board = board.get_copy_board()
        if try_board.is_empty(number):
            try_board[number] = letter
            if try_board.win(letter):
                return number
    else: 
        return False

# 2. Check if computer can block player from winning
def block_move(board, letter):
    for number in range(0, 9):
        try_board = board.get_copy_board()
        if try_board.is_empty(number):
            try_board[number] = letter
            if try_board.win(letter):
                return number
    else: 
        return False

# 3. Take a corner piece (first one computer finds)
def move_corner(board):
    for number in [0, 2, 6, 8]:
        if board.is_empty(number):
            return number
    else: 
        return False

# 4. Take center
def move_center(board):
    if board.is_empty(5):
        return 5
    else: 
        return False

# 5. Take side (first one computer finds)
def move_side(board):
    for number in [1, 3, 5, 7]:
        if board.is_empty(number):
            return number
    else: 
        return False

# class Game():
#   pass 


play_again = True
computer_thinking = 2


def print_example_board():
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

def first_move():
    if randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'

# Main part of game
while play_again:
    # Do the setup - part of every new game
    new_board = Board()
    print "\nWelcome to Tic Tac Toe! \n"
    player_letter, computer_letter = get_letter()
    print "Player is %s, computer is %s" % (player_letter, computer_letter)
    print ("\n")
    print_example_board()
    print ("\n")
    print "Computer will randomly decided who will make the first move..."
    sleep(computer_thinking)
    turn = first_move()
    print "%s will make the first move" % turn
    sleep(computer_thinking)
    #Draw board & get computer and player feedback until
    #one player wins or there is a tie
    while True:
        # check for tie - board is full and no one won
        if new_board.is_full():
            print "It's a tie!"
            break
        else:
            if turn == 'Player':
                print "Players turn: ",
                move = player_move(new_board)
                new_board.make_move(move, player_letter)
                new_board.print_board()
                if new_board.win(player_letter):
                    print "Player wins!"
                    break
                else:
                    turn = 'Computer'
            else:
                print "Computers turn..."
                sleep(computer_thinking)
                move = computer_move(new_board, computer_letter)
                new_board.make_move(move, computer_letter)
                board.print_board()
                if new_board.win(computer_letter):
                    print "Computer wins!"
                    break
                else:
                    turn = 'Player'#

    play_again = raw_input("Do you want to play again?"
                           "(Y)es/(N)o: ").lower().startswith('y')
