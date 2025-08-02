# coding:utf-8


import customtkinter as ctk
from graphics.cmenubtn import CustomButton
from utils.const import *

# informations missing
def warning_infos(window):
    popup_window = ctk.CTkToplevel(window)
    popup_window.configure(fg_color=BACKGROUND)
    
    popup_lbl = ctk.CTkLabel(popup_window,
                    text="Informations missing !")
    popup_btn = CustomButton(popup_window, "Ok", popup_window.destroy)

    popup_lbl.pack(padx=20, pady=20)
    popup_btn.pack(padx=20, pady=20)