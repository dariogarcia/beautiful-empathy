from PIL import Image, ImageFont, ImageDraw

def show_color_map():
    img = Image.open('images/color_map.jpg')
    

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
    d1.text((10, 10),"test",(255,255,255),font=font)
    d1.text((0, 0), "text", font=myFont, fill =(255, 0, 0))
    img.show()
