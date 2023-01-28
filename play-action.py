# INPUT: two files, the state of the board, and a file with one action to be played
# OUTPUT: a file describe the new state of the board after the action has been played

import random

state = open("txt-files\output\state-output.txt", "r")
stateList = state.readlines()
print(stateList)

# DY: would it not be more efficient to pick a random element from what-actions-output.txt?
actionList = open("txt-files\output\what-actions-output.txt", "r")

# pick action
action = random.choice(actionList.readlines())
print(action)

# extract data
idx = action[1]
char = action[4]

oldPosition = "(" + str(idx) + ", _)"
newPosition = "(" + str(idx) + ", " + char + ")"

# copy old text from state.txt
state2 = open("txt-files\output\state-output.txt", "r")
content = state2.read()
content = content.replace(oldPosition, newPosition)
print("new content:")
print(content)

state.close()

state = open("txt-files\output\state-output.txt", "w")
state.write(content)
state.close()