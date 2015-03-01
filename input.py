def get_numerical_input():
    while True:
        answer = raw_input("What move do you want to make? ")
        try:
            return int(answer) - 1
        except Exception:
            print "Please enter a numerical value (1 -9)"

def presentation(list):
    if len(list) > 1:
        for n in range(len(list)-2):
            print str(list[n]) + ",",
        print list[- 2],
        print "and", list[-1], "are available"
    elif len(list) == 1 :
        print list[0], "is available"  
    else:
        print "ERROR - No available elements in list"


def player_move(board):
    """Ask input from player, return an integer"""
    while True:
        move = get_numerical_input()
        if move >= 0 and move < 9 and is_empty(board, move):
            print "%s is a valid move" % move
            return move
        else:
            print "Please enter a valid number, "
            available_postions = []
            for n in range(9):
                if is_empty(board,n):
                    available_postions.append(n + 1)
            print "available_postions are ", available_postions
            presentation(available_postions)


def is_empty(board, index):
    """Return Bool indicating if token can be placed at given index"""
    return board[index] == ' '

def print_board(board):
        """Print the current state of a Board"""
        print ""
        print "   |   |   "
        print " %s | %s | %s " % (board[0], board[1], board[2])
        print "   |   |   "
        print "-----------"
        print "   |   |   "
        print " %s | %s | %s " % (board[3], board[4], board[5])
        print "   |   |   "
        print "-----------"
        print "   |   |   "
        print " %s | %s | %s " % (board[6], board[7], board[8])
        print "   |   |   "
        print ""

board1 = ["X", " ", "O", "X", " ", "O", " ", " ", " "]
board2 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
board3 = ["X", "O", "X", "O", "O", "X", "O", "X", " "]

presentation([1])
presentation([1,2])
presentation([1,2,3,4])
presentation(['a', 'b', 'c'])

#print_board(board1)
#print_board(board2)
#print_board(board3)

#player_move(board1)
#player_move(board2)
player_move(board3)