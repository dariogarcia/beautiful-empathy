from image_edit import init_color_map, init_board
from PIL import Image, ImageFont, ImageDraw


class Game:
        
    def __init__(self, names, init_colors, questions, color_map):
        self.players = dict(zip(names,init_colors))
        self.qs = questions
        
        self.color_map = init_color_map(names,\
            [(x,y) for (x_loc,y_loc) in color_map.colors[init_colors]])
        self.mosaic = init_board()

    def show_board():
        d1 = ImageDraw.Draw(self.mosaic)
        font = ImageFont.truetype("../fonts/BeckyTahlia-MP6r.ttf", 80) 
        d1.text((10, 10),"test",(255,255,255),font=font)
        self.mosaic.show()
