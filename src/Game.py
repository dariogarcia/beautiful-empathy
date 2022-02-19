from image_edit import init_color_map, init_board
from PIL import Image, ImageFont, ImageDraw
from Color_map import Color_map
import random
import curses
import time

class Game:
        
    def __init__(self, scr, names, questions):
        self.scr = scr
        self.players = dict(zip(names,[[]]*len(names)))
        self.names = names
        self.questions = questions
        self.qs = None
        self.color_map = Color_map()
        self.mosaic = init_board()

    def random_q(self):
        random.shuffle(self.questions.list_of_q)
        for q in self.questions.list_of_q:
            if q.used:
                continue
            q.used = True
            return q
        raise Exception('Runned out of questions')
        
    def show_board(self):
        self.mosaic.show()

    def show_color_map(self):
        self.color_map.map.show()

    def update_color_players(self, players_names, all_players_colors):
        for player_name,player_colors in zip(players_names,all_players_colors):
            self.players[player_name] = self.players[player_name]+player_colors
            for color in player_colors:
                if self.color_map.colors[color].in_use == True:
                    raise Exception("Can't repeat color!")
                self.color_map.colors[color].in_use == True
        self.update_color_map()

    def update_color_map(self):
        d1 = ImageDraw.Draw(self.color_map.map)
        font = ImageFont.truetype("../fonts/Excludeditalic-jEr99.ttf", 15)
        for name in self.names:
            for color in self.players[name]:
                d1.text(self.color_map.colors[color].coords, name,\
                    self.color_map.colors[color].text_col, font=font)

    def init_round_info(self,painter_name,guesser_name):
        self.scr.border(curses.ACS_VLINE, curses.ACS_VLINE,
              curses.ACS_DIAMOND, curses.ACS_DIAMOND)    
        self.scr.addstr(2, 2, 'A round of empathy questions is a about to start.')
        self.scr.addstr(3, 10, 'Painter:'+painter_name,curses.color_pair(3))
        self.scr.addstr(4, 10, 'Guesser:'+guesser_name,curses.color_pair(3))
        self.scr.addstr(6, 2, 'Each question must first be read by the painter')
        self.scr.addstr(7, 2, painter_name+' must quickly & instinctively '\
            'choose the best fitting word.')
        self.scr.addstr(8, 2, 'The guesser ('+guesser_name+') can then guess'\
            ' which word the painter choose')
        self.scr.addstr(10, 2, 'Press any key to begin with the first sentence.',\
             curses.color_pair(2) | curses.A_BLINK)
        self.scr.refresh()
        c = self.scr.getch()
        self.scr.clear()

    def print_question(self, q_num, painter_name, guesser_name):
        self.scr.addstr(2, 2, 'Question number '+str(q_num),curses.color_pair(4))
        self.scr.addstr(3, 2, 'Painter '+painter_name+' chose the word.',\
            curses.color_pair(4))
        self.scr.addstr(4, 2, 'Guesser '+guesser_name+' wait for '\
            +painter_name+' and make your guess.', curses.color_pair(4))
        question = self.random_q()
        empty_mask = question.q.replace('[MASK]','_______')
        self.scr.addstr(7,4,empty_mask)
        self.scr.addstr(9,12,question.v1+' / '+question.v2,curses.color_pair(3))
        self.scr.refresh()
        time.sleep(10)
        self.scr.addstr(12,2,'Press "H" if it was correctly guessed.'\
            ' Any other key otherwise', curses.color_pair(2) | curses.A_BLINK)
        self.scr.refresh()
        c = self.scr.getch()
        self.scr.clear()
        if c == ord('H'): 
            return 1
        else:
            return 0 

    def play_round(self,round_num,painter_name):
        #Who's who
        painter = self.players[painter_name]
        guesser_name, guesser = random.choice(list(self.players.items()))
        if len(self.players)>1:
            while guesser_name == painter_name:
                guesser_name, guesser = random.choice(list(self.players.items()))
        self.init_round_info(painter_name,guesser_name)
        #Empathy
        hits = 0
        for question_num in range(5):
            hits += self.print_question(question_num,painter_name,guesser_name)
        self.summary_end_questions(self, hits, painter_name,guesser_name)
        deck = end_empathy_info(painter_name,painter,hits)
        draw_card(deck)
        paint()
