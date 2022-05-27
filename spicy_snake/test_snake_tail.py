
import pytest
from spicy_snake.snake_tail import Snake
from spicy_snake.playground import Playground

#@pytest.mark.skip
def test_create_snake():
    """Check attributes"""
    s = Snake(5, 6)
    assert s.head == (5, 6)
    assert s.growing == 0
    # head counts as part of the tail
    assert len(s.tail) == 1

#@pytest.mark.skip
def test_move_snake():
    """Snake changes its position"""
    s = Snake(5, 6)
    s.forward()
    assert s.head == (6, 6)
    assert (6, 6) in s.tail
    assert len(s.tail) == 1

#@pytest.mark.skip
def test_snake_grows():
    """Check growth helper function"""
    s = Snake(5, 6)
    s.forward()
    s.grow()
    assert s.growing == 1

#@pytest.mark.skip
def test_tail_becomes_longer():
    """one move + eat once (.grow()) + one move, the tail becomes longer"""
    s = Snake(5, 6)
    s.forward()
    s.grow()
    s.forward()
    assert s.head == (7, 6)
    assert len(s.tail) == 2
    assert (6, 6) in s.tail
    assert (7, 6) in s.tail
    assert s.growing == 0


#@pytest.mark.skip
def test_collision():
    """Check collisions with obstacles"""
    p = Playground(10, 10)
    s = Snake(5, 5)
    for _ in range(4):
        s.forward()
        assert s.check_collision(p) is False
    s.forward()
    assert s.check_collision(p) is True


#@pytest.mark.skip
def test_eat():
    """Snake can eat food in the heads position"""
    p = Playground(10, 10)
    s = Snake(5, 5)
    p.add_food((6, 5))

    # picking up food increases growing by 1
    s.forward()
    s.eat(p)
    assert s.growing == 1

    # moving one more step makes the tail longer
    s.forward()
    assert s.growing == 0
    assert len(s.tail) == 2

#@pytest.mark.skip
def test_nothing_to_eat(): 
    """Snake cannot eat if the food is somewhere else - checks that the position is a relevant place"""
    p = Playground(10, 10)
    s = Snake(5, 5)
    p.add_food((1, 1))

    s.forward()
    s.eat(p)
    assert s.growing == 0


#@pytest.mark.skip
def test_tail_collision():
    """The snake hits its own tail"""
    p = Playground(10, 10)
    s = Snake(5, 5)
    
    # these are harmelse
    for d in ['right', 'up', 'left']:
        s.set_direction(d)
        s.grow()
        s.forward()
        assert s.check_collision(p) is False
    
    assert len(s.tail) == 4

    # now comes the move where the snake hits itself
    s.set_direction('down')
    s.grow()
    s.forward()
    assert s.check_collision(p) is True