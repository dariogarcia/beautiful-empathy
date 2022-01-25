import curses
from curses import wrapper
import random

def read_questions(qs):
    with open('./data/questions_v0.tsv') as file:
        lines = file.readlines()
        lines = [line.split('\t')[0] for line in lines]
        qs[lines[0]]=(lines[1],lines[2])

def game_init(stdscr):
    stdscr.addstr(0, 0, 'Welcome to Beautiful Empathy.\n'\
            '       A game by Dario'
            '       Press \'q\' at any time to exit.'
            '       Press any key to begin a new mural.'
            , curses.color_pair(1))
    stdscr.refresh()
    c = stdscr.getch()
    return c

def choose_color(stdscr):
    #1
    stdscr.addstr(0, 0, 'Player 1: Press key to select starting random color.'
            , curses.color_pair(1))
    stdscr.refresh()
    c = stdscr.getch()
    #2
    rand_col_1 = random.randint(1,20)
    stdscr.clear()
    stdscr.addstr(0, 0, 'Player 1, your initial color is '+str(rand_col_1)
        , curses.color_pair(1))
    stdscr.addstr(2, 0, 'Player 2: Press key to select starting random color.'
            , curses.color_pair(1))
    c = stdscr.getch()
    #3
    rand_col_2 = random.randint(1,20)
    while rand_col_2 == rand_col_1 :
        rand_col_2 = random.randint(1,20)
    stdscr.clear()
    stdscr.addstr(0, 0, 'Player 1, your initial color is '+str(rand_col_1)
        , curses.color_pair(1))
    stdscr.addstr(2, 0, 'Player 2, your initial color is '+str(rand_col_2)
            , curses.color_pair(1))
    c = stdscr.getch()
    return c

def play_round(stdscr, num_round, questions, read_questions):
    stdscr.addstr(0, 0, '---------------------------'
            , curses.color_pair(3))
    stdscr.addstr(1, 0, '---- Round number '+str(num_round+1)+'/5 -------'
            , curses.color_pair(3))
    stdscr.addstr(2, 0, '---------------------------'
            , curses.color_pair(3))
    stdscr.addstr(4, 0, '---------------------------'
            , curses.color_pair(3))
    stdscr.clrtoeol()
    stdscr.refresh()
    stdscr.refresh()
    hits = 0
    for num_question in range(5):
        stdscr.addstr(3, 0, '---- Question number '+str(num_question+1)+'/5 ----'
                , curses.color_pair(3))
        stdscr.addstr(6, 0, 'Press any key for a sentence')
        stdscr.clrtoeol()
        stdscr.refresh()
        stdscr.addstr(8, 0, 'Sentence: ')
        stdscr.clrtoeol()
        stdscr.addstr(10, 0, 'Words: ')
        stdscr.clrtoeol()
        stdscr.refresh()
        c = stdscr.getch()
        if len(read_questions) == len(questions):
            stdscr.addstr(6, 0, 'You run out of questions. Game will end now :('
                , curses.color_pair(2))
            c = stdscr.getch()
            return
        found = False
        while not found: 
            question = random.choice(list(questions.keys()))
            if questions not in read_questions:
                found = True
        read_questions.append(question)
        stdscr.addstr(8, 0, question
                , curses.color_pair(1))
        stdscr.addstr(6, 0, 'Press any key for the two options')
        stdscr.clrtoeol()
        stdscr.refresh()
        c = stdscr.getch()
        stdscr.addstr(10, 10, questions[question][0]+' / '+questions[question][1]
                , curses.color_pair(1))
        stdscr.clrtoeol()
        stdscr.refresh()
        stdscr.addstr(6, 0, 'Press "H" if it was correctly guessed. Any other key otherwise')
        stdscr.clrtoeol()
        stdscr.refresh()
        c = stdscr.getch()
        if c == ord('H'):
            hits+=1

    stdscr.clear()
    stdscr.addstr(4, 0, 'You guessed '+str(hits)+' out of 5.'
        , curses.color_pair(3))
    if hits == 2:
        stdscr.addstr(4, 0, 'Get a new color if you own 2 or less.'
            , curses.color_pair(3))
    elif 2 < hits < 5:
        stdscr.addstr(4, 0, 'Get a new color if you own 4 or less.'
            , curses.color_pair(3))
    elif hits == 5:
        stdscr.addstr(4, 0, 'Get a new color! You ROCK!!!'
            , curses.color_pair(3))
    c = stdscr.getch()
    return hits, read_questions

def get_card(stdscr, hits):
    #Deck 1
    if hits < 2:
        dice = random.randint(0,9)
        if dice < 7:
            stdscr.addstr(6, 0, 'Your card is: 4c')
            stdscr.clrtoeol()
            stdscr.refresh()
            c = stdscr.getch()
        elif dice < 9:
            stdscr.addstr(6, 0, 'Your card is: 4c + 1C')
            stdscr.clrtoeol()
            stdscr.refresh()
            c = stdscr.getch()
        else:
            stdscr.addstr(6, 0, 'Your card is: 8c')
            stdscr.clrtoeol()
            stdscr.refresh()
            c = stdscr.getch()
    #Deck 2
    else:
        dice = random.randint(0,9)
        if dice < 2:
            stdscr.addstr(6, 0, 'Your card is: 8c')
            stdscr.clrtoeol()
            stdscr.refresh()
            c = stdscr.getch()

        elif dice < 6:
            stdscr.addstr(6, 0, 'Your card is: 4c + 2C')
            stdscr.clrtoeol()
            stdscr.refresh()
            c = stdscr.getch()

        elif dice < 9:
            stdscr.addstr(6, 0, 'Your card is: 8c + 2C')
            stdscr.clrtoeol()
            stdscr.refresh()
            c = stdscr.getch()

        else:
            stdscr.addstr(6, 0, 'Your card is: 16c')
            stdscr.clrtoeol()
            stdscr.refresh()
            c = stdscr.getch()

        if hits == 5:
            dice = random.randint(1,3)
            if dice == 1:
                stdscr.addstr(8, 0, 'Bonus: Gift any color to your companion.')
                stdscr.clrtoeol()
                stdscr.refresh()
                c = stdscr.getch()
            elif dice == 2:
                stdscr.addstr(8, 0, 'Bonus: Place 8c of any color.')
                stdscr.clrtoeol()
                stdscr.refresh()
                c = stdscr.getch()
            else :
                stdscr.addstr(8, 0, 'Bonus: Change 4 tiles on the board with any color')
                stdscr.clrtoeol()
                stdscr.refresh()
                c = stdscr.getch()

def check_quit(c):
    if c == ord('q'):
        return True
    return False

def main(self):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
    stdscr = curses.initscr()
    # Clear screen
    stdscr.clear()
    #No echo of keys in screen
    curses.noecho()
    #No enter needed to empty buffer
    curses.cbreak()
    #Parse keypad
    stdscr.keypad(True)
   
    questions = {}
    #Read questions file
    read_questions(questions)
    num_questions = len(questions)
    #Game init
    c = game_init(stdscr)
    if check_quit(c):
        return
    stdscr.clear()

    #Choose first color
    c = choose_color(stdscr)
    if check_quit(c):
        return
    stdscr.clear()

    #Start playing rounds
    done_questions = []
    for round_num in range(15):
        hits,done_questions = play_round(stdscr, round_num, questions, done_questions)
        get_card(stdscr, hits)

    #End program
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


wrapper(main)
