# given a file with a list of the actions played, produce a file that describes the state
#
# INPUT: a file with a list of actions played of the form (N, X) where N is a position from 0-8
# OUTPUT: a file describing the state of the board with 9 pairs of values of the form (N,P) 
#         where N is the position (0-8) and P is what is placed there (X or __ ) 

def main():
    # local variables
    board = ["_" for i in range(9)]

    # read input (file with list of actions played)
    input = open("txt-files\input\\actions-input1.txt", "r")
    input.readline() # skip intro comment
    list1 = input.readlines()

    # populate board with actions on given positions
    for moves in list1:
        idx = moves[1]
        char = moves[4] # in tic-tac-alone, char will only be X
        board[int(idx)] = char

    # write to output (file that describes state)

    output = open("txt-files\output\state-output.txt", "w")
    for x in range(9):
        output.write( "(" + str(x) + ", " + board[x] + ")\n")
    output.close()

if __name__ == '__main__':
    main()