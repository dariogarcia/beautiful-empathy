from Questions import Questions
import tempfile
from Color_map import Color_map
from Mosaic import Mosaic
class Game:

    def __init__(self,names,colors):
        self.questions = Questions
        self.path = tempfile.mkdtemp(dir='./tmp_dirs')
        self.color_map = Color_map('circle_72',self.path)
        self.mosaic = Mosaic(self.path,14,14,60)
        self.players = names
        for name,color in zip(names,colors):
            self.color_map.add_color(name,color)


    def player_add_color(self,player_name,color_id):
            self.color_map.add_color(player_name,color_id)

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

    def gets_new_color(self, hits,owned):
        if owned < 4:
            return True
        elif hits==0:
            return False
        else:
            return owned < hits+4

    def player_neighbour_colors(self,player_name):
        colors = self.color_map.neighbour_colors(player_name)
        return colors

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
