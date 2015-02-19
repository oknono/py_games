""""This script starts a game of tic tac toe on a console where a human player
can play against an AI. The player can choose a token and the computer will
decide who will go first. A player can play as many games as (s)he likes. The
program will keep score"""
from random import randint, shuffle
from time import sleep
from copy import deepcopy


class Board(object):
    """" All functions that relate to the Board object
    i.e create, print, update, copy and check a Board"""

    def __init__(self, board):
        """Initialize a new Board object"""
        self.board = board

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
        """Return an Board updated with given token at given index"""
        self.board[index] = token
        return self.board

    def get_copy_board(self):
        """Return a copy of a board"""
        return deepcopy(self)

    def is_valid_move(self, index):
        """Return Bool indicating if token can be placed at given index"""
        return self.board[index] == ' '

    def is_full(self):
        """Return Bool indicating if no more tokens can be placed"""
        return ' ' not in self.board

    def available_position(self):
        """return a list of all available postions on board (1-9)"""
        positions = []
        for index in range(9):
            if self.is_valid_move(index):
                positions.append(index + 1)
        return positions

    def win(self, token):
        """Return Bool indicating if there are three similar tokens in a row
        column or diagonal"""
        return (self.row_win(token) or self.column_win(token) or
                self.diagonal_win(token))

    def row_win(self, token):
        """Return Bool indicating if there are three similar tokens in a row"""
        return ((self.board[0] == self.board[1] == self.board[2] == token) or
                (self.board[3] == self.board[4] == self.board[5] == token) or
                (self.board[6] == self.board[7] == self.board[8] == token))

    def column_win(self, token):
        """Return Bool indicating if there are three similar tokens in a
        column"""
        return ((self.board[0] == self.board[3] == self.board[6] == token) or
                (self.board[1] == self.board[4] == self.board[7] == token) or
                (self.board[2] == self.board[5] == self.board[8] == token))

    def diagonal_win(self, token):
        """Return Bool indicating if there are three similar tokens in a
        diagonal"""
        return ((self.board[0] == self.board[4] == self.board[8] == token) or
                (self.board[2] == self.board[4] == self.board[6] == token))


class AI(object):
    """ All Functions that determine the move that will be made by computer """

    def computer_move(self, board, computer_token, player_token):
        """Return a int representing best move for computer """
        return (self.win_move(board, computer_token) or
                self.block_move(board, player_token) or
                self.move_corner(board) or
                self.move_center(board) or
                self.move_side(board))

    @staticmethod
    def win_move(board, token):
        """Return int if computer can make a winning move"""
        for index in range(0, 9):
            try_board = board.get_copy_board()
            if try_board.is_valid_move(index):
                try_board.make_move(index, token)
                if try_board.win(token):
                    return str(index)

    @staticmethod
    def block_move(board, token):
        """Return int if computer can block other player from winning"""
        for index in range(0, 9):
            try_board = board.get_copy_board()
            if try_board.is_valid_move(index):
                try_board.make_move(index, token)
                if try_board.win(token):
                    return str(index)

    @staticmethod
    def move_corner(board):
        """Return int if there is an valid corner on the board"""
        corners = [0, 2, 6, 8]
        shuffle(corners)
        for index in corners:
            if board.is_valid_move(index):
                return str(index)

    @staticmethod
    def move_center(board):
        """Return int if center of board is valid"""
        if board.is_valid_move(4):
            return str(4)

    @staticmethod
    def move_side(board):
        """Return int if there is a side of the board that is valid"""
        sides = [1, 3, 5, 7]
        shuffle(sides)
        for index in sides:
            if board.is_valid_move(index):
                return str(index)


