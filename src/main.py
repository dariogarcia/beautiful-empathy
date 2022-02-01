import curses
global curses
from curses import wrapper
import random
from config import welcome_screen, init_color_pairs, get_num_players
from Questions import Questions
from Game import Player, Game

def choose_color(scr,num_players):
#Asigns num_players random values between 1 and 20
#Does not repeat values
#num_players max is between 1 and 20. Forced to it.
    if num_players<1:
        num_players==1
    if num_players>20:
        num_players==20
    chosen_colors = []
    #Assigning unique random initial numbers
    scr.addstr(0, 0, 'Total Players: '+str(num_players)\
        , curses.color_pair(1))
    for num_play in range(1,num_players+1):
        scr.addstr((num_play*2)-1, 0, 'Player '+str(num_play)+': Press any'\
            ' key to select starting random color.', curses.color_pair(1))
    	scr.refresh()
    	c = scr.getch()
        if check_quit(c):
            return c
    	rand_col = random.randint(1,20)
        while rand_col in chosen_colors:
    	   rand_col = random.randint(1,20)
        chosen_colors.append(rand_col)
        scr.addstr((num_play*2), 0, 'Player '+str(num_play)+', your '\
            'initial color is '+str(rand_col)+'. Press any key to continue'\
             , curses.color_pair(1))
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


def play_round(scr, num_round, questions, read_questions):
    scr.addstr(0, 0, '---------------------------'
            , curses.color_pair(3))
    scr.addstr(1, 0, '---- Round number '+str(num_round+1)+'/5 -------'
            , curses.color_pair(3))
    scr.addstr(2, 0, '---------------------------'
            , curses.color_pair(3))
    scr.addstr(4, 0, '---------------------------'
            , curses.color_pair(3))
    scr.clrtoeol()
    scr.refresh()
    scr.refresh()
    hits = 0
    for num_question in range(5):
        scr.addstr(3, 0, '---- Question number '+str(num_question+1)+'/5 ----'
                , curses.color_pair(3))
        scr.addstr(6, 0, 'Press any key for a sentence')
        scr.clrtoeol()
        scr.refresh()
        scr.addstr(8, 0, 'Sentence: ')
        scr.clrtoeol()
        scr.addstr(10, 0, 'Words: ')
        scr.clrtoeol()
        scr.refresh()
        c = scr.getch()
        
        #scr.addstr(6, 0, questions[0])
        #scr.clrtoeol()
        #scr.refresh()
        #c = scr.getch()
        
        for quest in questions.list_of_q:
            scr.addstr(8, 0, quest.q
                    , curses.color_pair(1))
            scr.addstr(6, 0, 'Press any key for the two options')
            scr.clrtoeol()
            scr.refresh()
            c = scr.getch()
            scr.addstr(10, 10, quest.v1+' / '+quest.v2
                    , curses.color_pair(1))
            scr.clrtoeol()
            scr.refresh()
            scr.addstr(6, 0, 'Press "H" if it was correctly guessed. Any other key otherwise')
            scr.clrtoeol()
            scr.refresh()
            c = scr.getch()
            if c == ord('H'):
                hits+=1

    scr.clear()
    scr.addstr(4, 0, 'You guessed '+str(hits)+' out of 5.'
        , curses.color_pair(3))
    if hits == 2:
        scr.addstr(4, 0, 'Get a new color if you own 2 or less.'
            , curses.color_pair(3))
    elif 2 < hits < 5:
        scr.addstr(4, 0, 'Get a new color if you own 4 or less.'
            , curses.color_pair(3))
    elif hits == 5:
        scr.addstr(4, 0, 'Get a new color! You ROCK!!!'
            , curses.color_pair(3))
    c = scr.getch()
    return hits, read_questions

def get_card(scr, hits):
    #Deck 1
    if hits < 2:
        dice = random.randint(0,9)
        if dice < 7:
            scr.addstr(6, 0, 'Your card is: 4c')
            scr.clrtoeol()
            scr.refresh()
            c = scr.getch()
        elif dice < 9:
            scr.addstr(6, 0, 'Your card is: 4c + 1C')
            scr.clrtoeol()
            scr.refresh()
            c = scr.getch()
        else:
            scr.addstr(6, 0, 'Your card is: 8c')
            scr.clrtoeol()
            scr.refresh()
            c = scr.getch()
    #Deck 2
    else:
        dice = random.randint(0,9)
        if dice < 2:
            scr.addstr(6, 0, 'Your card is: 8c')
            scr.clrtoeol()
            scr.refresh()
            c = scr.getch()

        elif dice < 6:
            scr.addstr(6, 0, 'Your card is: 4c + 2C')
            scr.clrtoeol()
            scr.refresh()
            c = scr.getch()

        elif dice < 9:
            scr.addstr(6, 0, 'Your card is: 8c + 2C')
            scr.clrtoeol()
            scr.refresh()
            c = scr.getch()

        else:
            scr.addstr(6, 0, 'Your card is: 16c')
            scr.clrtoeol()
            scr.refresh()
            c = scr.getch()

        if hits == 5:
            dice = random.randint(1,3)
            if dice == 1:
                scr.addstr(8, 0, 'Bonus: Gift any color to your companion.')
                scr.clrtoeol()
                scr.refresh()
                c = scr.getch()
            elif dice == 2:
                scr.addstr(8, 0, 'Bonus: Place 8c of any color.')
                scr.clrtoeol()
                scr.refresh()
                c = scr.getch()
            else :
                scr.addstr(8, 0, 'Bonus: Change 4 tiles on the board with any color')
                scr.clrtoeol()
                scr.refresh()
                c = scr.getch()

def check_quit(c):
    if c == ord('q'):
        return True
    return False

def main(self):
    q = Questions()
    global curses
    scr = curses.initscr()
    # Clear screen, add border
    scr.clear()
    scr.border(curses.ACS_VLINE, curses.ACS_VLINE,
              curses.ACS_DIAMOND, curses.ACS_DIAMOND)
    #No echo of keys, cbreak mode & keypad parse
    #curses.noecho()
    #curses.cbreak()
    #scr.keypad(True)
    
    #Initialize colors & read questions 
    init_color_pairs()
    qs = Questions()

    #Welcome Screen
    c = welcome_screen(scr)
    #Player Definition
    n = get_num_players(scr)
    names = get_names_players(scr)
    #First color
    c = get_first_color(scr,n)
    if check_quit(c):
        return
    scr.clear()

    names = ['A']
    init_colors = [1]

    #Create Game
    gg = Game(names, init_colors, qs)

    #Start playing rounds
    for round_num in range(15):
        hits,done_questions = play_round(scr, round_num, q, done_questions)
        get_card(scr, hits)

    #End program
    curses.nocbreak()
    scr.keypad(False)
    curses.echo()
    curses.endwin()

if __name__ == '__main__':
    wrapper(main)
