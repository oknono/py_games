# Inspired by "Invent Your Own Computer Games with Python
# 2nd Edition" by Al Sweigart

from random import randint
from time import sleep
import copy


class Board(object):
    # Eveything that relates to the board (basically a list)
    # check, update, print and copy

    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def print_board(self):
        print "   |   |   "
        print " %s | %s | %s " % (self.board[0], self.board[1], self.board[2])
        print "   |   |   "
        print "-----------"
        print "   |   |   "
        print " %s | %s | %s " % (self.board[3], self.board[4], self.board[5])
        print "   |   |   "
        print "-----------"
        print "   |   |   "
        print " %s | %s | %s " % (self.board[6], self.board[7], self.board[8])
        print "   |   |   "

    def make_move(self, move, letter):
        self.board[move] = letter
        return self.board

    def is_empty(self, index):
        return self.board[index] == ' '

    def is_full(self):
        return ' ' not in self.board

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
        return (self.win_move(board, letter) or
                self.block_move(board, p_letter) or
                self.move_corner(board) or
                self.move_center(board) or
                self.move_side(board))

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


class Game(object):

    def __init__(self):
        self.player_letter = None
        self.computer_letter = None
        self.turn = None
        self.play_again = True

    def print_opening(self):
        print "Let's play Tic Tac Toe!"
        print "To play, please enter number 1 - 9 (see the illustration below)"
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
        print "But first things first..."

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

    def set_letter(self):
        self.player_letter, self.computer_letter = new_game.get_letters()
        print "Player is %s, computer is %s" % (self.player_letter,
                                                self.computer_letter)

    def first_move(self):
        print "Computer will randomly decided who will make the first move...",
        sleep(AI.computer_thinking)
        if randint(0, 1) == 0:
            print "And the computer will go first"
            self.turn = 'Computer'
        else:
            print "And you get to go first!"
            self.turn = 'Player'
        sleep(AI.computer_thinking)
        return self.turn

    def play(self):
        while self.play_again:
            new_board, new_AI, new_player = Board(), AI(), Player()
            self.print_opening()
            self.set_letter()
            self.first_move()
            self.play_game(new_board, new_player, new_AI)
            self.again()

    def play_game(self, board, player, AI):
        while True:
            if board.is_full():
                print "It's a tie!"
                break
            else:
                if self.turn == 'Player':
                    print "Players turn: ",
                    move = player.player_move(board)
                    board.make_move(move, self.player_letter)
                    board.print_board()
                    if board.win(self.player_letter):
                        print "Player wins!"
                        break
                    else:
                        self.turn = 'Computer'
                else:
                    print "Computers turn..."
                    sleep(AI.computer_thinking)
                    move = int(AI.computer_move(board, self.computer_letter))
                    board.make_move(move, self.computer_letter)
                    board.print_board()
                    if board.win(self.computer_letter):
                        print "Computer wins!"
                        break
                    else:
                        self.turn = 'Player'

    def again(self):
        self.play_again = raw_input("Do you want to play again?"
                                    "(Y)es/(N)o: ").lower().startswith('y')
        if self.play_again:
            print "\n\TEST\n"
        else:
            print "Goodbye!"

new_game = Game()
new_game.play()
