# INPUT: a file describing the state of the board
# OUTPUT: a file with the number of times that the player has won (how many 3-in-a-rows)

# state of board
state = open("txt-files\output\state-output.txt", "r")
# TODO: if player has 3-in-a-row, increment wins
playerWon = False
state.close()

input = open("txt-files\output\calc-reward-output.txt", "r")
input.readline() # "The player has won:"
wins = int(input.readline())

if playerWon :
    wins += 1

output = open("txt-files\output\calc-reward-output.txt", "w")
output.write("The player has won:\n")
output.write(str(wins) + "\n")
output.write("times")
output.close()