from colors import COLORS
import random

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
    scr.addstr(2, 2, 'Enter a number and press any Enter.', curses.color_pair(2))
    scr.refresh()
    c = scr.getstr().decode(encoding="utf-8")
    while True:
        if c.isdigit():
            if int(c) in range(1,20):
                return int(c)
        scr.addstr(4, 2, c+' is not a number between 1 and 20...', curses.color_pair(2))
        scr.addstr(5, 2, 'Try again', curses.color_pair(1)| curses.A_BLINK)
        scr.refresh()
        c = scr.getstr().decode(encoding="utf-8")
    scr.clear()
    return 1

def get_names_players(scr,nplayers):
    names = []
    for i in range(nplayers):
        while True:
            scr.clear()
            scr.addstr(1, 2, 'Choose 3 characters that will represent their artist during the game')
            scr.addstr(3, 2, 'Player number '+str(i)+' please enter your 3'\
                +' characters and press Enter', curses.color_pair(2)| curses.A_BLINK)
            scr.refresh()
            c = scr.getstr().decode(encoding="utf-8")
            if len(c) != 3:
                continue
            scr.addstr(4, 3, c+' is correct? [y/n]', curses.color_pair(1))
            scr.refresh()
            c2 = scr.getstr().decode(encoding="utf-8")
            if c2 == 'y':
                names.append(c)
                break
    scr.clear()
    if len(names) != nplayers:
        raise Exception('Wrong number of player names recorded')
    return names

def choose_color(scr,names):
    colors = []
    scr.addstr(1, 2, 'Each player gets an randomly assigned,'\
        ' unique initial color')
    for n in names:
        scr.addstr(3, 2, n+ ' press any key for a random color.'\
            , curses.color_pair(2)| curses.A_BLINK)
        scr.refresh()
        c = scr.getch()
        color_id, color_hex = random.choice(list(COLORS.items()))
        while color_id in colors:
            color_id, color_hex = random.choice(list(COLORS.items()))
        colors.append(color_id)
        show_color(color_hex)
        scr.addstr((num_play*2), 0, n+', this is your initial color :) Press'\
            ' any key to continue', curses.color_pair(1))
        scr.refresh()
        c = scr.getch()
        if check_quit(c):
            return c
    #Goodbye
    scr.addstr((num_players*2)+1, 0, 'Initial color selection '\
        'complete' , curses.color_pair(2))
    scr.addstr((num_players*2)+2, 0, 'Locate yourself in the color '\
        'map, and get ready for the first round of empathy questions',\
        curses.color_pair(3))
    scr.addstr((num_players*2)+3, 0, 'Press any key to continue',\
        curses.color_pair(2))
    c = scr.getch()
    return c

