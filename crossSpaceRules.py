import numpy as np
#UNDER CONSTRUCTION, is not used at the moment now.
#This file is inteded to contain the rules which the creation of cross space uses.
#The cross space will apply each rule to each connection, and fit it there after.

# the rules are as follows: (some of these might be ambiguous, so they are up to change if that is the case)
# NC - a corner of a 0 will never be connected
# bounce - three zeroes in a row can initiate a bounce from the right ange and with some extra checks on zeroes around
# split - two zeroes in a row will create a split. THis is because if the path was in a bounce direction, then
# a bounce would happen, but from the bounces point of view, the bounce never happened.
# normal - this happens when there's no zeroes "behind" it, following standard down left/right

# Stop in general: Stop is defined at the last line segment before the path comes to a stop.
# edge stop - the final line segment before it crashes into a corner of a lonely zero
# bounce-stop - three zeroes and then an angeled edge stop.
# corner-stop - special case of bounce-stop. This is bouncestop * 2.
# Split stop - when a split was supposed to happen, but there is a zero  like in edge stop

# Uses a 2*2 array, if there is any zeroes, then a nc is detected, regardless of direction
def nc_check(core_array_2x2):
    if core_array_2x2.__contains__(0):
        return 1
    else:
        return 0

def nor_and_sum_array(array1, array2):
    #nors each element in the arrays, and sums up the remaining booleans to int
    return np.sum(np.logical_not(np.logical_or(array1,array2)))

def bounce_check(core_array_3x3):
    horizontal_bounce_check_array = np.array([[0,0,0],
                                              [1,1,1],
                                              [1,1,1]])

    nor_and_sum_hbca_up = nor_and_sum_array(core_array_3x3,horizontal_bounce_check_array)
    nor_and_sum_hbca_left = nor_and_sum_array(core_array_3x3,horizontal_bounce_check_array.transpose())
    nor_and_sum_hbca_down = nor_and_sum_array(core_array_3x3,np.flip(horizontal_bounce_check_array))
    nor_and_sum_hbca_right = nor_and_sum_array(core_array_3x3,np.flip(horizontal_bounce_check_array.transpose()))

    hex_sum = 0

    if nor_and_sum_hbca_up == 3:
        hex_sum += 1
    if nor_and_sum_hbca_left == 3:
        hex_sum += 2
    if nor_and_sum_hbca_down == 3:
        hex_sum += 4
    if nor_and_sum_hbca_right == 3:
        hex_sum += 8

    return hex_sum

def bounce_stop_check(core_array_3x3):
    horizontal_bounce_check_array = np.array([[0, 0, 0],
                                              [1, 1, 1],
                                              [1, 1, 0]])

    nor_and_sum_hbca_up = nor_and_sum_array(core_array_3x3, horizontal_bounce_check_array)
    nor_and_sum_hbca_left = nor_and_sum_array(core_array_3x3, horizontal_bounce_check_array.transpose())
    nor_and_sum_hbca_down = nor_and_sum_array(core_array_3x3, np.flip(horizontal_bounce_check_array))
    nor_and_sum_hbca_right = nor_and_sum_array(core_array_3x3, np.flip(horizontal_bounce_check_array.transpose()))

    print(horizontal_bounce_check_array)
    print(horizontal_bounce_check_array.transpose())
    print(np.flip(horizontal_bounce_check_array))
    print(np.flip(horizontal_bounce_check_array.transpose()))
    hex_sum = 0

    if nor_and_sum_hbca_up == 3:
        hex_sum += 1
    if nor_and_sum_hbca_left == 3:
        hex_sum += 2
    if nor_and_sum_hbca_down == 3:
        hex_sum += 4
    if nor_and_sum_hbca_right == 3:
        hex_sum += 8

    return hex_sum


print(bounce_stop_check(np.array([[0,0,0],[1,1,1],[1,1,1]])))
print(bounce_check(np.array([[1,1,0],[1,1,0],[0,0,0]])))
