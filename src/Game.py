from image_edit import init_color_map, init_board


class Game:
    from PIL import Image, ImageFont, ImageDraw
    class Player:
    
        def __init__(self, name, color):
            self.name = name
            self.colors = [color]
    
    def __init__(self, names, init_colors, questions, color_map):

        if len(names)!=len(init_colors):
            raise Exception('Num players and initial colors mismatch!')

        self.nplayers = len(names)
        self.qs = questions
        self.players = []

        for i,c in enumerate(zip(names, init_colors)):
            self.players.append(Player(c[0],c[1]))

        self.color_map = init_color_map(names, init_colors)
        self.mosaic = init_board()

    def show_board():
        d1 = ImageDraw.Draw(self.mosaic)
        font = ImageFont.truetype("../fonts/BeckyTahlia-MP6r.ttf", 80) 
        d1.text((10, 10),"test",(255,255,255),font=font)
        self.mosaic.show()
