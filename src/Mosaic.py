import os
from PIL import Image, ImageDraw, ImageFont


class Mosaic:

    def __init__(self,storage_path,num_cells_x,num_cells_y,size_cell):
        #Initialize mosaic path and image
        self.storage_path = storage_path
        self.board_path = self.storage_path+'/last_mosaic.png'
        self.tmpboard_path = self.storage_path+'/last_mosaic_tmp.png'
        #Read, persist and load clear mosaic
        init_board = Image.open("../boards/initial_board.png")
        init_board.save(self.board_path,'PNG')
        init_board.save(self.tmpboard_path,'PNG')
        #Vars
        self.height = num_cells_x
        self.width = num_cells_y
        self.pix_per_sq = size_cell
        #row = np.array([-1]*self.height*self.width)
        #self.matrix = row.reshape(self.height,self.width)

    def store_mosaic(self):
        board_img = Image.open(self.board_path)
        board_img.save(self.board_path,'PNG')

    def persist_tmp(self):
        tmpboard_img = Image.open(self.tmpboard_path)
        tmpboard_img.save(self.board_path,'PNG')

    def scrap_tmp(self):
        board_img = Image.open(self.board_path)
        board_img.save(self.tmpboard_path,'PNG')
 
    def paint_square(self,x,y,c):
        scale = 62
        n_x = (int(x/(scale+1))*(scale+1))+int(x/(scale+1))+1
        n_y = (int(y/(scale+1))*(scale+1))+int(y/(scale+1))+1
        tmp_image = Image.open(self.tmpboard_path)
        draw = ImageDraw.Draw(tmp_image)
        xy = [(n_x, n_y), (n_x+scale, n_y+scale)]
        draw.rectangle(xy, fill = c, outline=None, width=0) 
        tmp_image.save(self.tmpboard_path,'PNG')

