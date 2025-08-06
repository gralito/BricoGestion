# coding:utf-8

from graphics.cscreens import CustomScreen
from graphics.cmenubtn import CustomButton
import tkinter as tk
import customtkinter as ctk
from utils.user import User

class ControlBoard(CustomScreen):
    def __init__(self, username):
        super().__init__(f'Control Board - {username}')
        self.grid_columnconfigure(1, weight=3)
        self.current_user = User(username)
        
        # variables
        self.username = username

        # frames
        self.button_frame = ctk.CTkFrame(self, height=600)
        self.display_frame = ctk.CTkScrollableFrame(self)

        # widgets
        self.lbl_menu = ctk.CTkLabel(self.button_frame, text='BOARD',
                                fg_color='transparent')
        self.btn_show_item = CustomButton(self.button_frame, text='Open Stock',
                                command=self.open_stock)
        self.btn_add_item = CustomButton(self.button_frame, text='Create Stock',
                                command=self.create_stock)
        self.btn_remove_item = CustomButton(self.button_frame, text='Remove Stock',
                                command=self.remove_stock)
        self.btn_logoff = CustomButton(self.button_frame, text='Log Off',
                                command=self.logoff)
        
        # packing
        self.lbl_menu.pack(padx=10, pady=10)
        self.btn_show_item.pack(padx=10, pady=10)
        self.btn_add_item.pack(padx=10, pady=10)
        self.btn_remove_item.pack(padx=10, pady=10)
        self.btn_logoff.pack(padx=10, pady=10)

        self.button_frame.grid(row=0, column=0, sticky='nsw')
        self.display_frame.grid(row=0, column=1, sticky='nsew')


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



