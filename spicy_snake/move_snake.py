
VALID_DIRECTIONS = {'left', 'up', 'down', 'right'}

def move(current_position, direction): 
    # defensive code: validity checks on input data
    assert direction in VALID_DIRECTIONS
    x, y = current_position
    if type(x) != int or type(y) != int:
        raise Exception("x and y have to be integers")
    # code that does the calculation
    if direction == "right":
        new_position = x+1, y
    elif direction == "up":
        new_position = x, y+1
    elif direction == "down":
        new_position = x, y-1
    else:
        new_position = x-1, y
    return new_position