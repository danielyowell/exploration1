# INPUT: a file describing the state of the board
# OUTPUT: a file with the number of times that the player has won (how many 3-in-a-rows)

def vertCheck(moves):
    vertWins = 0
    vwin1 = [0,3,6]
    vwin2 = [1,4,7]
    vwin3 = [2,5,8]

    if all(i in moves for i in vwin1):
        vertWins += 1
    if all(i in moves for i in vwin2):
        vertWins += 1
    if all(i in moves for i in vwin3):
        vertWins += 1
    return vertWins
    

def horiCheck(moves):
    horiWins = 0
    hwin1 = [0,1,2]
    hwin2 = [3,4,5]
    hwin3 = [6,7,8]

    if all(i in moves for i in hwin1):
        horiWins += 1
    if all(i in moves for i in hwin2):
        horiWins += 1
    if all(i in moves for i in hwin3):
        horiWins += 1
    return horiWins

def diagCheck(moves):
    diagWins = 0
    dwin1 = [0,4,8]
    dwin2 = [2,4,6]
    if all(i in moves for i in dwin1):
        diagWins += 1
    if all(i in moves for i in dwin2):
        diagWins += 1
    return diagWins

def main():
    # local variables
    test = [0,1,2,3,6]
    oldwins = 0
    newwins = 0
    playerWon = False
    moves = []

    # read input (file describing state of board)
    state = open("txt-files\output\state-output.txt", "r")
    List = state.readlines()
    for move in List:
        if move[4] == 'X':
            moves.append(int(move[1]))
    newwins = vertCheck(moves) + horiCheck(moves) + diagCheck(moves) # see 3 check functions above
    print(newwins)
    state.close()

    # read existing output (how many times player has won already)
    #input = open("txt-files\output\calc-reward-output.txt", "r")
    #input.readline() # "The player has won:"
    #oldwins = int(input.readline())

    # write to new output (output = input + newWins)
    output = open("txt-files\output\calc-reward-output.txt", "w")
    output.write("The player has won:\n")
    output.write(str(newwins) + "\n")
    output.write("times")
    output.close()

if __name__ == '__main__':
    main()