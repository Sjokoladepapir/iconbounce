from worldBuilderTest import Rectangle
from naiveRules import *
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


class NaiveStateSpace():
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns


        # CONSTANTS, DO NOT CHANGE.
        self.pass_through_hex = 8
        self.bounce_v_hex = 4
        self.bounce_h_hex = 2
        self.end_of_path_hex = 1

        # Defining 0, or false as down-left, and 1 as down-right.
        self.dl = 0
        self.dr = 1

        #create the world
        self.world = np.full((rows - 1, columns - 1), 0)
        self.world0 = np.full((rows - 1, columns - 1), 0)
        self.world1 = np.full((rows - 1, columns - 1), 0)


    def world0_creation (self, obj):
        self.world0 = np.full((self.rows-1, self.columns-1), 0)
        for i in range(0, self.rows-1):
            for j in range(0,self.columns - 1):
                self.world0[i,j] = naive_bounce_rules(obj,i,j,0)
                self.world0[i,j] += naive_stop_rules(obj,i,j,0)
                #shitty hack
                self.world0[i,j] += 8 if self.world0[i,j] == 0 else 0
      #  print self.world0



    def world1_creation (self, obj):
        self.world1 = np.full((self.rows-1, self.columns-1), 0)
        for i in range(0, self.rows-1):
            for j in range(0,self.columns - 1):
                self.world1[i,j] = naive_bounce_rules(obj,i,j,1)
                self.world1[i,j] += naive_stop_rules(obj,i,j,1)
                #shitty hack
                self.world1[i,j] += 8 if self.world1[i,j] == 0 else 0
       # print self.world1

    # Hack? There is probably a better way of doing this thing. It will be used a lot.
    def is_valid_range(self, column, row):
        t = True
        try:
            a = self.world0[column, row]
        except:
            t = False
        return t

#rows, columns = 7, 7
#myWorld = Rectangle(rows, columns)
#a = NaiveStateSpace(rows,columns)
#myWorld.exclude_row(5)
#myWorld.makeSpace0()
#myWorld.exclude_single_value(1,0)
#print myWorld.world
#a.world0_creation(myWorld)
#a.world1_creation(myWorld)
