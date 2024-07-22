from math import *

move = input().split(" ")
robotx = 0
roboty = 0

robotx += int(move[7])
robotx -= int(move[5])

roboty += int(move[1])
roboty -= int(move[3])

print(int(sqrt((roboty**2) + (robotx**2))))