import numpy as np


class Connection:
    def __init__(self, row, column, world_type):
        self.row = row
        self.column = column
        self.world_type = world_type
        self.

    # Used to check direction of this connection
    def direction(self):
        is_odd = (self.row + self.column) % 2 == 1
        return 0 if (self.world_type == 1 and is_odd is True) or (self.world_type == 0 and is_odd is False) else 1


a = Connection(0, 0, 1)
print a.direction()
