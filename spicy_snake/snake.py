import curses
import time

from spicy_snake.playground import Playground
from spicy_snake.screen_helper import prepare_screen
from spicy_snake.snake_tail import Snake

# definition of constants UPPERCASE
# LEFT = (-1, 0)
# RIGHT = (1, 0)
# UP = (0, -1)
# DOWN = (0, 1)

# ASCII codes of characters on the keyboards
KEY_COMMANDS = {97: 'left', 100: 'right', 119: 'down', 115: 'up'}
#KEY_COMMANDS = {27: LEFT, 26: RIGHT, 24:UP, 25: DOWN} #FIXME:windows arrow keys are not working

# symbols
SNAKE_SYMBOL = "0"
#SNAKE_SYMBOL = "0<"[(x+y)%2] switches off from both symbols from the result of the modualar
WALL_SYMBOL = "#"
HEAD_SYMBOL = "G"
FOOD_SYMBOL = '*'


def draw(snake, pg, win, screen): # we are not creating any new variables or information so we do not need to call the function
    # separate functions draw_player and draw_playground
    screen.clear()

    # draw the snake
    for x, y in snake.tail:
        screen.addch(y, x, SNAKE_SYMBOL, curses.color_pair(1)) # making the symbol a variable
    x, y = snake.head
    screen.addch(y, x, HEAD_SYMBOL, curses.color_pair(1))
    
    # draw the playground:
    for pgx in range(pg.xsize + 1):
        for pgy in range(pg.ysize + 1):
            if pg.is_obstacle((pgx, pgy)):
                screen.addch(pgy, pgx, WALL_SYMBOL, curses.color_pair(2))

    if pg.food:
        fx, fy = pg.food
        screen.addch(fy, fx, FOOD_SYMBOL, curses.color_pair(3))

    win.refresh()
    screen.refresh()

win, screen = prepare_screen()

def move_player(player_position, direction):
    dx, dy = direction
    x, y = player_position
    x += dx
    y += dy
    return x, y

def game_loop(screen):
    pg = Playground(30, 14)
    snake =Snake(5, 5)
    draw(snake, pg, win, screen)

    delay = 20000

    while not snake.check_collision(pg):
        # move the player
        char = win.getch() # returns the code of a pressed key
        direction = KEY_COMMANDS.get(char)  # direction is a tuple or None
        if direction:
            snake.set_direction(direction)

        delay -= 1
        if delay == 0:
            delay = 20000 
            snake.forward()
            snake.eat(pg)
            if not pg.food:
                pg.add_random_food()
            draw(snake, pg, win, screen)

    time.sleep(2)



if __name__ == "__main__":
    curses.wrapper(game_loop)
    curses.endwin()