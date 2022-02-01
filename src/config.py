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
    scr.addstr(3, 2, 'To exit press Ctrl+C at any time ;)',\
         curses.color_pair(2))
    scr.addstr(5, 2, 'Press any key to begin a new Beautiful Empathy mural.',\
         curses.color_pair(3) | curses.A_BLINK)
    scr.refresh()
    c = scr.getch()
    scr.clear()
    return c

def get_num_players(scr):
    scr.addstr(1, 2, 'How many players will be joining the game? [1-20]')
    scr.addstr(2, 2, 'Enter a number and press any key.', curses.color_pair(2))
    scr.refresh()
    c = scr.getstr()
    while True:
        if c.isdigit():
            if int(c) in range(1,20):
                return int(c)
        scr.addstr(4, 2, 'Invalid value: '+c+'', curses.color_pair(2))
        scr.addstr(5, 2, 'Try again', curses.color_pair(1)| curses.A_BLINK)
        scr.refresh()
        c = scr.getstr()
    scr.clear()
    return 1