class Game(object):
    """Class for creating a game object, with all necessary variables
    and functions for gameplay"""

    computer_thinking = 2

    def __init__(self):
        """Initialize a new Game object"""
        self.player_token = None
        self.computer_token = None
        self.player_turn = None
        self.play_again = True
        self.player_score = 0
        self.tie_score = 0
        self.ai_score = 0

    @staticmethod
    def print_opening():
        """Print an instruction on how to play the game"""
        print "\nLet's play Tic Tac Toe!\n"
        print "To play, please enter number 1 - 9 (see the illustration below)"
        example_board = Board([n for n in range(1, 10)])
        example_board.print_board()
        print "But first things first..."

    def tokens(self):
        """Ask players what token (s)he wants to use.
        Set and print values of computer token and player token"""
        while True:
            token = raw_input("Do you want to play"
                              " \"X\" or \"O\"? : ").upper()
            if token != 'X' and token != 'O':
                print "Does not compute, please choose again"
            else:
                if token == 'X':
                    self.player_token, self.computer_token = 'X', 'O'
                    print "Player is %s, computer is %s" % (self.player_token,
                                                            self.computer_token)
                    break
                else:
                    self.player_token, self.computer_token = 'O', 'X'
                    print "Player is %s, computer is %s" % (self.player_token,
                                                            self.computer_token)
                    break

    def first_move(self):
        """Set Boolean that determines if player make first move"""
        print "Computer will randomly decide who will make the first move..."
        self.player_turn = randint(0, 1)

    def play(self):
        """This function structures the flow of the game"""
        while self.play_again:
            ttt_board, computer = Board([' '] * 9), AI()
            self.print_opening()
            self.tokens()
            self.first_move()
            self.game_play(ttt_board, computer)
            self.score()
            self.again()

    def game_play(self, board, computer):
        """Let player and computer take turns and check for winning
        or tie condition"""
        #while True:
        while not (board.is_full() or board.win(self.computer_token) or
                   board.win(self.player_token)):
            if self.player_turn:
                print "Players turn: ",
                move = self.player_move(board)
                board.make_move(move, self.player_token)
                board.print_board()
                self.player_turn = False
            else:
                print "Computers turn..."
                sleep(Game.computer_thinking)
                move = int(computer.computer_move(board,
                                                  self.computer_token,
                                                  self.player_token))
                board.make_move(move, self.computer_token)
                board.print_board()
                self.player_turn = True
        self.game_end(board)

    def game_end(self, board):
        """Prints end message and updates score"""
        if board.is_full():
            print "It's a tie!"
            self.tie_score += 1
            #break
        elif board.win(self.computer_token):
            print "Computer wins!"
            self.ai_score += 1
            #break
        elif board.win(self.player_token):
            print "Player wins!"
            self.player_score += 1
            #break
        else:
            print "ERROR - this should not be printed"

    def player_move(self, board):
        """Return an integer if input is and int, in range and available,
        otherwise give feedback on valid input"""
        while True:
            answer = raw_input("What move do you want to make? ")
            try:
                move = int(answer) - 1
                if self.in_range(move) and board.is_valid_move(move):
                    return move
                else:
                    self.input_feedback(board)
            except ValueError:
                self.input_feedback(board)

    @staticmethod
    def in_range(move):
        """Return Bool if move is in range (0-8)"""
        return move >= 0 and move < 9

    @staticmethod
    def input_feedback(board):
        """Print feedback on move that is incorrect or invalid"""
        print "Please enter a valid move:",
        open_position = board.available_position()
        if len(open_position) > 1:
            print "positions",
            for index in range(len(open_position)-2):
                print str(open_position[index]) + ",",
            print open_position[- 2],
            print "and", open_position[-1], "are available"
        elif len(open_position) == 1:
            print "position", open_position[0], "is available"
        else:
            print "ERROR - No available elements in list"

    def score(self):
        """Print the current score"""
        print "The score is..."
        print "Human: " + str(self.player_score)
        print "Computer: " + str(self.ai_score)
        print "Ties: " + str(self.tie_score)

    def again(self):
        """Return Bool based on user input - new game or quit game"""
        self.play_again = raw_input("Do you want to play again?"
                                    "(Y)es/(N)o: ").lower().startswith('y')
        if self.play_again:
            print ""
        else:
            print "Goodbye!\n"

TTT = Game()
TTT.play()
