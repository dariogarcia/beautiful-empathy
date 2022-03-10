import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

class BeautifulEmpathyApp():
    def __init__(self, root):
        self.root = root
        self.root.title('Beautiful Empathy')
        self.left_frame = None
        self.right_frame = None
        self.center_frame = None
        #set up visuals
        self.configure_main_window()
        self.create_containers()
        #vars
        self.current_window = 0
        self.num_players = None

    def configure_main_window(self):
        #center screen
        window_width = 1600
        window_height = 800
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
                
    def create_containers(self):
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.left_frame = tk.Frame(self.root, bg='cyan', width=600, height=600, pady=3)
        self.center_frame = tk.Frame(self.root, bg='pink', width=300, height=600, pady=3)
        self.right_frame = tk.Frame(self.root, bg='red', width=600, height=600, pady=3)
        self.left_frame.grid(row=0, column=0)
        self.center_frame.grid(row=0, column=1)
        self.right_frame.grid(row=0, column=2)
        
    def left_pane_widgets(self):
        cm_title = tk.Label(self.left_frame, text="Color Map")
        img_color_map= ImageTk.PhotoImage(Image.open("./tmp_dirs/tmplxo50eo3/last_color_map.png"))
        cm_img = tk.Label(self.left_frame, image = img_color_map,anchor='e')
        cm_title.grid(row=0,column=0)
        cm_img.grid(row=1,column=0)

    def right_pane_widgets(self):
        mo_title = tk.Label(self.right_frame, text="Mosaic")
        img_mosaic= ImageTk.PhotoImage(Image.open("./tmp_dirs/tmplxo50eo3/last_mosaic.png"))
        mo_img = tk.Label(self.right_frame, image = img_mosaic,anchor='w')
        mo_title.grid(row=0,column=0)
        mo_img.grid(row=1,column=0)

    def clear_center_frame(self):
       for widgets in self.center_frame.winfo_children():
          widgets.destroy()

    def show_next_screen(self,event):
        if  self.current_window == 0:
            self.num_players = int(event.widget.get())
            self.clear_center_frame()
            self.get_name_players()
           
    def get_num_players(self):
        title = tk.Label(self.center_frame, text="Enter number of painters")
        plist = [i+1 for i in range(6)]
        str_num = tk.StringVar()
        combo = ttk.Combobox(self.center_frame, values = plist)
        combo.bind('<<ComboboxSelected>>', self.show_next_screen)
        combo.pack(padx = 5, pady = 5)

    def get_name_players(self):
        title = tk.Label(self.center_frame, text="Enter painter name\n(3 characters max)")
        for i in range(self.num_players):
            painter = tk.Entry(self.center_frame, width = 5)
            painter.insert(0,'Player'+str(i)+'name')
            painter.pack(padx = 5, pady = 5)
        #add button
        #check thereturn an
        #raise_next func
        #return 1
    #combo.get()

root = tk.Tk()
beauty = BeautifulEmpathyApp(root)
beauty.get_num_players()

root.mainloop()
