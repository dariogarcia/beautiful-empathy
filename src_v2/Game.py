from Color_map import Color_map
from Mosaic import Mosaic
import tempfile
import subprocess
import random

class Game:

    def __init__(self,questions,names):
        self.questions = questions
        self.path = tempfile.mkdtemp(dir='./tmp_dirs')
        self.color_map = Color_map('circle_72',self.path)
        self.mosaic = Mosaic(self.path,14,14,60)
        self.players = names

    def show_color_map(self):
        color_map_tmp_file = self.color_map.get_updated_color_map_path()
        color_map_viewer = subprocess.Popen(['eog', color_map_tmp_file])
        return color_map_viewer

    def player_add_color(self,player_name,color_id):
            self.color_map.add_color(player_name,color_id)

    def show_mosaic(self):
        mosaic_tmp_file = self.mosaic.get_updated_mosaic_path(self.color_map.colors)
        mosaic_viewer = subprocess.Popen(['eog', mosaic_tmp_file])
        return mosaic_viewer

    def player_neighbour_colors(self,player_name):
        colors = self.color_map.neighbour_colors(player_name)
        return colors

    def get_rand_color(self):
        found = False
        while not found:
            c = random.randint(1,72)
            if self.color_map.colors[c].in_use:
                continue
            break
        return c

    def num_colors_player(self,name):
        count = 0
        for c_id,color in self.color_map.colors.items():
            if color.player_name == name:
                count+=1
        return count
