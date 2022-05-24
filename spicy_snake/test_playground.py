"""
Tests for the Playground class:

- after creating a Playground object it has the correct size attribute
- food should be inside the Playground size
- add_random_food puts the food in random positions
- food is not placed on obstacles (boundaries)

"""


from spicy_snake.playground import Playground
from sqlalchemy import true
from unittest.mock import MagicMock
import random

def test_create():
    """creating a Playground object works - which also works as on of our obstacles"""
    p = Playground(10,11)
    # after creating a Playground object it has the correct size attribute
    assert p.size == (10,11)

def test_is_obstacle():
    """
    - check for obstacles on the playground
    """
    p = Playground(5,6)
    assert p.is_obstacle((3,3)) is False
    assert p.is_obstacle((-1, -1)) is True
    assert p.is_obstacle((5, 6)) is True
    assert p.is_obstacle((0, 6)) is True
    assert p.is_obstacle((0, 0)) is True

def test_add_food():
    """- food should be inside the Playground size"""
    p = Playground(5,6)
    p.add_food((3,3))
    assert p.food == (3,3)

def test_add_food_playground():
    """
    - food should not be on the wall boundry 
    - food removed if an invalid position is given
    """
    p = Playground(5,6)
    p.add_food((3,3))
    assert p.food is not None
    p.add_food((0,0))
    assert p.food is None

def test_add_food_random(): # tests dont interfere because we add a playground that we dont have food in it
    """
    - place food in random positions 
    """
    p = Playground(5,6)
    p.add_random_food()
    assert p.food is not None

# check if the random food is actually random 
def test_add_food_random_mock():
    """
    - running MagicMock 
    """
    p = Playground(5,6)
    mm = MagicMock(return_value=4)
    random.randint = mm
    p.add_random_food()
    assert p.food == (4,4)
    assert mm.call_count == 2 