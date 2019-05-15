from worldBuilderTest import Rectangle
from naiveRules import *
import numpy as np


#OLD but works. Will be replaced soon.


# Cross space is a transformation from icon space. Here instead of keepeing track of where
# icons are, it keeps track of the connections between icons.
# This space will further be used as for the path connecting algorithm.
# The path connecting algorithm always reads from left to right, and down.

# World0 and World1 will always contain different paths, that do not connect.
# Since 0 is defined as down-left, and world0 starts with 0 at [0,0],
# then all the paths that can happen in world 0 will follow the rule (rows+colums)%2=0.
# World1 will follow (rows+colums)%2=1, instead.
# An example of this would be if a 3*3 squeare is created.
# World1 would here contain the cross that forms, World0 would however contain the circular path.


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



    def world1_creation (self, obj):
        self.world1 = np.full((self.rows-1, self.columns-1), 0)
        for i in range(0, self.rows-1):
            for j in range(0,self.columns - 1):
                self.world1[i,j] = naive_bounce_rules(obj,i,j,1)
                self.world1[i,j] += naive_stop_rules(obj,i,j,1)
                #shitty hack
                self.world1[i,j] += 8 if self.world1[i,j] == 0 else 0