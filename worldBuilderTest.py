import numpy as np


class Rectangle:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.world = np.full((self.row, self.column), 1)

    # function to exclude single values
    def exclude_single_value(self, row, column):
        self.world[row, column] = 0

    # function to exclude rows
    def exclude_row(self, row):
        self.world.T[..., row] = 0

    # function to exclude columns
    def exclude_column(self, column):
        self.world[..., column] = 0

    # function to include single values
    def include_single_value(self, row, column):
        self.world[row, column] = 1

    # function to include row
    def include_row(self, row):
        self.world.T[..., row] = 1

    # function to include columns
    def include_column(self, column):
        self.world[..., column] = 1

    #the following is mostly used for tests, as they create icon worlds where only one path world will have a path
    def makeSpace0(self):
        for i in range(self.row):
            for j in range(self.column):
                if (i == 0 and j == 0) or (i + j) % 2 == 0:
                    self.world[i, j] = 0

    def makeSpace1(self):
        for i in range(self.row):
            for j in range(self.column):
                if (i + j) % 2 == 1:
                    self.world[i, j] = 0
