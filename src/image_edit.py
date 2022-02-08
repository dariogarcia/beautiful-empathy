from PIL import Image, ImageFont, ImageDraw

def init_color_map(names, colors):
    img = Image.open('../boards/map_1.png')
    d1 = ImageDraw.Draw(img)
    font = ImageFont.truetype("../fonts/BeckyTahlia-MP6r.ttf", 80)
    d1.text((10, 10),"test",(255,255,255),font=font)
    img.show()
    
def init_board():
    img = Image.open('../boards/initial_board.jpg')
    return img 

def show_color_map():
    img = Image.open('../boards/color_map.jpg')
    

def show_color(color_hex):
    width = 400 
    height = 400 
    img  = Image.new( mode = "RGB", size = (width, height), color=color_hex )
    img.show()
    return img

def add_name(name,color_id):
    img = Image.open('images/logo.jpg')
    d1 = ImageDraw.Draw(img)
    font = ImageFont.truetype("..Verdanab.ttf", 80)
    
    color(color_id)
    d1.text((10, 10),"test",(0,0,0),font=font)
    d1.text((0, 0), "text", font=myFont, fill =(255, 0, 0))
    img.show()
