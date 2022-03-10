from Game import Game
from Questions import Questions
import time
import random
from config import gets_new_color, gets_shape

#get players
names = ['asd','qwe']

#load questions
qs = Questions

#initialize game
gg = Game(qs,names)

#assign random colors to players
for n in names:
    c = gg.get_rand_color()
    gg.player_add_color(n,c)

#show color map
color_map_viewer = gg.show_color_map()
#color_map_viewer.kill()

#show empty mosaic
mosaic_viewer = gg.show_mosaic()
#mosaic_viewer.kill()

for i in range(5):
    for n in names:
        num_hits = random.randint(0,5)
        print('Hits:',num_hits)
        num_cols = gg.num_colors_player(n)
        print('Owned colors:',num_cols)
        if gets_new_color(num_hits,num_cols):
            avail = gg.player_neighbour_colors(n)
            print('NEW! choose:',n,avail)
            col = random.choice(avail)
            print('CHOSEN:',col)
            gg.player_add_color(n,col)
        shapes = gets_shape(num_hits,num_cols)
        print('Gets shape:',shapes)
        print('')
        time.sleep(3)
