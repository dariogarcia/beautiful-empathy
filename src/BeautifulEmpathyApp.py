import random
import time
from textwrap import TextWrapper
import tkinter as tk
from tkinter import ttk, IntVar, StringVar, PhotoImage
import tkinter.font as tkFont
from BeautifulEmpathy import Game

MAX_PLAYERS=6
NUM_ROUNDS=6
NUM_QUESTIONS=5
NAME_LEN_LIM=3
WINDOW_WIDTH=1800
WINDOW_HEIGHT=900
SENTENCE_WIDTH=40

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
        self.b_only = None
        #dynamic vars
        self.current_player_name = None
        self.current_round = None
        self.current_turn = None
        self.num_hits = None
        self.current_shapes = None 
        self.chosen_color = None
        self.available_clicks = None
        self.done_clicks = StringVar()
        self.num_empathy = None
        self.current_question = None
        #game widgets
        self.combo_num_players = None

   ###################
   ##### WIDGETS ##### 
   ###################

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
        self.center_frame = tk.Frame(self.root, bg='white', width=400, height=1200)
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
        mosaic = PhotoImage(file = '../boards/color_sets.png')
        root.base_mosaic = mosaic
        self.right_canvas.create_image(0,0,image=mosaic,anchor = "nw")

    def update_tmp_right_frame_widgets(self):
        #This function loads the unconfirmed mosaic being edited
        img_mosaic = PhotoImage(file = self.game.mosaic.tmpboard_path)
        root.base_mosaic = img_mosaic
        self.right_canvas.create_image(0,0,image=img_mosaic,anchor = "nw")

    def update_right_frame_widgets(self):
        img_mosaic = PhotoImage(file = self.game.mosaic.board_path)
        root.base_mosaic = img_mosaic
        self.right_canvas.create_image(0,0,image=img_mosaic,anchor = "nw")
    
    def clear_center_frame(self):
       for widgets in self.center_frame.winfo_children():
          widgets.destroy()
 
   ###################
   ##### SCREENS ##### 
   ###################

    def init_screen(self):
        tk.Label(self.center_frame, font=("Arial", 22), text="Welcome,\n"\
             +"this is a game of feeling others\n"\
             +" and paiting together\n"\
             +"\n").pack()
        tk.Label(self.center_frame, text=""\
             +"\nOn your left is the Color Map\n"\
             +"it show the colors you own and could own\n"\
             +"\nOn your right there will be the Mosaic\n"\
             +"the canvas you will paint collaboratively\n"\
             +"\nBut first things first..."\
             +"\n").pack()
        self.update_top_frame_widgets()
        self.get_num_players()

    def get_num_players(self):
        title = tk.Label(self.center_frame, text="How many painters will"\
            " be playing today?")
        title.pack()
        plist = [i+1 for i in range(MAX_PLAYERS)]
        self.num_players = IntVar()
        self.combo_num_players = ttk.Combobox(self.center_frame,\
             values = plist)
        self.combo_num_players.bind('<<ComboboxSelected>>',\
             self.get_name_players)
        self.combo_num_players.pack(padx = 5, pady = 5)

    def create_game(self):
        self.game = Game(self.names_players,self.init_colors)

    def check_names(self, var, index, mode):
        #var, index and mode refer to the triggering event
        for idx, val in enumerate(self.names_players):
            #Limit to 3 chars
            string_name = self.names_players[idx].get()[:NAME_LEN_LIM]
            #Remove duplicates, from list of StringVar!
            for prev_name in self.names_players[:idx]:
                if string_name == prev_name.get():
                    string_name = ""
            self.names_players[idx].set(string_name)

    def get_name_players(self,event=None):
        self.num_players = int(self.combo_num_players.get())
        self.clear_center_frame()
        self.names_players = [None]*self.num_players
        tk.Label(self.center_frame, text="Enter painters names\n").pack()
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
        self.init_colors = self.game.assign_rand_init_colors(\
            self.num_players, self.names_players)
        tk.Label(self.center_frame, text="These are your initial colors").pack()
        for name,color in zip(self.names_players,self.init_colors):
            if len(name.get())<1:
                return
            tk.Label(self.center_frame, width=30, text=name.get(),\
                background=self.game.color_map.colors[color].hex).pack()
        self.update_left_frame_widgets()
        nx_btn = tk.Button(self.center_frame, text="Next",\
             command=self.game_type_screen)
        nx_btn.pack()
    
    def game_type_screen(self):
        self.clear_center_frame()
        tk.Label(self.center_frame, text="Which type of game you want to play?").pack()
        both_button = tk.Button(self.center_frame, text="Beauty & Empathy",\
             command=self.beauty_and_empathy)
        both_button.pack()
        only_button = tk.Button(self.center_frame, text="Beauty only",\
             command=self.beauty_only)
        only_button.pack()

    def beauty_and_empathy(self):
        self.b_only = False
        self.num_empathy = 0
        self.start_game()    
    
    def beauty_only(self):
        self.b_only = True
        self.start_game()    

    def start_game(self):
        self.current_round = 0
        self.update_right_frame_widgets()
        self.inter_round()
 
    def inter_round(self):
        if self.current_round >= NUM_ROUNDS:
            self.end_screen()
        else:
            self.current_round+=1
            self.current_turn = 0
            self.clear_center_frame()
            round_label = tk.Label(self.center_frame, text=\
                    "This is round number:"+str(self.current_round)+"/"\
                    +str(NUM_ROUNDS)).pack()
            tk.Label(self.center_frame, text="Ready?").pack()
            if self.current_round>1:
                tk.Label(self.center_frame, text=\
                    "btw I love your mosaic.\nFor realsies.").pack()
            only_button = tk.Button(self.center_frame, text="Start Round",\
                 command=self.inter_turn)
            only_button.pack()

    def inter_turn(self):
        #All players have painted
        if self.current_turn >= len(self.names_players):
            self.inter_round()
        #Players remain
        else:
            self.play_new_turn()

    def play_new_turn(self):
        self.current_player_name = self.names_players[self.current_turn]
        self.clear_center_frame()
        round_label = tk.Label(self.center_frame, text=\
                "This is round number:"+str(self.current_round)+"/"\
                +str(NUM_ROUNDS)+'\n').pack()
        turn_label = tk.Label(self.center_frame, text=\
             "It's the turn of player "+
             str(self.current_player_name.get()+"\n")).pack()
        if self.b_only == True:
            #Simulates empathy
            self.num_hits = random.randint(0,5)
            self.check_empathy_result()
        else:
            self.num_hits = 0
            self.play_empathy()

    def play_empathy(self):
        if self.num_empathy < NUM_QUESTIONS:
            self.play_empathy_turn()
        else:
            self.num_empathy = 0
            self.empathy_end()

    def play_empathy_turn(self):
        tk.Label(self.center_frame, text="Empathy phase", \
             font=('Helvetica 16 bold')).pack()
        self.num_empathy+=1
        self.current_question = self.game.get_rand_question()
        tk.Label(self.center_frame, text="The Painter this round is "+\
            self.current_player_name.get()).pack()
        tk.Label(self.center_frame, text="Decide who the guesser is\n"\
            +"(random, alphabet, clockwise, ...)\n"\
            +"Press the button to start the round\n").pack()
        tk.Button(self.center_frame, text="SHOW QUESTION "+str(self.num_empathy)\
            +"/"+str(NUM_QUESTIONS), command=self.show_question).pack()

    def show_question(self):
        self.clear_center_frame()
        self.current_question = self.game.get_rand_question()
        clear_q = self.current_question.q.replace("[MASK]","[ ? ]")
        tw = TextWrapper()
        tw.width = SENTENCE_WIDTH
        splitted_q = "\n".join(tw.wrap(clear_q))
        tk.Label(self.center_frame, text=splitted_q+'\n',\
             font=('Helvetica 16 italic')).pack()
        tk.Label(self.center_frame, text=self.current_player_name.get()\
            +", read the sentence outloud,\n"\
            +"then click below to see the options,\n"\
            +"and instinctively and quickly decide\n"\
            +"which option feels more natural").pack()
        tk.Button(self.center_frame, text="SEE OPTIONS",\
             command=self.show_options).pack()
    
    def show_options(self):
        self.clear_center_frame()
        clear_q = self.current_question.q.replace("[MASK]","[ ? ]")
        tw = TextWrapper()
        tw.width = SENTENCE_WIDTH
        splitted_q = "\n".join(tw.wrap(clear_q))
        tk.Label(self.center_frame, text=splitted_q,\
             font=('Helvetica 16 italic')).pack()
        tk.Label(self.center_frame, text=self.current_question.v1+\
             "<--?-->"+self.current_question.v2,\
              font=("Helvetica", 21)).pack()
        root.update()
        self.show_options_after_5_sec()

    def show_options_after_5_sec(self):
        time.sleep(3)
        tk.Label(self.center_frame, text="\n").pack()
        tk.Label(self.center_frame, text="Once the painter has decided,\n"\
            +"The guesser can guess.\n").pack()
        tk.Label(self.center_frame, text="\nWas the guess correct?").pack()
        tk.Button(self.center_frame, text="Yes",\
             command=self.question_hit).pack()
        tk.Button(self.center_frame, text="No",\
             command=self.question_miss).pack()
        
    def question_hit(self):
        self.num_hits+=1
        self.current_question = None
        self.clear_center_frame()
        self.play_empathy()

    def question_miss(self):
        self.current_question = None
        self.clear_center_frame()
        self.play_empathy()

    def empathy_end(self):
        self.clear_center_frame()
        #print results
        tk.Label(self.center_frame, text=\
            "You guessed correctly "+str(self.num_hits)+" out of "\
            +str(NUM_QUESTIONS)+" questions").pack()
        tk.Label(self.center_frame, text=\
            "Click the button for the Beauty phase\n").pack()
        tk.Button(self.center_frame, text="Let's paint!",\
             command=self.check_empathy_result).pack()

    def check_empathy_result(self):
        self.clear_center_frame()
        #Get num owned colors
        num_owned_colors = self.game.num_colors_player(self.current_player_name)
        #If deserved, offer available options
        if(self.game.gets_new_color(self.num_hits,num_owned_colors)):
            self.select_color()
        else:
            self.get_shapes()

    def select_color(self):
        available_colors = self.game.player_neighbour_colors\
        (player_name = self.current_player_name.get(), skip_unused = True)
        owned_colors = self.game.hex_colors_player(self.current_player_name.get())
        tk.Label(self.center_frame, text="Because of empathy, "+\
            self.current_player_name.get()+"\nyou get a new color :)\n").pack()
        tk.Label(self.center_frame, text=\
            "\nThese are the colors you own:").pack()
        for c in owned_colors:
            color_label = tk.Label(self.center_frame, width=50, background=c)
            color_label.pack()
        tk.Label(self.center_frame, text="\n\nChoose one of these colors\n"
            +"and add them to your palette").pack()
        for c in available_colors:
            color_label = tk.Label(self.center_frame, width=50, text=str(c), background=self.game.color_map.colors[c].hex)
            color_label.pack()
        combo = ttk.Combobox(self.center_frame, values = available_colors)
        combo.bind('<<ComboboxSelected>>', self.color_chosen)
        combo.pack(padx = 5, pady = 5)
    
    def color_chosen(self,event=None):
        chosen_color = int(event.widget.get())
        self.game.player_add_color(self.current_player_name.get(), chosen_color)
        self.update_left_frame_widgets()
        self.get_shapes()

    def get_shapes(self):
        self.clear_center_frame()
        self.current_shapes = self.game.get_rand_shape(self.num_hits,self.game.\
            num_colors_player(self.current_player_name.get()))
        self.paint()

    def paint(self):
        self.painter_colors = self.game.colors_player(self.current_player_name.get())
        self.current_color = random.choice(list(self.painter_colors.values())).hex
        #Add radio button and link with click on right canvas
        tk.Label(self.center_frame, text=\
            "Which color you want to use?").pack()
        color_indices = []
        for idx,c in self.painter_colors.items():
            color_label = tk.Label(self.center_frame,text=str(idx), width=50, background=c.hex)
            color_label.pack()
            color_indices.append(idx)
        #Clear combo selection
        self.chosen_color == None
        combo = ttk.Combobox(self.center_frame, values = color_indices)
        combo.bind('<<ComboboxSelected>>', self.color_paint_chosen)
        combo.pack()
        self.right_canvas.bind("<Button 1>", self.paint_square)
        #Add label with shape info
        tk.Label(self.center_frame, text=\
            "\nYou can paint:\n").pack()
        self.available_clicks = 0
        self.done_clicks.set("0")
        for shape,num in self.current_shapes.items():
            if shape == 'c':
                tk.Label(self.center_frame, text=str(num)+\
                    " small squares").pack()
                self.available_clicks+=num
            elif shape == 'C':
                tk.Label(self.center_frame, text=str(num)+\
                    " large squares").pack()
                self.available_clicks+=num*4
        info_label = tk.Label(self.center_frame, text=\
            "\nHit RESET to start over\n"\
            +"Hit CONFIRM to continue.\n")
        info_label.pack()
        #Add two buttons. confirm and reset
        reset_button = tk.Button(self.center_frame, text="RESET",\
             command=self.reset_mosaic)
        reset_button.pack()
        tk.Label(self.center_frame, text="").pack()
        accept_button = tk.Button(self.center_frame, text="CONFIRM",\
             command=self.confirm_mosaic)
        accept_button.pack()
        tk.Label(self.center_frame, text="Painted squares:").pack()
        tk.Label(self.center_frame, textvariable=self.done_clicks).pack()

    def color_paint_chosen(self,event=None):
        self.chosen_color = int(event.widget.get())

    def paint_square(self, event):
        #if the combo aint selected yet
        if self.chosen_color == None:
            return
        if self.available_clicks <= int(self.done_clicks.get()):
            return
        self.done_clicks.set(str(int(self.done_clicks.get())+1))
        x = event.x
        y = event.y
        self.game.mosaic.paint_square(x,y,self.painter_colors[self.chosen_color].hex)
        self.update_tmp_right_frame_widgets()

    def reset_mosaic(self,event=None):
        self.game.mosaic.scrap_tmp()
        self.clear_center_frame()
        self.update_right_frame_widgets()
        self.paint()

    def confirm_mosaic(self,event=None):
        self.current_turn += 1
        self.current_shapes = None
        self.chosen_color = None
        self.game.mosaic.persist_tmp()
        self.inter_turn()

    def end_screen(self):
        self.clear_center_frame()
        info_label = tk.Label(self.center_frame, text="Your mosaic is done"\
            +"\nThis is the result of your empathy and artistry\n"\
            +"file stored in: "+self.game.mosaic.board_path)
        info_label.pack()
        
def set_default_font():
    default_font = tkFont.nametofont("TkDefaultFont")
    default_font.configure(size=13)

if __name__ == "__main__":
    root = tk.Tk()
    set_default_font()
    beauty = BeautifulEmpathyApp(root)
    beauty.init_screen()
    beauty.create_game()
    root.mainloop()

