# Introduction

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


def print_board(v1, v2, v3, v4 ,v5, v6, v7, v8, v9):
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
'''%(v1,v2,v3,v4,v5,v6,v7,v8,v9)
    print BOARD
    

while play_again:
    print " Welcome to Tic Tac Toe! \n"
    print_example_board()
    print_board('X',' ','X','O',' ',' ','0',' ',' ')
    # Let player choose symbol
    while True:
        letter = raw_input("Do you want to play \"X\" or \"O\"? :").upper() 
        if letter != "X" and letter !="O":
        	print "Does not compute, please choose again"
        else:
            break
    print "player symbol is %s"%letter
    play_again = raw_input("Do you want to play again?(Y)es/(N)o: ").lower().startswith('y')

    

    



#check for win	
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


