import curses

from spicy_snake.playground import Playground
from spicy_snake.screen_helper import prepare_screen

# definition of constants UPPERCASE
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

# ASCII codes of characters on the keyboards
KEY_COMMANDS = {97: LEFT, 100: RIGHT, 119: UP, 115: DOWN}
#KEY_COMMANDS = {27: LEFT, 26: RIGHT, 24:UP, 25: DOWN} #FIXME:windows arrow keys are not working

# symbols
SNAKE_SYMBOL = "0"
#SNAKE_SYMBOL = "0<"[(x+y)%2] switches off from both symbols from the result of the modualar
WALL_SYMBOL = "#"


def draw(player_pos, pg, win, screen): # we are not creating any new variables or information so we do not need to call the function
    screen.clear() 
    # draw the player
    #TODO: we could seperate the draw and draw_player into seperate function
    x, y = player_pos
    screen.addch(y, x, SNAKE_SYMBOL, curses.color_pair(1)) # making the symbol a variable
    # draw playground
    for pgx in range(pg.xsize + 1):
        for pgy in range(pg.ysize + 1):
            if pg.is_obstacle((pgx, pgy)):
                screen.addch(pgy, pgx, WALL_SYMBOL, curses.color_pair(2))
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
    player_position = 5, 5 # player position
    pg = Playground(30, 14)
    draw(player_position, pg, win, screen)

    while True:
        # move player around
        char = win.getch()
        direction = KEY_COMMANDS.get(char) # direction is a tuple or None # returns the code of a pressed key
        if direction:
            player_position = move_player(player_position, direction)

            # draw
            draw(player_position, pg, win, screen) # call back the draw screen function 

if __name__ == "__main__":
    curses.wrapper(game_loop)
    curses.endwin()