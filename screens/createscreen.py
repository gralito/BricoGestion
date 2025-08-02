# coding:utf-8
# classe CreateScreen
# to create a new user
# can be used logged in or not
# the default created user is not admin


# imports
import tkinter as tk
import customtkinter as ctk
from graphics.cmenubtn import CustomButton
from utils.const import *


class CreateScreen(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry(LOG_SIZE)
        self.title('Register')
        self.configure(fg_color=TITLE_GRAY)

        # variables
        var_ent_usr = tk.StringVar()
        var_ent_pwd = tk.StringVar()
        var_ent_cpwd = tk.StringVar()
        
        # frames
        ent_frame = ctk.CTkFrame(self, fg_color=BROWN_BG)
        btn_frame = ctk.CTkFrame(self, fg_color=TITLE_GRAY)

        # widgets 
        lbl_usr = ctk.CTkLabel(ent_frame, text='username >')
        lbl_pwd = ctk.CTkLabel(ent_frame, text='password >')
        lbl_cpwd = ctk.CTkLabel(ent_frame, text=' confirm >')
        ent_usr = ctk.CTkEntry(ent_frame, textvariable=var_ent_usr)
        ent_pwd = ctk.CTkEntry(ent_frame, textvariable=var_ent_pwd)
        ent_cpwd = ctk.CTkEntry(ent_frame, textvariable=var_ent_cpwd)       
        btn_val = CustomButton(btn_frame, 'Validate', self.validate)
        btn_back = CustomButton(btn_frame, 'Back', self.back_to_menu)

        # packing
        lbl_usr.grid(row=0, column=0, padx=10, pady=10)
        lbl_pwd.grid(row=1, column=0, padx=10, pady=10)
        lbl_cpwd.grid(row=2, column=0, padx=10, pady=10)
        ent_usr.grid(row=0, column=1, padx=10, pady=10)
        ent_pwd.grid(row=1, column=1, padx=10, pady=10)
        ent_cpwd.grid(row=2, column=1, padx=10, pady=10)
        btn_back.grid(row=0, column=0, padx=10)
        btn_val.grid(row=0, column=1, padx=10)
        ent_frame.pack(anchor='s', pady=20)
        btn_frame.pack(anchor='s', pady=20)

    # the validate button
    def validate(self):
        pass


    # back to menu button
    def back_to_menu(self):
        self.master.deiconify()
        self.destroy()
        print(self.master.state)