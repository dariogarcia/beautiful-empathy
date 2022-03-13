import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class Mosaic:

    def __init__(self,tmp_path,num_cells_x,num_cells_y,size_cell):
        #Initialize mosaic path and image
        self.path = tmp_path
        self.img = Image.open("../boards/initial_board.png")
        self.tmp_img = Image.open("../boards/initial_board.png")
        file_path = os.path.join(self.path,'last_mosaic.png')
        self.img.save(file_path,'PNG')
        #Other vars
        self.height = num_cells_x
        self.width = num_cells_y
        self.pix_per_sq = size_cell
        #row = np.array([-1]*self.height*self.width)
        #self.matrix = row.reshape(self.height,self.width)

    #def create_empty_image(self):
    #    height = (self.height*self.pix_per_sq)+(self.height*1)+1
    #    width = (self.width*self.pix_per_sq)+(self.width*1)+1
    #    image = Image.new(mode='RGB', size=(height, width), color=255)
    #    return image

    #def draw_lines(self,image):
    #    draw = ImageDraw.Draw(image)
    #    y_start = 0
    #    y_end = image.height
    #    step_size = int(image.width / self.height)
    #    for x in range(0, image.width+1, step_size):
    #        line = ((x, y_start), (x, y_end))
    #        draw.line(line, fill='#000000')
    #    x_start = 0
    #    x_end = image.width
    #    for y in range(0, image.height+1, step_size):
    #        line = ((x_start, y), (x_end, y))
    #        draw.line(line, fill='#000000')
    #    del draw
   
    #def paint_colors(self, image, colors):
    #    draw = ImageDraw.Draw(image)
    #    for y, x in np.ndindex(self.matrix.shape):
    #        color_id = self.matrix[y, x]
    #        x_base = (x*self.pix_per_sq)+(x*1)+1
    #        y_base = (y*self.pix_per_sq)+(y*1)+1
    #        xy = [(x_base, y_base),\
    #             (x_base+self.pix_per_sq-1, y_base+self.pix_per_sq-1)]
    #        draw.rectangle(xy, fill = colors[color_id].hex, outline=None, width=0) 
    def store_mosaic(self):
        file_path = os.path.join(self.path,'last_mosaic.png')
        self.img.save(file_path,'PNG')

    def get_updated_mosaic_path(self):
    #    image = self.create_empty_image()
    #    draw = self.draw_lines(image)
    #    draw = self.paint_colors(image, colors)
         tmp_file_path = os.path.join(self.path,'last_mosaic_tmp.png')
    #     image.save(tmp_file_path,'PNG')
         return tmp_file_path

    def init_tmp_mosaic(self):
        file_path= os.path.join(self.path,'last_mosaic.png')
        self.tmp_img = Image.open(file_path)

    def paint_square(self,x,y,c):
        scale = 62
        n_x = (int(x/(scale+1))*(scale+1))+int(x/(scale+1))+1
        n_y = (int(y/(scale+1))*(scale+1))+int(y/(scale+1))+1
        draw = ImageDraw.Draw(self.tmp_img)
        xy = [(n_x, n_y), (n_x+scale, n_y+scale)]
        draw.rectangle(xy, fill = c, outline=None, width=0) 
        tmp_file_path = os.path.join(self.path,'last_mosaic_tmp.png')
        self.tmp_img.save(tmp_file_path,'PNG')

