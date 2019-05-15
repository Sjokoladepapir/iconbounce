import numpy as np
from NaivecrossStateSpace import NaiveStateSpace
from worldBuilderTest import Rectangle
from naiveRules import direction

# import numpy as np
import pylab as pl
from matplotlib import collections as mc
import matplotlib.pyplot as plt

rows, columns = 14, 10
newWorld = Rectangle(rows, columns)
print(newWorld.world)
crossWorld = NaiveStateSpace(rows, columns)
crossWorld.world1_creation(newWorld)
crossWorld.world0_creation(newWorld)


# THIS WHOLE ALGORITHM IS SUBJECT TO CHANGE AFTER A NEW RULESET FOR CROSS SPACE IS IMPLEMENTED


# CONSTANTS, DO NOT CHANGE.
pass_through_hex = 8
bounce_v_hex = 4
bounce_h_hex = 2
end_of_path_hex = 1

dl = 0
dr = 1

def return_0_outside_2d_array(row, column, array):
    return len(array) > row and len(array[0]) > column and row >= 0 and column >= 0 and array[row, column]


def pass_through_rules(row, column, world_type, array):
    # new path
    return_flag = -1
    if array[row, column] == pass_through_hex or array[row, column] & end_of_path_hex == end_of_path_hex:
        if (return_0_outside_2d_array(row - 1, column + 1, array) == 0 or
                return_0_outside_2d_array(row - 1, column - 1, array) == 0):
            return_flag = 0

        # use existing path dl
        if array[row, column] != 0:
            if return_0_outside_2d_array(row - 1, column + 1, array) != 0 and direction(row, column, world_type) == dl:
                return_flag = 1
            # existing dr
            elif return_0_outside_2d_array(row - 1, column - 1, array) != 0 and direction(row, column,
                                                                                          world_type) == dr:
                return_flag = 2
        else:
            return_flag = -1
    return return_flag


def bounce_h_rules(row, column, world_type, array):
    if (array[row, column] & bounce_v_hex == bounce_v_hex) and (array[row, column] & bounce_h_hex == bounce_h_hex):
        return 2
    elif array[row, column] & bounce_h_hex == bounce_h_hex:
        return 1
    else:
        return 0


def bounce_v_rules(row, column, world_type, array):
    if array[row, column] & bounce_v_hex == bounce_v_hex:
        return 1
    else:
        return 0


def correct_paths(correct_path, wrong_path, path_array):
    for i in range(0, len(path_array)):
        for j in range(0, len(path_array[0])):
            if path_array[i, j] == wrong_path:
                path_array[i, j] = correct_path
    return path_array


def path_connect_rules(world_type, cross_space_array):
    path_world = np.full((rows - 1, columns - 1), 0)
    path_nr = 1
    for i in range(0, rows - 1):
        for j in range(0, columns - 1):
            # new path
            if pass_through_rules(i, j, world_type, cross_space_array) == 0:
                path_world[i, j] = path_nr
                path_nr += 1
            # existing path dl
            elif pass_through_rules(i, j, world_type, cross_space_array) == 1:
                path_world[i, j] = path_world[i - 1, j + 1]
            # existing path dr
            elif pass_through_rules(i, j, world_type, cross_space_array) == 2:
                path_world[i, j] = path_world[i - 1, j - 1]
            # Bounce!
            elif bounce_h_rules(i, j, world_type, cross_space_array) != 0:
                path_world[i, j] = path_world[i, j - 1]
                # Normal Bounce path correction
                if path_world[i, j] != return_0_outside_2d_array(i - 1, j + 1, path_world) and \
                        bounce_h_rules(i, j, world_type, cross_space_array) == 1:
                    path_world = correct_paths(path_world[i, j], return_0_outside_2d_array(i - 1, j + 1, path_world),
                                               path_world)
                # Corner Bounce path correction
                if path_world[i, j] != return_0_outside_2d_array(i - 1, j, path_world) and \
                        bounce_h_rules(i, j, world_type, cross_space_array) == 2:
                    path_world = correct_paths(path_world[i, j], return_0_outside_2d_array(i - 1, j, path_world),
                                               path_world)
                # if path_world[i, j] != return_0_outside_2d_array()
            elif bounce_v_rules(i, j, world_type, cross_space_array) == 1:
                path_world[i, j] = path_world[i - 1, j]
            else:
                path_world[i, j] = 0

    return path_world


path_world0 = path_connect_rules(0, crossWorld.world0)
path_world1 = path_connect_rules(1, crossWorld.world1)

# print(crossWorld.world1)
print(crossWorld.world0)
print(path_world1)
print(path_world0)


# MATPLOTLIB
def line_maker(row, column, world_type, path_array):
    # Converts between [row,column] and (x,y) coordinates:
    max_row = len(path_array) - 1
    x = column
    y = max_row - row
    if direction(row, column, world_type) == dr:
        return [(-0.5 + x, +0.5 + y), (0.5 + x, -0.5 + y)]
    else:
        return [(-0.5 + x, -0.5 + y), (0.5 + x, 0.5 + y)]


# todo
# instead of biggest number in path array, find how many unique paths there are instead, robust.
biggest_path_nr_w0 = 0
biggest_path_nr_w1 = 0
unique_paths_w0 = 0
unique_paths_w1 = 0

for i in range(0, len(path_world0)):
    for j in range(0, len(path_world0[0])):
        if path_world0[i, j] > biggest_path_nr_w0:
            biggest_path_nr_w0 = path_world0[i, j]
            unique_paths_w0 += 1
        if path_world1[i, j] > biggest_path_nr_w1:
            biggest_path_nr_w1 = path_world1[i, j]
            unique_paths_w1 += 1

print("biggest", biggest_path_nr_w0, biggest_path_nr_w1)
print("unique paths:", unique_paths_w0, unique_paths_w1)

line_arr = []
color_arr = []
for i in range(0, len(path_world0)):
    for j in range(0, len(path_world0[0])):
        # world 0
        co0 = path_world0[i, j] * 1.0 / biggest_path_nr_w0
        line_arr.append(line_maker(i, j, 0, path_world0))
        color_arr.append(([0.2, co0, co0, 1]))
        # world 1
        co0 = path_world1[i, j] * 1.0 / biggest_path_nr_w1
        line_arr.append(line_maker(i, j, 1, path_world1))
        color_arr.append(([co0, co0, 0.2, 1]))

lc = mc.LineCollection(line_arr, colors=color_arr, linewidths=2)

fig, ax = pl.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)
print("done")

plt.show()
