import curses
global curses
from curses import wrapper
from config import welcome_screen, init_font_color_pairs, get_num_players, get_names_players, choose_color
from Questions import Questions
from Game import Game


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
        scr.addstr(4, 0, 'Get a new color if you own 3 or less.'
            , curses.color_pair(3))
    elif hits == 3:
        scr.addstr(4, 0, 'Get a new color if you own 4 or less.'
            , curses.color_pair(3))
    elif hits == 4:
        scr.addstr(4, 0, 'Get a new color if you own 5 or less.'
            , curses.color_pair(3))
    elif hits == 5:
        scr.addstr(4, 0, 'Get a new color! Your empathy ROCKS!!!'
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

def main(self):
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
    init_font_color_pairs()
    qs = Questions()

    #Welcome Screen
    welcome_screen(scr)
    #Player Definition
#n = get_num_players(scr)
#names = get_names_players(scr,n)
    n = 12
    names = ["037","038","039","040","041","042","043","044","045","046","047","048"]
    #Create Game
    gg = Game(names, qs)
    
    #Get & update with first color
    #init_colors = choose_color(scr, names, gg.color_map)
    init_colors = [[37],[38],[39],[40],[41],[42],[43],[44],[45],[46],[47],[48]]
    #init_colors = [[13],[14],[15],[16],[17],[18],[19],[20],[21],[22],[23],[24]]
    gg.update_color_players(names,init_colors)
    
    #Show color map
    gg.show_color_map()
    #Show board
    #gg.show_board()



    #Start playing rounds
    done_questions = []
    for round_num in range(15):
        hits,done_questions = play_round(scr, round_num, qs, done_questions)
        get_card(scr, hits)

    #End program
    curses.nocbreak()
    scr.keypad(False)
    curses.echo()
    curses.endwin()

if __name__ == '__main__':
    wrapper(main)
