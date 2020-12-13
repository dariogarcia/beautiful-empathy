import csv
import curses
from curses import wrapper
import random

def read_questions(qs):
    with open('Questions - Sheet1.tsv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            qs[row[0].replace("mask","   ")] = (row[1],row[2])
            print(qs)

def game_init(stdscr):
    stdscr.addstr(0, 0, 'Welcome to Beautiful Empathy.\n'\
            '       Press a key to begin a new mural.'
            , curses.color_pair(1))
    stdscr.refresh()
    c = stdscr.getch()

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

def play_round(stdscr, num_round, questions):
    stdscr.addstr(0, 0, '---------------------------'
            , curses.color_pair(3))
    stdscr.addstr(1, 0, '---- Round number '+str(num_round+1)+'/5 -------'
            , curses.color_pair(3))
    stdscr.addstr(2, 0, '---------------------------'
            , curses.color_pair(3))
    stdscr.addstr(4, 0, '---------------------------'
            , curses.color_pair(3))
    stdscr.refresh()
    read_questions = []
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
    stdscr.addstr(6, 0, 'You guessed '+str(hits)+' out of 5.'
                , curses.color_pair(3))
    stdscr.addstr(7, 0, 'Hit any key for next round')
    c = stdscr.getch()


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
    game_init(stdscr)
    stdscr.clear()

    #Choose first color
    choose_color(stdscr)
    stdscr.clear()

    #Start playing rounds
    for round_num in range(15):
        play_round(stdscr,round_num,questions)

    #End program
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


wrapper(main)
