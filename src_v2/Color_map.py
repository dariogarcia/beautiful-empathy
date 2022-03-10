from PIL import Image, ImageDraw, ImageFont
import os

class Color_map:

    def __init__(self, type_map, tmp_path):
        self.path = tmp_path
        if type_map == 'circle_72':
            import Circle72 as c72
            self.map = Image.open("../boards/map_1.png")
            self.colors = c72.get_initial_colors()
            self.edges = c72.get_initial_edges()
        else:
            raise Exception('Type of map not recognized:'+type_map)

    def get_updated_color_map_path(self):
        d1 = ImageDraw.Draw(self.map)
        font = ImageFont.truetype("../fonts/Excludeditalic-jEr99.ttf", 15)
        for c_id, color in self.colors.items():
            if color.player_name != None:
                d1.text(self.colors[c_id].coords, color.player_name,\
                    self.colors[c_id].text_col, font=font)
        tmp_file_path = os.path.join(self.path,'last_color_map.png')
        self.map.save(tmp_file_path,'PNG')
        return tmp_file_path   

    def add_color(self, player_name, color_id):
        if self.colors[color_id].in_use:
            raise Exception('Color already in use:'+color_id)
        self.colors[color_id].in_use = True
        self.colors[color_id].player_name = player_name

    def owned_colors(self, player_name):
        available = []
        for c_id, color in self.colors.items():
            if color.player_name == player_name:
                available.append(c_id)
        return available

    def neighbour_colors(self, player_name):
        owned = self.owned_colors(player_name)
        candidates = []
        for (c1,c2) in self.edges:
            if c1 in owned and c2 not in owned:
                candidates.append(c2)
            if c2 in owned and c1 not in owned:
                candidates.append(c1)
        return candidates
