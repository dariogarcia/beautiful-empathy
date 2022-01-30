def init_color_pairs():
    global curses
    import curses
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)

def welcome_screen(scr):
    #TODO: turn BE name into a colorful one character assignment
    scr.addstr(1, 2, 'Welcome to Beautiful Empathy.')
    scr.addstr(2, 2, '       A game by Dario')
    scr.addstr(3, 2, '       Ctrl+C to exit 8-O', curses.color_pair(2))
    #scr.addstr(3, 2, '       Press \'q\' at any time to exit.', curses.color_pair(3))
    scr.addstr(5, 2, 'Press any key to begin a new mural.', curses.color_pair(4)\
         | curses.A_BLINK)
    scr.refresh()
    c = scr.getch()
    return c
