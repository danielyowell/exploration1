# given a file with a list of the actions played, produce a file that describes the state
#
# INPUT: a file with a list of actions played of the form (N, X) where N is a position from 0-8
# OUTPUT: a file describing the state of the board with 9 pairs of values of the form (N,P) 
#         where N is the position (0-8) and P is what is placed there (X or __ ) 

file1 = open("txt-files\input\\actions-input1.txt", "r")
file1.readline() # skip intro comment
print(file1.readlines())

file2 = open("txt-files\output\state-output.txt", "w")
file2.write("hello world")
file2.close()

file3 = open("txt-files\output\what-actions-output.txt", "w")
file3.write("hello again")
file3.close()