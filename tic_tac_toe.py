# Introduction
print " Welcome to Tic Tac Toe! \n"

def print_example_board():
    print "Please enter the number where you want to play. See the illustration below"
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
    
print_example_board()

print_board('X',' ','X','O',' ',' ','0',' ',' ')

	




