from Questions import Questions
import tempfile
from Color_map import Color_map
from Mosaic import Mosaic
import random

class Game:

    def __init__(self,names,colors):
        self.questions = Questions()
        self.path = tempfile.mkdtemp(dir='./tmp_dirs')
        self.color_map = Color_map('circle_72',self.path)
        for name,color in zip(names,colors):
            self.color_map.add_color(name,color)
        self.mosaic = Mosaic(self.path,14,14,60)

    def player_add_color(self,player_name,color_id):
            self.color_map.add_color(player_name,color_id)

    def colors_player(self,name):
        cols_pl = {} 
        for c_id,color in self.color_map.colors.items():
            if color.player_name == name:
                cols_pl[c_id] = color
        return cols_pl

    def num_colors_player(self,name):
        count = 0 
        for c_id,color in self.color_map.colors.items():
            if color.player_name == name:
                count+=1
        return count

    def hex_colors_player(self,name):
        hexes = [] 
        for c_id,color in self.color_map.colors.items():
            if color.player_name == name:
                hexes.append(color.hex)
        return hexes

    def gets_new_color(self, hits, owned):
        if hits == 5:
            return True
        if owned < 4:
            return True
        else:
            return owned < hits+4
    
    def player_neighbour_colors(self,player_name, skip_unused = False):
        colors = self.color_map.neighbour_colors(player_name, skip_unused)
        return colors

    def assign_rand_init_colors(self,num_players, names_players):
        rand_init_colors = []
        for i in range(num_players):
            found = False
            while not found:
                c = random.randint(1,72)
                if self.color_map.colors[c].in_use:
                    continue
                break
            self.player_add_color(names_players[i].get(),c)
            rand_init_colors.append(c)
        return rand_init_colors

    def get_rand_shape(self, hits, owned):
        if owned < 4:
            if hits < 2:
                return {'c':2}
            elif hits < 4: 
                return {'c':4}
            else:#4 or 5 hits
                return {'c':6}
        elif 3 < owned < 7: 
            if hits < 2:
                return {'c':8}
            elif hits < 4: 
                return {'c':4,'C':2}
            else:#4 or 5 hits
                return {'c':8,'C':2}
        else:#owned 7 or more
            if hits < 2:
                return {'c':4,'C':2}
            elif hits < 4:
                return {'c':8,'C':2}
            else:#4 or 5 hits
                return {'c':16}

    def get_rand_question(self):
        #Failsafe. Cant know how many qs are.
        for i in range(1000):
            idx = random.choice(range(len(self.questions.list_of_q)))
            if not self.questions.list_of_q[idx].used:
                self.questions.list_of_q[idx].used = True
                return self.questions.list_of_q[idx]
        raise Exception("Runned out of questions. All used.")
