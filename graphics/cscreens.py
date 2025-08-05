# coding:utf-8
# custom Screens
# a base to design the app's screens
# except the main screen (CTk())

import customtkinter as ctk
from utils.const import *

class CustomScreen(ctk.CTkToplevel):
    def __init__(self, window_title):
        super().__init__()
        self.geometry(LOG_SIZE)
        self.title(window_title)
        self.configure(fg_color=TITLE_GRAY)


    # function kills the window and the main menu comes back
    def back_to_menu(self):
        self.master.deiconify()
        print(self.master.state)
        self.destroy()
        