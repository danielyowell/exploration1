# given a file describing the state, print out what actions are available to be played
# 
# INPUT: a file describing the state of the board like above
# OUTPUT: A file with a list of actions that can be played next (N,X)

input = open("txt-files\output\state-output.txt", "r")
list2 = input.readlines()
print(list2)

board = [False for i in range(9)] 
print(board)

idx = 0
for moves in list2:
    # print(moves[4])
    if moves[4] == "_":
        board[idx] = True
    idx += 1

print(board)

output = open("txt-files\output\what-actions-output.txt", "w")
for x in range(9):
    if(board[x]) :
        output.write( "(" + str(x) + ", O)\n")
output.close()