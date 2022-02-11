from image_edit import init_color_map, init_board
from PIL import Image, ImageFont, ImageDraw
from Color_map import Color_map

class Game:
        
    def __init__(self, names, color_map):
        self.players = dict(zip(names,[[]]*len(names)))
        self.names = names
        self.qs = None
        self.color_map = Color_map()
        self.mosaic = init_board()

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
        font = ImageFont.truetype("../fonts/Nivis-RYyl.ttf", 15)
        for name in self.names:
            for color in self.players[name]:
                d1.text(self.color_map.colors[color].coords, name,\
                     self.color_map.colors[color].text_col, font=font)
