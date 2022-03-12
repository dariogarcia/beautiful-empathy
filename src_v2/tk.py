import tkinter as tk
from tkinter import ttk, StringVar, PhotoImage
import random
from BeautifulEmpathy import Game

class BeautifulEmpathyApp():

    def __init__(self, root):
        #set tk objects
        self.root = root
        self.root.title('Beautiful Empathy')
        self.left_frame = None
        self.left_canvas = None
        self.right_frame = None
        self.right_canvas = None
        self.center_frame = None
        #set tk config
        self.configure_main_window()
        self.create_containers()
        self.left_frame_widgets()
        self.right_frame_widgets()
        #game vars
        self.game = None
        self.current_window = 0
        self.num_players = None
        self.names_players = []
        self.init_colors = []
        self.current_player_name = None

    def configure_main_window(self):
        window_width = 1800
        window_height = 900
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
                
    def create_containers(self):
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.left_frame = tk.Frame(self.root, bg='black', width=500, height=500)
        self.center_frame = tk.Frame(self.root, bg='white', width=200, height=800)
        self.right_frame = tk.Frame(self.root, bg='black', width=900, height=900)
        self.left_frame.grid(row=0, column=0)
        self.center_frame.grid(row=0, column=1)
        self.right_frame.grid(row=0, column=2)

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

    def show_next_screen(self,event=None):
        #Transition from get num players to get names
        if  self.current_window == 0:
            self.current_window+=1
            self.num_players = int(event.widget.get())
            self.names_players = [None]*self.num_players
            self.clear_center_frame()
            self.get_name_players()
            return
        #Transition from get names to choose initial colors
        if  self.current_window == 1:
            for name in self.names_players:
                if len(name.get())<1:
                    print(name.get())
                    return
            self.current_window+=1
            self.clear_center_frame()
            self.choose_init_colors()
            self.show_colors_players()
            return
 
    def limit_name_len(self, var, index, mode):
        len_limit = 3
        for idx, val in enumerate(self.names_players):
            string_name = self.names_players[idx].get()[:len_limit]
            self.names_players[idx].set(string_name)

    def choose_init_colors(self):
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

    def get_num_players(self):
        title = tk.Label(self.center_frame, text="Enter number of painters")
        title.pack()
        plist = [i+1 for i in range(6)]
        str_num = tk.StringVar()
        combo = ttk.Combobox(self.center_frame, values = plist)
        combo.bind('<<ComboboxSelected>>', self.show_next_screen)
        combo.pack(padx = 5, pady = 5)

    def get_name_players(self):
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
            self.names_players[i].trace('w', self.limit_name_len)
        submit_button = tk.Button(self.center_frame, text="Next",\
             command=self.show_next_screen)
        submit_button.pack()

    def show_colors_players(self):
        for name,color in zip(self.names_players,self.init_colors):
            name_label = tk.Label(self.center_frame, text="Player "+name.get()+", this is your color")
            name_label.pack()
            tk.Label(self.center_frame, width = 20, background=self.game.color_map.colors[color].hex).pack()
        self.update_left_frame_widgets()
        self.game_type_screen()

    def color_chosen(self,event=None):
        chosen_color = int(event.widget.get())
        self.game.player_add_color(self.current_player_name)

    def select_color(self, name, owned_colors, available_colors):
        self.clear_center_frame()
        welcome_label = tk.Label(self.center_frame, text="You win a new color.\n CONGRATULATIONS "+name+" !!!")
        welcome_label.pack()
        info_label = tk.Label(self.center_frame, text="\nThese are the colors you own:")
        info_label.pack()
        for c in owned_colors:
            color_label = tk.Label(self.center_frame, width=50, background=c)
            color_label.pack()
        info2_label = tk.Label(self.center_frame, text="\nYou can choose one of these colors:")
        info2_label.pack()
        for idx, c in enumerate(available_colors):
            color_label = tk.Label(self.center_frame, width=50, text=str(idx), background=self.game.color_map.colors[c].hex)
            color_label.pack()
        plist = [i for i in range(len(available_colors))]        
        chosen_color = tk.StringVar()
        combo = ttk.Combobox(self.center_frame, values = plist)
        combo.bind('<<ComboboxSelected>>', self.color_chosen)
        combo.pack(padx = 5, pady = 5)


    def game_type_screen(self):
        info_label = tk.Label(self.center_frame, text="Which type of game you want to play?")
        info_label.pack()
        both_button = tk.Button(self.center_frame, text="Beauty & Empathy",\
             command=self.beauty_only)
        both_button.pack()
        only_button = tk.Button(self.center_frame, text="Beauty only",\
             command=self.beauty_only)
        only_button.pack()

    def beauty_only(self):
        if self.game.played_rounds < 5:
            for player in self.names_players:
                self.current_player_name = player.get()
                #Simulates empathy
                num_hits = random.randint(0,5)
                #Gets owned colors
                num_owned_colors = self.game.num_colors_player(player.get())
                #If deserved, offer available options
                if(self.game.gets_new_color(num_hits,num_owned_colors)):
                    available_colors = self.game.player_neighbour_colors(player.get())
                    owned_colors = self.game.hex_colors_player(player.get())
                    self.select_color(player.get(),owned_colors, available_colors)
                #Get shapes
                call_window_for_selecting_shape(player.get())
            self.game.player_rounds+=1 

if __name__ == "__main__":
    root = tk.Tk()
    beauty = BeautifulEmpathyApp(root)
    beauty.get_num_players()
    beauty.create_game()
    root.mainloop()

