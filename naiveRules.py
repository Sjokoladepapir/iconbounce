# CONSTANTS, DO NOT CHANGE.
pass_through_hex =  8
bounce_v_hex = 4
bounce_h_hex = 2
end_of_path_hex = 1

# Defining 0, or false as down-left, and 1 as down-right.
dl = 0
dr = 1

def direction(row, column, world_type):
    is_odd = (row + column) % 2 == 1
    return 0 if (world_type == 1 and is_odd is True) or (world_type == 0 and is_odd is False) else 1


# Used to get the right range in the array. Any value outside is considered as 0
def lessClutter(r, c, obj):
    return len(obj.world) > r and len(obj.world[0]) > c and obj.world[r, c] and r >= 0 and c >= 0


def naive_stop_rules(obj, row, column, world_type):
    sum = 0
    # up_left corner
    if direction(row, column, world_type) is dr and \
            lessClutter(row - 1, column - 1, obj) == 0 and \
            lessClutter(row - 1, column, obj) == 0 and \
            lessClutter(row, column - 1, obj) == 0:
        #    print "up_left corner", row, column
        sum += end_of_path_hex

    # up_right corner
    if direction(row, column, world_type) is dl and \
            lessClutter(row - 1, column + 1, obj) == 0 and \
            lessClutter(row - 1, column + 2, obj) == 0 and \
            lessClutter(row, column + 2, obj) == 0:
        #    print "up_right corner", row, column
        sum += end_of_path_hex
    # down_left corner
    if direction(row, column, world_type) is dl and \
            lessClutter(row + 1, column - 1, obj) == 0 and \
            lessClutter(row + 2, column - 1, obj) == 0 and \
            lessClutter(row + 2, column, obj) == 0:
        #    print "up_right corner", row, column
        sum += end_of_path_hex
    # down_right corner
    if direction(row, column, world_type) is dr and \
            lessClutter(row + 1, column + 2, obj) == 0 and \
            lessClutter(row + 2, column + 1, obj) == 0 and \
            lessClutter(row + 2, column + 2, obj) == 0:
      #  print "up_right corner", row, column
        sum += end_of_path_hex
    return sum

    # works for less complicated worlds e.g. rectangles
def naive_bounce_rules(obj, row, column, world_type):
    # naive vbounce (right)
    sum = 0
    if direction(row, column, world_type) is dr and \
            lessClutter(row - 1, column - 1, obj) == 0 and \
            lessClutter(row, column - 1, obj) == 0 and \
            lessClutter(row + 1, column - 1, obj) == 0:
        #    print "bounce_v, dr", row, column
        sum += bounce_v_hex
    # naive vbounce dl (left)
    if direction(row, column, world_type) == dl and \
            lessClutter(row - 1, column + 2, obj) == 0 and \
            lessClutter(row, column + 2, obj) == 0 and \
            lessClutter(row + 1, column + 2, obj) == 0:
        #    print "bounce_v, dl", row, column
        sum += bounce_v_hex
    # naive hbounce dr (roof)
    if direction(row, column, world_type) is dr and \
            lessClutter(row - 1, column - 1, obj) == 0 and \
            lessClutter(row - 1, column, obj) == 0 and \
            lessClutter(row - 1, column + 1, obj) == 0:
        #    print "bounce_h, dr", row, column
        sum += bounce_h_hex
    # naive hbounce dl (floor)
    if direction(row, column, world_type) == dl and \
            lessClutter(row + 2, column - 1, obj) == 0 and \
            lessClutter(row + 2, column, obj) == 0 and \
            lessClutter(row + 2, column + 1, obj) == 0:
        #    print "bounce_h, dl", row, column
        sum += bounce_h_hex

    return sum