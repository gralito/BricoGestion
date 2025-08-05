# coding:utf-8

from graphics.cscreens import CustomScreen
from graphics.cmenubtn import CustomButton
import tkinter as tk
import customtkinter as ctk

class ControlBoard(CustomScreen):
    def __init__(self, username):
        super().__init__(f'Control Board - {username}')
        self.grid_columnconfigure(1, weight=3)
        
        # variables
        self.username = username

        # frames
        self.button_frame = ctk.CTkFrame(self)
        self.display_frame = ctk.CTkScrollableFrame(self)

        # widgets
        self.lbl_menu = ctk.CTkLabel(self.button_frame, text='BOARD',
                                fg_color='transparent')
        self.btn_show_item = CustomButton(self.button_frame, text='Show Item',
                                command=self.show_item)
        self.btn_add_item = CustomButton(self.button_frame, text='Add Item',
                                command=self.add_item)
        self.btn_remove_item = CustomButton(self.button_frame, text='Remove Item',
                                command=self.remove_item)
        self.btn_logoff = CustomButton(self.button_frame, text='LogOff',
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
    def show_item(self):
        pass


    def add_item(self):
        pass


    def remove_item(self):
        pass


    def logoff(self):
        self.master.state = "logoff"
        print(f"{self.username} déconnecté")
        self.master.deiconify()
        self.destroy()



