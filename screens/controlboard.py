# coding:utf-8

from graphics.cscreens import CustomScreen
from graphics.cmenubtn import CustomButton
import tkinter as tk
import customtkinter as ctk
from utils.user import User
from graphics.cmenuframe import CustomMenuFrame

class ControlBoard(CustomScreen):
    def __init__(self, username):
        super().__init__(f'Control Board - {username}')
        self.current_user = User(username)

        # frames
        self.button_frame = CustomMenuFrame(self, self.logoff)
        self.display_frame = ctk.CTkScrollableFrame(self, width=400)

        # packing
        self.button_frame.pack(side='left')
        self.display_frame.pack(side='left', expand=True)


    # FONCTIONS
    def open_stock(self):
        pass


    def create_stock(self):
        pass


    def remove_stock(self):
        pass


    def logoff(self):
        self.master.state = "logoff"
        self.current_user.print_state("disconnected")
        self.master.deiconify()
        self.destroy()



