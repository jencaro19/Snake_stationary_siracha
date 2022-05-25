import curses

def prepare_screen():
    """
    -- Initialize the screen --
    """
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
    return win, screen
