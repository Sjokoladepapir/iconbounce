from worldBuilderTest import Rectangle
from connections import Connection
import numpy as np


# Cross space is a transformation from normal space. Here instead of keepeing track of where
# icons are, it keeps track of the connections between icons.
# This space will further be used as for the path connecting algorithm.
# The path connecting algorithm always reads from left to rigth, and down. I assume it can only refer to
# paths already created, so this space will have to be created with that in mind.
# This space will therefore define most of the rules to the world
# Bounce Vertical, Bounce Horizontal, Passtrougth, Stop, and combinations of these, will be defined here.
# Not connected will probably be used.
# Split can potentially be split up, and implemented as a combination of passtrough
# and bounces in different nodes. This will however be one of the harder rules to implement.



#CONSTANTS, DO NOT CHANGE.
pass_through_hex =  8
bounce_v_hex = 4
bounce_h_hex = 2
end_of_path_hex = 1

# Defining 0, or false as down-left, and 1 as down-right.
dl = 0
dr = 1

# World0 and World1 will always contain different paths, that do not connect.
# Since 0 is defined as down-left, and world0 starts with 0 at [0,0],
# then all the paths that can happen in world 0 will follow the rule (rows+colums)%2=0.
# World1 will follow (rows+colums)%2=1, instead.
# An example of this would be if a 3*3 squeare is created.
# World1 would here contain the cross that forms, World0 would however contain the circular path.

# TODO
# Size will be original size -1 on both rows and columns. Smallest size will therefore be [1,1].
# This restriction could be implemented in the worldBuilder class
# The single 1 with 0 on it's four corners, cannot be defined here, and must be implemented elsewhere

rows, columns = 10, 10
myWorld = Rectangle(rows, columns)
#myWorld.exclude_row(5)
#myWorld.makeSpace0()
#myWorld.exclude_single_value(1,0)
print myWorld.world


#DL = 0
#DR = 1
def direction(row,column,world_type):
    is_odd = (row + column) % 2 == 1
    return 0 if (world_type == 1 and is_odd is True) or (world_type == 0 and is_odd is False) else 1

#Used to get the rigth range in the array. Any value outside is considered as 0
def lessClutter(r, c, obj):
    return obj.is_valid_range(r, c) and obj.world[r, c] and r >= 0 and c >= 0

#works for less complicated worlds e.g. rectangles
def naive_bounce_rules (obj,row,column,world_type):
    #naive vbounce (right)
    sum = 0
    if direction(row,column,world_type) is dr                   and \
            lessClutter(row - 1,    column - 1, obj) == 0       and \
            lessClutter(row,        column - 1, obj) == 0       and \
            lessClutter(row + 1,    column - 1, obj) == 0       :
    #    print "bounce_v, dr", row, column
        sum += bounce_v_hex
    #naive vbounce dl (left)
    if direction(row, column, world_type) == dl             and \
            lessClutter(row - 1 , column + 2, obj) == 0     and \
            lessClutter(row     , column + 2, obj) == 0     and \
            lessClutter(row + 1 , column + 2, obj) == 0     :
    #    print "bounce_v, dl", row, column
        sum += bounce_v_hex
    #naive hbounce dr (roof)
    if direction(row,column,world_type) is dr       and \
            lessClutter(row-1,column-1,obj) == 0    and \
            lessClutter(row-1,column,obj)   == 0    and \
            lessClutter(row-1,column+1,obj) == 0    :
    #    print "bounce_h, dr", row, column
        sum += bounce_h_hex
    #naive hbounce dl (floor)
    if direction(row, column, world_type)   == dl   and \
            lessClutter(row+2,column-1,obj) == 0    and \
            lessClutter(row+2,column,obj)   == 0    and \
            lessClutter(row+2,column+1,obj) == 0    :
    #    print "bounce_h, dl", row, column
        sum += bounce_h_hex

    return sum

def naive_stop_rules (obj,row,column,world_type):
    sum = 0
    #up_left corner
    if direction(row,column,world_type) is dr                       and \
            lessClutter(row - 1,    column - 1, obj)    == 0        and \
            lessClutter(row - 1,    column, obj)        == 0        and \
            lessClutter(row,    column - 1, obj)        == 0        :
    #    print "up_left corner", row, column
        sum += end_of_path_hex

    #up_right corner
    if direction(row,column,world_type) is dl                       and \
            lessClutter(row - 1,    column + 1, obj)    == 0        and \
            lessClutter(row - 1,    column + 2, obj)    == 0        and \
            lessClutter(row,    column + 2, obj)        == 0        :
    #    print "up_right corner", row, column
        sum += end_of_path_hex
    #down_left corner
    if direction(row,column,world_type) is dl                       and \
            lessClutter(row + 1,    column - 1, obj)    == 0        and \
            lessClutter(row + 2,    column - 1, obj)    == 0        and \
            lessClutter(row + 2,    column, obj)        == 0        :
    #    print "up_right corner", row, column
        sum += end_of_path_hex
    #down_right corner
    if direction(row,column,world_type) is dr                        and \
            lessClutter(row + 1,    column + 2 , obj)    == 0        and \
            lessClutter(row + 2,    column + 1 , obj)    == 0        and \
            lessClutter(row + 2,    column + 2, obj)     == 0        :
        print "up_right corner", row, column
        sum += end_of_path_hex
    return sum
#world 0 array.
#np.set_printoptions(formatter={'int':lambda x:hex(int(x))})
world0 = np.full((rows-1, columns-1), 0)
for i in range(0, rows-1):
    for j in range(0,columns - 1):
        world0[i,j] = naive_bounce_rules(myWorld,i,j,0)
        world0[i,j] += naive_stop_rules(myWorld,i,j,0)
        #shitty hack
        world0[i,j] += 8 if world0[i,j] == 0 else 0
print world0

#world 1 array
world1 = np.full((rows-1, columns-1), 0)
for i in range(0, rows-1):
    for j in range(0,columns - 1):
        world1[i,j] = naive_bounce_rules(myWorld,i,j,1)
        world1[i,j] += naive_stop_rules(myWorld,i,j,1)
        #shitty hack
        world1[i,j] += 8 if world1[i,j] == 0 else 0

#print world1

print ("funker dette")