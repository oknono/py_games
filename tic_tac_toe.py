import random 

play_again = True

def print_example_board():
    print "To play, please enter the number where you want to play. See the illustration below"
    EXAMPLE_BOARD ='''
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
    print EXAMPLE_BOARD

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
    
def who_goes_first():
    #randomly choose who goes first
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
 # add catch for unsopported input           	
def player_move(board, letter):
    # check if move is legal
    while True:
        move = raw_input("What move do you want to make? ")
        if move.isdigit():
                move = int(move)
                if move > 0 and move < 10 and board[move-1] == ' ':
    	              board[int(move)-1] = letter
    	              return board
    	        elif move < 0 or move >= 10:
    	            print "That number is off the charts! Try again!"    
    	        else:
    	            print "That position is already taken"	            
        else:
            print "Please enter a number!"
            
def board_is_full(board):
	if ' ' not in board:
		return True
	else:
	    return False

while play_again:
    # Do the setup
    board = [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print "\nWelcome to Tic Tac Toe! \n"
    print_example_board()
    # Let player choose symbol
    player_letter, computer_letter = get_player_letter()
    print "Player is %s, computer is %s"%(player_letter, computer_letter)
    # Decides who will go first
    turn = who_goes_first()
    print "%s will make the first move" %turn
    # Draw board & get computer and player feedback until
    #check for win	
    while True:
        # check if board is full
        if board_is_full(board):
             	print "End of this game"
             	break
        else:
            # player turn   	
            if turn == 'player':
                print "Players turn using %s" %player_letter
                print_board(player_move(board,player_letter))
                # check for wins
                #disabled for now, game ends when board is full
                turn = 'computer'  
            # computer turn
            else:
            # uses user input for computer as well, need to implement heuristics
                print "Computers turn using %s" %computer_letter
                print_board(player_move(board,computer_letter))
                # check for wins
                #disabled for now, game ends when board is full
                turn = 'player'

        
#row_win
#v1 == v2 == v3 
#v4 == v5 == v6
#v7 == v8 == v9

#column_win

#v1 == v4 == v7
#v2 == v5 == v8
#v3 == v6 == v9

#diagonal_win
#v1 == v5 == v9
#v3 == v5 == v7
    # Win, lose or draw
    
    #play_again
    play_again = raw_input("Do you want to play again?(Y)es/(N)o: ").lower().startswith('y')

    

    






