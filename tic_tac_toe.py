# Last updated Sunday Feb 1st 2015
# Inspired by "Invent Your Own Computer Games with Python, 2nd Edition" by Al Sweigart

import random 
import time

play_again = True

def play_again():
    play_again = raw_input("Do you want to play again?(Y)es/(N)o: ").lower().startswith('y')
    return play_again

def print_example_board():
    print "To play, please enter the number of the field. See the illustration below"
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

def print_board(list):
    BOARD = '''
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
'''%(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],)
    print BOARD
    
def first_move():
    if random.randint(0,1) == 0:
    	return 'Computer'
    else:
        return 'Player'
        
def get_player_letter():
  while True:
        player_letter = raw_input("Do you want to play \"X\" or \"O\"? :").upper() 
        if player_letter != "X" and player_letter !="O":
        	print "Does not compute, please choose again"
        else:
            if player_letter == "X":
                return ["X", "O"]
            else: 
            	return ["O", "X"]

def make_move(board, move, letter):
    board[move] = letter
    return board
 
def player_move(board):
    # input is board, return is an index
    # check if move is legal
    while True:
        move = raw_input("What move do you want to make? ")
        if move.isdigit():
                move = int(move)
                if move > 0 and move < 10 and is_empty(board, move-1):
    	              # board[int(move)-1] = letter
    	              return int(move) - 1
    	        elif move < 0 or move >= 10:
    	            print "That number is off the charts! Try again!"    
    	        else:
    	            print "That position is already taken"	            
        else:
            print "Please enter a number!"

def is_empty(board, index):
   return board[index] == ' ' 
   
def computer_move(board,letter): 
    if letter == 'X':
        p_letter = 'O'
    else:
        p_letter = 'X'

# Check if computer can make winning move
    for number in range(0,9):
        try_board = get_copy_board(board)
        if is_empty(try_board,number):
            try_board[number] = letter
            if win(try_board,letter):
                return number
                
# Check if can block player from winning
    for number in range(0,9):
        try_board = get_copy_board(board)
        if is_empty(try_board,number):
            try_board[number] = p_letter
            if win(try_board,p_letter):
                return number
            
# Take a corner piece (first one)
    for number in [0,2,6,8]:
        try_board = get_copy_board(board)
        if is_empty(try_board,number):
            return number

# Take center
    if is_empty(board, 5):
        return 5

# Take side (first one)
    for number in [1,3,5,7]:
        try_board = get_copy_board(board)
        if is_empty(try_board,number):
            return number

# Random move
#   for number in range(0,9):
#        if board[number] == ' ':
#            return number     

def get_copy_board(board):
    copy = []
    for item in board:
        copy.append(item)
    return copy

def board_is_full(board):
	if ' ' not in board:
		return True
	else:
	    return False

  
def win(board,player):
    return row_win(board,player) or column_win(board,player) or diagonal_win(board,player)      

def row_win(board,player):
    return ((board[0] == board[1] == board[2] == player) or 
       (board[3] == board[4] == board[5] == player) or
       (board[6] == board[7] == board[8] == player))

def column_win(board,player):
    return ((board[0] == board[3] == board[6] == player) or 
       (board[1] == board[4] == board[7] == player) or
       (board[2] == board[5] == board[8] == player)) 
        
def diagonal_win(board,player):
    return ((board[0] == board[4] == board[8] == player) or 
       (board[2] == board[4] == board[6] == player))
       

while play_again:
    # Do the setup
    board = [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print "\nWelcome to Tic Tac Toe! \n"
    print_example_board()
    # Let player choose symbol
    player_letter, computer_letter = get_player_letter()
    print "Player is %s, computer is %s"%(player_letter, computer_letter)
    # Decides who will go first
    turn = first_move()
    print "%s will make the first move" %turn
    # Draw board & get computer and player feedback until
    #check for win	
    while True:
        # check if board is full
        if board_is_full(board):
             	print "It's a tie!"
             	break
        else:
            # player turn   	
            if turn == 'Player':
                print "Players turn"
                move = player_move(board)
                make_move(board, move, player_letter)
                print_board(board)
                # check for wins
                if win(board,player_letter):
                    print "Player wins!"
                    break
                else:
                    turn = 'Computer'  
            # computer turn
            else:
            # uses user input for computer as well, need to implement heuristics
                print "Computers turn..."   
                time.sleep(1.5)        
                move = computer_move(board,computer_letter)
                make_move(board, move, computer_letter)
                print_board(board)
                # check for wins
                if win(board,computer_letter):
                    print "Computer wins!"
                    break
                else:
                    turn = 'Player'
    play_again = play_again()
        



    

    






