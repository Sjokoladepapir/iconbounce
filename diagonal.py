from worldBuilderTest import Rectangle
import numpy as np


# TODO
# Find out what rules to the game apply
# Find a way to check each of them
# add check for diagonal values
#


# "GAMERULES"
# 1: One can only move diagonally
# 2: One bounces off walls, where there are

# Rules can potentially be boiled down to just two set of directions. If the algorithm that sees this just makes
# a note of all possiable ways, and connects paths to existing if it can.

def lessClutter(r, c, obj):
    return obj.is_valid_range(r, c) and obj.world[r, c] and r >= 0 and c >= 0


def rules_down_right(r, c, obj):
    # DownRight
    if lessClutter(r, c + 1, obj) == 0 and lessClutter(r + 1, c, obj) == 0 and lessClutter(r + 1, c + 1, obj) == 0:
        print "cornerStop"
    elif lessClutter(r, c + 1, obj) == 1 and lessClutter(r + 1, c, obj) == 1 and lessClutter(r + 1, c + 1, obj) == 0:
        print "edgeStop"
    elif lessClutter(r + 1, c + 1, obj) == 1:
        print "move to next normally"
    elif lessClutter(r+1,c+1,obj) == 0 and lessClutter(r-1,c-1,obj) == 0:
        print "noBounceStop"
    elif lessClutter(r, c + 1, obj) == 0 or lessClutter(r+1,c,obj) == 0:
        print "bounce"
    else:
        print "ERROR, I have no idea what happened"

def rules_down_left(r, c, obj):
    # DownRight
    if lessClutter(r, c - 1, obj) == 0 and lessClutter(r + 1, c, obj) == 0 and lessClutter(r + 1, c - 1, obj) == 0:
        print "cornerStop"
    elif lessClutter(r, c - 1, obj) == 1 and lessClutter(r + 1, c, obj) == 1 and lessClutter(r + 1, c - 1, obj) == 0:
        print "edgeStop"
    elif lessClutter(r + 1, c - 1, obj) == 1:
        print "move to next normally"
    elif lessClutter(r+1,c-1,obj) == 0 and lessClutter(r-1,c+1,obj) == 0:
        print "noBounceStop"
    elif lessClutter(r, c - 1, obj) == 0 or lessClutter(r+1,c,obj) == 0:
        print "bounce"
    else:
        print "ERROR, I have no idea what happened"

def rules_up_left(r, c, obj):
    # DownRight
    if lessClutter(r, c - 1, obj) == 0 and lessClutter(r - 1, c, obj) == 0 and lessClutter(r - 1, c - 1, obj) == 0:
        print "cornerStop"
    elif lessClutter(r, c - 1, obj) == 1 and lessClutter(r - 1, c, obj) == 1 and lessClutter(r - 1, c - 1, obj) == 0:
        print "edgeStop"
    elif lessClutter(r - 1, c - 1, obj) == 1:
        print "move to next normally"
    elif lessClutter(r-1,c-1,obj) == 0 and lessClutter(r+1,c+1,obj) == 0:
        print "noBounceStop"
    elif lessClutter(r, c - 1, obj) == 0 or lessClutter(r-1,c,obj) == 0:
        print "bounce"
    else:
        print "ERROR, I have no idea what happened"

def rules_up_right(r, c, obj):
    # DownRight
    if lessClutter(r, c + 1, obj) == 0 and lessClutter(r - 1, c, obj) == 0 and lessClutter(r - 1, c + 1, obj) == 0:
        print "cornerStop"
    elif lessClutter(r, c + 1, obj) == 1 and lessClutter(r - 1, c, obj) == 1 and lessClutter(r - 1, c + 1, obj) == 0:
        print "edgeStop"
    elif lessClutter(r - 1, c + 1, obj) == 1:
        print "move to next normally"
    elif lessClutter(r+1,c-1,obj) == 0 and lessClutter(r-1,c+1,obj) == 0:
        print "noBounceStop"
    elif lessClutter(r, c + 1, obj) == 0 or lessClutter(r-1,c,obj) == 0:
        print "bounce"
    else:
        print "ERROR, I have no idea what happened"

myWorld = Rectangle(4, 5)
row, column = 0, 0
myWorld.exclude_single_value(row, column)
#myWorld.exclude_single_value(row -1 , column )
print myWorld.world
rules_up_right(row,column,myWorld)
#print(myWorld.world)

print lessClutter(row,column-1,myWorld)



#print myWorld.world[row+1, column-1]