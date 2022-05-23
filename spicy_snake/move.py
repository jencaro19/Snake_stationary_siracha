import curses


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

KEY_COMMANDS = {97: LEFT, 100: RIGHT, 119: UP, 115: DOWN}

# prepare the screen
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.curs_set(0)
curses.noecho()
curses.raw()
screen.keypad(False)

win = curses.newwin(80, 25, 0, 0)
win.nodelay(True)


def game_loop(screen):
    x, y = 5, 5

    # draw
    screen.clear()
    screen.addch(y, x, "O", curses.color_pair(1))
    win.refresh()
    screen.refresh()

    while True:

        char = win.getch()
        direction = KEY_COMMANDS.get(char)
        if direction:
            dx, dy = direction
            x += dx
            y += dy

            # draw
            screen.clear()
            screen.addch(y, x, "O", curses.color_pair(1))
            win.refresh()
            screen.refresh()


if __name__ == "__main__":

    curses.wrapper(game_loop)
    curses.endwin()
