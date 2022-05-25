
from spicy_snake.playground import Playground
import curses


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

# ASCII codes of characters on the keyboards
KEY_COMMANDS = {97: LEFT, 100: RIGHT, 119: UP, 115: DOWN}
#TODO: use arrow keys instead

# prepare the screen
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.curs_set(0)
curses.noecho()
curses.raw()
screen.keypad(False)

win = curses.newwin(40, 15, 0, 0)
win.nodelay(True)


def game_loop(screen):
    x, y = 5, 5 # player position

    pg = Playground(30, 14)

    # draw
    screen.clear() #FIXME:redundance from line 52-59
    # draw the player
    screen.addch(y, x, "O", curses.color_pair(1))
    # draw playground
    for pgx in range(31):
        for pgy in range(15):
            if pg.is_obstacle((pgx, pgy)):
                screen.addch(pgy, pgx, "#", curses.color_pair(2))
    win.refresh()
    screen.refresh()

    while True:
        # move player around
        char = win.getch()
        direction = KEY_COMMANDS.get(char) # direction is a tuple or None
        if direction:
            dx, dy = direction
            x += dx
            y += dy
            #FIXME: name collision x and y


            # draw
            screen.clear() #FIXME:the order of these codes are different fromthe other one
            screen.addch(y, x, "O", curses.color_pair(1))
            for pgx in range(31):
                for pgy in range(15):
                    if pg.is_obstacle((pgx, pgy)):
                        screen.addch(pgy, pgx, "#", curses.color_pair(2))
            win.refresh() # FIXED: the order improved the code the wall does not disappear
            screen.refresh()


if __name__ == "__main__":

    curses.wrapper(game_loop)
    curses.endwin()