import tkinter as tk
from tkinter import ttk, IntVar, StringVar, PhotoImage
import random
from BeautifulEmpathy import Game

MAX_PLAYERS=6
NUM_ROUNDS=10
NAME_LEN_LIM=3
WINDOW_WIDTH=1800
WINDOW_HEIGHT=900

class BeautifulEmpathyApp():

    def __init__(self, root):
        #set tk objects
        self.root = root
        self.root.title('Beautiful Empathy')
        self.top_frame = None
        self.top_canvas = None
        self.left_frame = None
        self.left_canvas = None
        self.right_frame = None
        self.right_canvas = None
        self.center_frame = None
        #set tk config
        self.configure_main_window()
        self.create_containers()
        self.top_frame_widgets()
        self.left_frame_widgets()
        self.right_frame_widgets()
        #game vars
        self.game = None
        self.num_players = None
        self.names_players = []
        self.init_colors = []
        self.current_player_name = None
        self.current_round = None
        self.num_hits = None
        self.current_shapes = None 
        #game widgets
        self.combo_num_players = None

    def configure_main_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2-WINDOW_WIDTH/2)
        center_y = int(screen_height/2-WINDOW_HEIGHT/2)
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}')
    
    def create_containers(self):
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.top_frame = tk.Frame(self.root, bg='white', width=1600, height=200)
        self.left_frame = tk.Frame(self.root, bg='black', width=500, height=900)
        self.center_frame = tk.Frame(self.root, bg='white', width=200, height=900)
        self.right_frame = tk.Frame(self.root, bg='black', width=900, height=900)
        self.top_frame.grid(row=0, column=0, columnspan=3)
        self.left_frame.grid(row=1, column=0)
        self.center_frame.grid(row=1, column=1)
        self.right_frame.grid(row=1, column=2)

    def top_frame_widgets(self):
        self.title_canvas = tk.Canvas(self.top_frame, width = 1000, height = 200)
        self.title_canvas.pack(fill='both', expand = True)
    
    def update_top_frame_widgets(self):
        self.title_canvas.create_text(250,50, text="BEAUTIFUL EMPATHY", fill="purple", font=('Helvetica 25 bold'))
        self.title_canvas.pack()
        if self.current_round != None:
            self.title_canvas.create_text(500, 50, text="Round Number:", fill="black")
            self.title_canvas.pack()
    
    def left_frame_widgets(self):
        self.left_canvas = tk.Canvas(self.left_frame, width = 600, height = 600)
        self.left_canvas.pack(fill='both', expand = True)
        img_color_map = PhotoImage(file = '../boards/map_1.png')
        root.base_color_map = img_color_map
        self.left_canvas.create_image(10,0,image=img_color_map,anchor = "nw")
    
    def update_left_frame_widgets(self):
        img_color_map = PhotoImage(file = self.game.color_map.get_updated_color_map_path())
        root.base_color_map = img_color_map
        self.left_canvas.create_image(10,0,image=img_color_map,anchor = "nw")

    def right_frame_widgets(self):
        self.right_canvas = tk.Canvas(self.right_frame, width = 900, height = 900)
        self.right_canvas.pack(fill='both', expand = True)
        mosaic = PhotoImage(file = '../boards/initial_board.png')
        root.base_mosaic = mosaic
        self.right_canvas.create_image(0,50,image=mosaic,anchor = "nw")
    
    def update_right_frame_widgets(self):
        img_mosaic = PhotoImage(file = self.game.mosaic.get_updated_mosaic_path())
        root.base_mosaic = img_mosaic
        self.right_canvas.create_image(0,50,image=img_mosaic,anchor = "nw")

    def clear_center_frame(self):
       for widgets in self.center_frame.winfo_children():
          widgets.destroy()
 
    def check_names(self, var, index, mode):
        for idx, val in enumerate(self.names_players):
            string_name = self.names_players[idx].get()[:NAME_LEN_LIM]
            self.names_players[idx].set(string_name)
            for prev_name in self.names_players[:idx]:
                if string_name == prev_name.get():
                    self.names_players[idx].set("")

    def assign_rand_init_colors(self):
        for i in range(self.num_players):
            found = False
            while not found:
                c = random.randint(1,72)
                if self.game.color_map.colors[c].in_use:
                    continue
                break
            self.game.player_add_color(self.names_players[i].get(),c)
            self.init_colors.append(c)

    def create_game(self):
        self.game = Game(self.names_players,self.init_colors)

   ###################
   ##### SCREENS ##### 
   ###################

    def init_screen(self):
        main_title = tk.Label(self.center_frame, text="BEAUTIFUL EMPATHY\n\
            A game of feeling others while paiting together")
        main_title.pack()
        self.update_top_frame_widgets()
        self.get_num_players()

    def get_num_players(self):
        title = tk.Label(self.center_frame, text="How many painters will"\
            " be joining us today?")
        title.pack()
        plist = [i+1 for i in range(MAX_PLAYERS)]
        self.num_players = IntVar()
        self.combo_num_players = ttk.Combobox(self.center_frame,\
             values = plist)
        self.combo_num_players.bind('<<ComboboxSelected>>',\
             self.get_name_players)
        self.combo_num_players.pack(padx = 5, pady = 5)

    def get_name_players(self,event=None):
        self.num_players = int(self.combo_num_players.get())
        self.clear_center_frame()
        self.names_players = [None]*self.num_players
        warning = tk.Label(self.center_frame, text="Enter painter names\n"\
            "(3 characters MAX)")
        warning.pack()
        for i in range(self.num_players):
            name_label = tk.Label(self.center_frame, text="Player "+str(i+1))
            name_label.pack()
            self.names_players[i] = StringVar()
            name_entry = tk.Entry(self.center_frame, bg="white", fg="black",\
                 textvariable=self.names_players[i])
            name_entry.pack()
            self.names_players[i].trace('w', self.check_names)
        submit_button = tk.Button(self.center_frame, text="Next",\
             command=self.show_colors_players)
        submit_button.pack()

    def show_colors_players(self):
        for name in self.names_players:
            if len(name.get())<1:
                return
        self.clear_center_frame()
        self.assign_rand_init_colors()
        for name,color in zip(self.names_players,self.init_colors):
            if len(name.get())<1:
                return
            name_label = tk.Label(self.center_frame, text="Player "+\
                name.get()+", this is your color")
            name_label.pack()
            tk.Label(self.center_frame, width = 20, background=\
                self.game.color_map.colors[color].hex).pack()
        self.update_left_frame_widgets()
        nx_btn = tk.Button(self.center_frame, text="Next",\
             command=self.game_type_screen)
        nx_btn.pack()
    
    def game_type_screen(self):
        self.clear_center_frame()
        info_label = tk.Label(self.center_frame, text="Which type of game you want to play?")
        info_label.pack()
        both_button = tk.Button(self.center_frame, text="Beauty & Empathy")
        both_button.pack()
        only_button = tk.Button(self.center_frame, text="Beauty only",\
             command=self.start_game)
        only_button.pack()

    def start_game(self):
        self.current_round = 0
        self.play_new_round()

    def play_new_round(self):
        self.current_player_name = self.names_players[self.current_round]
        self.current_round +=1
        #Simulates empathy
        self.num_hits = random.randint(0,5)
        #Get num owned colors
        num_owned_colors = self.game.num_colors_player(self.current_player_name)
        #If deserved, offer available options
        if(self.game.gets_new_color(self.num_hits,num_owned_colors)):
            self.select_color()
            return
        self.get_shapes()

    def select_color(self):
        available_colors = self.game.player_neighbour_colors\
        (self.current_player_name.get())
        owned_colors = self.game.hex_colors_player(self.current_player_name.get())
        self.clear_center_frame()
        welcome_label = tk.Label(self.center_frame, text="You win a new color."\
            +"\n CONGRATULATIONS "+self.current_player_name.get()+" !!!")
        welcome_label.pack()
        info_label = tk.Label(self.center_frame, text=\
            "\nThese are the colors you own:")
        info_label.pack()
        for c in owned_colors:
            color_label = tk.Label(self.center_frame, width=50, background=c)
            color_label.pack()
        info2_label = tk.Label(self.center_frame, text="\nYou can choose one of these colors:")
        info2_label.pack()
        for c in available_colors:
            color_label = tk.Label(self.center_frame, width=50, text=str(c), background=self.game.color_map.colors[c].hex)
            color_label.pack()
        chosen_color = tk.StringVar()
        combo = ttk.Combobox(self.center_frame, values = available_colors)
        combo.bind('<<ComboboxSelected>>', self.color_chosen)
        combo.pack(padx = 5, pady = 5)
    
    def color_chosen(self,event=None):
        chosen_color = int(event.widget.get())
        self.game.player_add_color(self.current_player_name.get(), chosen_color)
        self.get_shapes()

    def get_shapes(self):
        self.clear_center_frame()
        self.current_shapes = self.game.get_rand_shape(self.num_hits,self.game.\
            num_colors_player(self.current_player_name.get()))
        self.paint()

    def paint(self):
        owned_colors = self.game.hex_colors_player(self.current_player_name.get())
        #paint
        #info = tk.Label(self.center_frame, text="Color chosen is:")
        #info.pack()
        #col_label = tk.Label(self.center_frame, width=50, background=color)
        #col_label.pack()
        #info2 = tk.Label(self.center_frame, text="Shape chosen is:"+str(shape))
        #info2.pack()
        self.right_canvas.bind("<Button 1>",self.paint_square)

    def paint_square(self, eventorigin):
        global x,y
        x = eventorigin.x
        y = eventorigin.y
        


if __name__ == "__main__":
    root = tk.Tk()
    beauty = BeautifulEmpathyApp(root)
    beauty.init_screen()
    beauty.create_game()
    root.mainloop()

