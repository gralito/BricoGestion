# coding:utf-8
# custom menu button
# a base to design the app's menus buttons

import customtkinter as ctk

class CustomButton(ctk.CTkButton):
    def __init__(self, master, text, command):
        super().__init__(master, text=text, command=command)
        self.configure(width=100, height=30,
                    fg_color='#79470F', hover_color='#33363C')
        