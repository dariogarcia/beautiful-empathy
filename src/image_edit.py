from PIL import Image, ImageFont, ImageDraw
import subprocess

def init_color_map():
    img = Image.open('../boards/map_1.png')
    return img

def paint_player(img, name, location):
    asdad
    d1 = ImageDraw.Draw(img)
    font = ImageFont.truetype("../fonts/BeckyTahlia-MP6r.ttf", 80)
    d1.text(location,name,(255,255,255),font=font)

def init_board():
    img = Image.open('../boards/initial_board.png')
    return img 

def show_color(color_hex):
    width = 400 
    height = 400 
    img  = Image.new( mode = "RGB", size = (width, height), color=color_hex)
    tmp_path = "/tmp/last_color.png"
    img.save(tmp_path,"PNG")
    color_viewer = subprocess.Popen(['eog', tmp_path])
    return color_viewer
