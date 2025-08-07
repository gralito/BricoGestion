# coding:utf-8
# custom Screens
# a base to design the app's screens
# except the main screen (CTk())

import customtkinter as ctk
from utils.const import *

class CustomScreen(ctk.CTkToplevel):
    def __init__(self, window_title):
        super().__init__()
        self.geometry(APP_SIZE)
        self.title(window_title)
        self.configure(fg_color=TITLE_GRAY)
        
        # frames
        self.title_frame = ctk.CTkFrame(self, fg_color=TITLE_GRAY)
        self.content_frame = ctk.CTkFrame(self, fg_color=TITLE_GRAY) 

        # widgets     
        lbl_title = ctk.CTkLabel(self.title_frame, text=window_title,
                font=('Tahoma', 24), corner_radius=5, 
                height=75, width=250,
                fg_color=BROWN_BG)
        lbl_title.grid(row=0, column=0, columnspan=2, pady=20, sticky='ew')

        # packing
        self.title_frame.pack()
        self.content_frame.pack()


    # function kills the window and the main menu comes back
    def back_to_menu(self):
        self.master.deiconify()
        self.destroy()
        