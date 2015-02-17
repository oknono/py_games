
from random import randint, shuffle
from time import sleep
from copy import deepcopy


class Board(object):
    # Eveything that relates to the board (a list)
    # --> check, update, print and copy

    def __init__(self):
        self.board = [' '] * 9

    def print_board(self):
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

    def make_move(self, index, player):
        self.board[index] = player
        return self.board

    def is_empty(self, index):
        return self.board[index] == ' '

    def is_full(self):
        return ' ' not in self.board

    def get_copy_board(self):
        return deepcopy(self)

    def win(self, player):
        return (self.row_win(player) or self.column_win(player) or
                self.diagonal_win(player))

    def row_win(self, player):
        return ((self.board[0] == self.board[1] == self.board[2] == player) or
                (self.board[3] == self.board[4] == self.board[5] == player) or
                (self.board[6] == self.board[7] == self.board[8] == player))

    def column_win(self, player):
        return ((self.board[0] == self.board[3] == self.board[6] == player) or
                (self.board[1] == self.board[4] == self.board[7] == player) or
                (self.board[2] == self.board[5] == self.board[8] == player))

    def diagonal_win(self, player):
        return ((self.board[0] == self.board[4] == self.board[8] == player) or
                (self.board[2] == self.board[4] == self.board[6] == player))


class Player(object):
    # Function(s) that get input from player
    # self.player_letter = None

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
    # All computer behaviour
    # self.computer_letter = None

    def computer_move(self, board, computer_letter):
        if computer_letter == 'X':
            player_letter = 'O'
        else:
            player_letter = 'X'
        return (self.win_move(board, computer_letter) or
                self.block_move(board, player_letter) or
                self.move_corner(board) or
                self.move_center(board) or
                self.move_side(board))

    # 1. Check if computer can make winning move
    def win_move(self, board, letter):
        print "win move"
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
        print "block move"
        for index in range(0, 9):
            try_board = board.get_copy_board()
            if try_board.is_empty(index):
                try_board.make_move(index, letter)
                if try_board.win(letter):
                    return str(index)
        else:
            return False

    # 3. Take a corner piece (shuffled list of corners)
    def move_corner(self, board):
        print "corner move"
        corners = [0, 2, 6, 8]
        shuffle(corners)
        print corners
        for index in corners:
            if board.is_empty(index):
                return str(index)
        else:
            return False

    # 4. Take center
    def move_center(self, board):
        "print center move"
        if board.is_empty(4):
            return str(4)
        else:
            return False

    # 5. Take side (shuffled list of sides)
    def move_side(self, board):
        "print side move"
        sides = [1, 3, 5, 7]
        shuffle(sides)
        print sides
        for index in sides:
            if board.is_empty(index):
                return str(index)
        else:
            return False


class Game(object):

    computer_thinking = 2

    def __init__(self):
        self.player_letter = None
        self.computer_letter = None
        self.turn = None
        self.play_again = True
        self.player_score = 0
        self.tie_score = 0
        self.ai_score = 0

    def print_opening(self):
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

    def set_letter(self):
        self.player_letter, self.computer_letter = self.get_letters()
        print "Player is %s, computer is %s" % (self.player_letter,
                                                self.computer_letter)

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

    def first_move(self):
        print "Computer will randomly decide who will make the first move...",
        #sleep(computer_thinking)
        if randint(0, 1) == 0:
            print "And the computer will go first"
            self.turn = 'Computer'
        else:
            print "And you get to go first!"
            self.turn = 'Player'
        #sleep(computer_thinking)
        return self.turn

    def play(self):
        while self.play_again:
            new_board, new_AI, new_player = Board(), AI(), Player()
            self.print_opening()
            self.set_letter()
            self.first_move()
            self.game_play(new_board, new_player, new_AI)
            self.score()
            self.again()

    def game_play(self, board, player, AI):
        while True:
            if board.is_full():
                print "It's a tie!"
                self.tie_score += 1
                break
            else:
                if self.turn == 'Player':
                    print "Players turn: ",
                    move = player.player_move(board)
                    board.make_move(move, self.player_letter)
                    board.print_board()
                    if board.win(self.player_letter):
                        print "Player wins!"
                        self.player_score += 1
                        break
                    else:
                        self.turn = 'Computer'
                else:
                    print "Computers turn..."
                    sleep(Game.computer_thinking)
                    move = int(AI.computer_move(board, self.computer_letter))
                    board.make_move(move, self.computer_letter)
                    board.print_board()
                    if board.win(self.computer_letter):
                        print "Computer wins!"
                        self.ai_score += 1
                        break
                    else:
                        self.turn = 'Player'

    def score(self):
        print "The score is..."
        print "Human: " + str(self.player_score)
        print "Computer: " + str(self.ai_score)
        print "Ties: " + str(self.tie_score)

    def again(self):
        self.play_again = raw_input("Do you want to play again?"
                                    "(Y)es/(N)o: ").lower().startswith('y')
        if self.play_again:
            print ""
        else:
            print "Goodbye!\n"

new_game = Game()
new_game.play()
