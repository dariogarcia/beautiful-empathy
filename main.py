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
    stdscr.addstr(0, 0, 'Player 1: Press key to select starting color at rand.'
            , curses.color_pair(1))
    stdscr.refresh()
    c = stdscr.getch()
    #2
    rand_col_1 = random.randint(1,20)
    stdscr.clear()
    stdscr.addstr(0, 0, 'Player 1, your initial color is '+str(rand_col_1)
        , curses.color_pair(1))
    stdscr.addstr(2, 0, 'Player 2: Press key to select starting color at rand.'
            , curses.color_pair(1))
    c = stdscr.getch()
    #3
    rand_col_2 = random.randint(1,20)
    stdscr.clear()
    stdscr.addstr(0, 0, 'Player 1, your initial color is '+str(rand_col_1)
        , curses.color_pair(1))
    stdscr.addstr(2, 0, 'Player 2, your initial color is '+str(rand_col_2)
            , curses.color_pair(1))
    c = stdscr.getch()



def main(self):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
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
    
    #Game init
    game_init(stdscr)
    stdscr.clear()

    #Choose first color
    choose_color(stdscr)

    
    for round in range(5):
        play_round

    #End program
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


wrapper(main)
