
class Player:

    def __init__(self, name, color):
        self.name = name
        self.colors = [color]

class Game:
    from Game import Player
    def __init__(self, names, init_colors, questions):

        if len(names)!=len(init_colors):
            raise Exception('Num players and initial colors mismatch!')

        self.nplayers = len(names)
        self.qs = questions
        self.players = []

        for i,c in enumerate(zip(names, init_colors)):
            self.players.append(Player(c[0],c[1]))
