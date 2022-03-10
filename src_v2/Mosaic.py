import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class Mosaic:

    def __init__(self,tmp_path,num_cells_x,num_cells_y,size_cell):
        self.path = tmp_path
        self.height = num_cells_x
        self.width = num_cells_y
        self.pix_per_sq = size_cell
        row = np.array([-1]*self.height*self.width)
        self.matrix = row.reshape(self.height,self.width)

    def create_empty_image(self):
        height = (self.height*self.pix_per_sq)+(self.height*1)+1
        width = (self.width*self.pix_per_sq)+(self.width*1)+1
        image = Image.new(mode='RGB', size=(height, width), color=255)
        return image

    def draw_lines(self,image):
        draw = ImageDraw.Draw(image)
        y_start = 0
        y_end = image.height
        step_size = int(image.width / self.height)
        for x in range(0, image.width+1, step_size):
            line = ((x, y_start), (x, y_end))
            draw.line(line, fill='#000000')
        x_start = 0
        x_end = image.width
        for y in range(0, image.height+1, step_size):
            line = ((x_start, y), (x_end, y))
            draw.line(line, fill='#000000')
        del draw
   
    def paint_colors(self, image, colors):
        draw = ImageDraw.Draw(image)
        for y, x in np.ndindex(self.matrix.shape):
            color_id = self.matrix[y, x]
            x_base = (x*self.pix_per_sq)+(x*1)+1
            y_base = (y*self.pix_per_sq)+(y*1)+1
            xy = [(x_base, y_base),\
                 (x_base+self.pix_per_sq-1, y_base+self.pix_per_sq-1)]
            draw.rectangle(xy, fill = colors[color_id].hex, outline=None, width=0) 
 
    def get_updated_mosaic_path(self, colors):
        image = self.create_empty_image()
        draw = self.draw_lines(image)
        draw = self.paint_colors(image, colors)
        tmp_file_path = os.path.join(self.path,'last_mosaic.png')
        image.save(tmp_file_path,'PNG')
        return tmp_file_path

    def paint_square(self,x,y,c):
        self.matrix[x,y] = c
