#
# Automated test with pytest

"""
Automated test with PYTEST
(writing another program to test our application)

The discipline of TDD (Test-Driven-Development)
-----------------------------------------------

1. Write a test
2. Run the test and make sure it fails 
3. Write just enough code to make the test past
4. Run the test again and make sure it passes 
5. Clean up
6. Run the tests again(regression testing)
7. Back to step 1!!!!

look up: Uncle BOB "Clean Code Lectures"
"""

# feature can move in all 4 directions

from spicy_snake import move, VALID_DIRECTIONS
import pytest
import random

@pytest.mark.parametrize('position,direction,expected', [
    # data examples
    ((5, 5), 'left', (4, 5)),
    ((5, 5), 'right', (6, 5)),
    ((5, 0), 'left', (4, 0)),
    ((5, 5), 'up', (5, 6)),
    ((5, 5), 'down', (5, 4)),
    ((3, 3), 'left', (2, 3))
    # ((0, 5), 'left', (10, 5)) # only if we allow wraparound
])

def test_move(position, direction, expected):
    """the snake is moving in all 4 directions"""
    assert move(position, direction) == expected

def test_move_random():
    """test random positions"""
    # --> also see: hypothesis library
    for _ in range(100):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        direction = random.choice(list(VALID_DIRECTIONS))
        position = x, y
        move(position, direction)
    
def test_move_invalid_direction():
    with pytest.raises(Exception):
        move((1, 1), 'dummy')
   

def test_move_fraction():
    """An example of code that is not suppose to work"""
    position = (3.1458,5)
    with pytest.raises(Exception): # test will only pass if the exception is generated
        move(position, "down")

#TODO: check for the boundaries of the playing field

"""
here is the previous example of the code before reducing its size
------------------------------

def test_move_left():
    position = (5,5)
    new_position = move(position, "left")
    assert new_position == (4,5)            # makes sure that the condition is true or not --> throws and exception

def test_move_left_from_different_else():
    position = (5,0)
    new_position = move(position, "left")
    assert new_position == (4,0)

def test_move_right():
    position = (5,5)
    new_position = move(position, "right")
    assert new_position == (6,5)            

def test_move_up():
    position = (5,5)
    new_position = move(position, "up")
    assert new_position == (5,6)            

def test_move_down():
    position = (5,5)
    new_position = move(position, "down")
    assert new_position == (5,4)  
-------------------
the code was reduced to have a smaller script 
but does the same as these previous number of code lines
"""