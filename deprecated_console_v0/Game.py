from image_edit import init_color_map, init_board
from PIL import Image, ImageFont, ImageDraw
from Color_map import Color_map
import random
import curses
import time
import subprocess
import tempfile

class Game:
        
    def __init__(self, scr, names, questions):
        self.scr = scr
        self.players = dict(zip(names,[[]]*len(names)))
        self.names = names
        self.questions = questions
        #self.qs = None
        self.color_map = Color_map()
        self.mosaic = Mosaic()#init_board()
        #self.tmp_dir_path = tempfile.mkdtemp()
        #need to creat classes for maps with persistence


    import tempfile

    def random_q(self):
        random.shuffle(self.questions.list_of_q)
        for q in self.questions.list_of_q:
            if q.used:
                continue
            q.used = True
            return q
        raise Exception('Runned out of questions')
         
    def show_board(self):
        #need to store a tmp file for every board and color map
        #either used as persistence, or being recomputed from
        #status of Game
        mosaic_view = subprocess.Popen(['eog', self.mosaic])
        return 

    def show_color_map(self):
        color_map_view = subprocess.Popen(['eog', self.color_map.path])
        return 

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
        self.scr.addstr(3, 2, 'Painter '+painter_name+' choose the word.',\
            curses.color_pair(4))
        self.scr.addstr(4, 2, 'Guesser '+guesser_name+' wait for '\
            +painter_name+' and make your guess.', curses.color_pair(4))
        question = self.random_q()
        empty_mask = question.q.replace('[MASK]','_______')
        self.scr.addstr(7,4,empty_mask)
        self.scr.addstr(9,12,question.v1+' / '+question.v2,curses.color_pair(3))
        self.scr.refresh()
        time.sleep(1)
        self.scr.addstr(12,2,'Press "H" if it was correctly guessed.'\
            ' Any other key otherwise', curses.color_pair(2) | curses.A_BLINK)
        self.scr.refresh()
        c = self.scr.getch()
        self.scr.clear()
        if c == ord('H'): 
            return 1
        else:
            return 0 

    def summary_question(self, last_hit, total_ques, q_num):
        self.scr.addstr(2, 2, 'Question number '+str(q_num)+'/'\
            +str(total_ques),curses.color_pair(4))
        if last_hit:
            self.scr.addstr(4, 2, 'Was CORRECTLY guessed :)')
        else:
            self.scr.addstr(4, 2, 'Was INCORRECTLY guessed :(')
        self.scr.addstr(6,2,'Press any key for the next question.',\
             curses.color_pair(2) | curses.A_BLINK)
        self.scr.refresh()
        c = self.scr.getch()
        self.scr.clear()
    
    def summary_last_question(self, last_hit, total_ques, total_hits):
        self.scr.addstr(2, 2, 'Last question...',curses.color_pair(4))
        if last_hit:
            self.scr.addstr(4, 2, 'Was CORRECTLY guessed :)')
        else:
            self.scr.addstr(4, 2, 'Was INCORRECTLY guessed :(')
        self.scr.addstr(6, 2, 'Total correct guesses: '+str(total_hits),\
             curses.color_pair(4))
        self.scr.addstr(8,2,'Press any key for paiting!.',\
             curses.color_pair(2) | curses.A_BLINK)
        self.scr.refresh()
        c = self.scr.getch()
        self.scr.clear()

    def who_is_who(self, painter_name):
        painter = self.players[painter_name]
        guesser_name, guesser = random.choice(list(self.players.items()))
        if len(self.players)>1:
            while guesser_name == painter_name:
                guesser_name, guesser = random.choice(list(self.players.items()))
        return guesser_name, guesser

    def ask_questions(self, total_questions, painter_name, guesser_name):
        hits = 0
        for question_num in range(1,total_questions+1):
            q_hit = self.print_question(question_num,painter_name,guesser_name)
            hits += q_hit
            if total_questions == question_num:
                self.summary_last_question(q_hit, total_questions, hits)
            else:
                self.summary_question(q_hit,total_questions,question_num)
        return hits

    def choose_color_scr(self, painter):
        scr.addstr(1, 2, 'Painter '+painter+' you can now choose a new color.')
        scr.addstr(2, 2, 'Your options are written on the color map, and'\
            ' include the numbers: '+str(), curses.color_pair(2))

    def choose_color(self, painter):
        owned_colors = self.players[painter]
        not_chosen = True
        while not_chosen:
            available_colors = []
            for owned_c in owned_colors:
                for edge in self.color_map.edge_list:
                    if owned_c in edge:
                        candidates  = [x for x in edge if x != owned_c]
                        available_colors.append([x for x in candidates if\
                             not self.color_map.colors[x].in_use])
            c = self.choose_color_scr(painter)
            self.color_map.colors[int(c)].in_use = True
            self.players[painter].append(int(c))
            not_chosen = False
        return

    def get_new_colors(self, painter, hits):
        num_owned_colors = len(self.players[painter])
        num_new_colors = 1
        if num_owned_colors < 6:
            num_new_colors = 2
        for i in range(num_new_colors):
            self.choose_color(painter)
        return        

    def play_round(self,round_num,painter_name):
        guesser_name, guesser = self.who_is_who(painter_name)
        self.init_round_info(painter_name,guesser_name)
        #Empathy
        hits = self.ask_questions(5, painter_name, guesser_name) 
        #Get new colors
        colors = self.get_new_colors(painter_name,hits)
        #Get shapes
        shapes = self.get_shapes(hits)        
        #Summary
        self.preprint_info(painter_name, hits, colors, shapes)
        #Beauty
        self.paint(painter_name, colors, shapes)
