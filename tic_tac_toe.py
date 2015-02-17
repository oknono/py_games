""""This script starts a game of tic tac toe on a console where a human player
can play against an AI"""
from random import randint, shuffle
from time import sleep
from copy import deepcopy


class Board(object):
    """" All functions that relate to the Board object
    i.e create, print, update, copy and check a Board"""

    def __init__(self):
        """Initialize a new Board object"""
        self.board = [' '] * 9

    def print_board(self):
        """Print the current state of a Board"""
        print ""
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
        print ""

    def make_move(self, index, token):
        """return an Board updated with given token at given index"""
        self.board[index] = token
        return self.board

    def get_copy_board(self):
        """Given a Board, return an exact replica"""
        return deepcopy(self)

    def is_empty(self, index):
        """Given a position on a board, return if token can be placed"""
        return self.board[index] == ' '

    def is_full(self):
        """Given a board, return if any moves can still be made"""
        return ' ' not in self.board

    def win(self, token):
        """Given a board and token, return if this token wins a game"""
        return (self.row_win(token) or self.column_win(token) or
                self.diagonal_win(token))

    def row_win(self, token):
        """Given a board and a token, return if there is a win on a row"""
        return ((self.board[0] == self.board[1] == self.board[2] == token) or
                (self.board[3] == self.board[4] == self.board[5] == token) or
                (self.board[6] == self.board[7] == self.board[8] == token))

    def column_win(self, token):
        """Given a board and a token, return if there is a win on a column"""
        return ((self.board[0] == self.board[3] == self.board[6] == token) or
                (self.board[1] == self.board[4] == self.board[7] == token) or
                (self.board[2] == self.board[5] == self.board[8] == token))

    def diagonal_win(self, token):
        """Given a board and a token, return if there is a win on a diagonal"""
        return ((self.board[0] == self.board[4] == self.board[8] == token) or
                (self.board[2] == self.board[4] == self.board[6] == token))

class AI(object):
    """ All Functions that determines the computer move"""

    def computer_move(self, board, computer_token, player_token):
        """ Given a board and player token, returns the best move for computer player"""
        return (self.win_move(board, computer_token) or
                self.block_move(board, player_token) or
                self.move_corner(board) or
                self.move_center(board) or
                self.move_side(board))

    @staticmethod
    def win_move(board, token):
        """Checks if computer can make winning move. Return integer or False"""
        for index in range(0, 9):
            try_board = board.get_copy_board()
            if try_board.is_empty(index):
                try_board.make_move(index, token)
                if try_board.win(token):
                    return str(index)

    @staticmethod
    def block_move(board, token):
        """Checks if computer can block the human player from making a winning move.
        Return integer or False"""
        for index in range(0, 9):
            try_board = board.get_copy_board()
            if try_board.is_empty(index):
                try_board.make_move(index, token)
                if try_board.win(token):
                    return str(index)

    @staticmethod
    def move_corner(board):
        """Checks if computer can make a move in a corner, picked randomly from the corners"""
        corners = [0, 2, 6, 8]
        shuffle(corners)
        for index in corners:
            if board.is_empty(index):
                return str(index)

    @staticmethod
    def move_center(board):
        """Checks if computer can make move in the center of board, returns center or False"""
        if board.is_empty(4):
            return str(4)

    @staticmethod
    def move_side(board):
        """Checks if computer can make a move in a corner, picked randomly from the corners"""
        sides = [1, 3, 5, 7]
        shuffle(sides)
        for index in sides:
            if board.is_empty(index):
                return str(index)

class Game(object):
    """Class for creating a game object, with all necessary variables and functions for gameplay"""

    computer_thinking = 2

    def __init__(self):
        """Initialize a new Game object"""
        self.player_token = None
        self.computer_token = None
        self.turn = None
        self.play_again = True
        self.player_score = 0
        self.tie_score = 0
        self.ai_score = 0

    @staticmethod
    def print_opening():
        """Print an instruction on how to play the game"""
        print "\nLet's play Tic Tac Toe!\n"
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

    def set_token(self):
        """Set the tokens for computer player and human player"""
        self.player_token, self.computer_token = self.get_tokens()
        print "Player is %s, computer is %s" % (self.player_token,
                                                self.computer_token)

    @staticmethod
    def get_tokens():
        """Ask players what token (s)he wants to use. Return computer token and player token"""
        while True:
            token = raw_input("Do you want to play"
                               " \"X\" or \"O\"? : ").upper()
            if token != 'X' and token != 'O':
                print "Does not compute, please choose again"
            else:
                if token == 'X':
                    return ['X', 'O']
                else:
                    return ['O', 'X']

    def first_move(self):
        """Returns the player that will have the first turn"""
        print "Computer will randomly decide who will make the first move..."
        sleep(Game.computer_thinking)
        if randint(0, 1) == 0:
            print "And the computer will go first"
            self.turn = 'Computer'
        else:
            print "And you get to go first!"
            self.turn = 'Player'
        return self.turn

    def play(self):
        """This function structures the flow of the game"""
        while self.play_again:
            ttt_board, computer = Board(), AI()
            self.print_opening()
            self.set_token()
            self.first_move()
            self.game_play(ttt_board, computer)
            self.score()
            self.again()

    def game_play(self, board, computer):
        """Let player and computer take turns and check for winning or tie condition"""
        while True:
            if board.is_full():
                print "It's a tie!"
                self.tie_score += 1
                break
            else:
                if self.turn == 'Player':
                    print "Players turn: ",
                    move = self.player_move(board)
                    board.make_move(move, self.player_token)
                    board.print_board()
                    if board.win(self.player_token):
                        print "Player wins!"
                        self.player_score += 1
                        break
                    else:
                        self.turn = 'Computer'
                else:
                    print "Computers turn..."
                    sleep(Game.computer_thinking)
                    move = int(computer.computer_move(board, self.computer_token, \
                               self.player_token))
                    board.make_move(move, self.computer_token)
                    board.print_board()
                    if board.win(self.computer_token):
                        print "Computer wins!"
                        self.ai_score += 1
                        break
                    else:
                        self.turn = 'Player'

    @staticmethod
    def player_move(board):
        """Ask input from player, return an integer"""
        while True:
            move = raw_input("What move do you want to make? ")
            if move.isdigit():
                move = int(move)
                if move > 0 and move < 10 and board.is_empty(move-1):
                    return move - 1
                elif move < 0 or move >= 10:
                    print "That number is off the charts! Try again!"
                else:
                    print "That position is already taken! Try again!"
            else:
                print "Please enter a NUMBER!"

    def score(self):
        """print the score of previous and current game"""
        print "The score is..."
        print "Human: " + str(self.player_score)
        print "Computer: " + str(self.ai_score)
        print "Ties: " + str(self.tie_score)

    def again(self):
        """Ask player to play again, return boolean"""
        self.play_again = raw_input("Do you want to play again?"
                                    "(Y)es/(N)o: ").lower().startswith('y')
        if self.play_again:
            print ""
        else:
            print "Goodbye!\n"

TTT = Game()
TTT.play()
