# coding:utf-8
# LoginScreen

# imports
import tkinter as tk
import customtkinter as ctk
from graphics.cmenubtn import CustomButton
from utils.const import *
from utils.dbfunc import get_login_info
from graphics.cscreens import CustomScreen

class LoginScreen(CustomScreen):
    def __init__(self):
        super().__init__('Login')

        # variables
        self.var_usr = tk.StringVar()
        self.var_pss = tk.StringVar()
        self.admin_check = tk.BooleanVar()

        # frames
        login_frame = ctk.CTkFrame(self, fg_color=BROWN_BG)
        button_frame = ctk.CTkFrame(self, fg_color=TITLE_GRAY)
        
        # widgets
        lbl_usr = ctk.CTkLabel(login_frame, text='Username   >')
        lbl_pss = ctk.CTkLabel(login_frame, text='Password   >')
        ent_usr = ctk.CTkEntry(login_frame, textvariable=self.var_usr)
        ent_pss = ctk.CTkEntry(login_frame, textvariable=self.var_pss, show='*')
        cbox_admin = ctk.CTkCheckBox(login_frame, text='Admin mode (-not yet available-)',
                                    variable=self.admin_check)
        btn_back = CustomButton(button_frame, 'Back', self.back_to_menu)
        btn_login = CustomButton(button_frame, 'Login', self.login)

        # packing
        lbl_usr.grid(row=0, column=0, padx=10, pady=10)
        lbl_pss.grid(row=1, column=0, padx=10, pady=10)
        ent_usr.grid(row=0, column=1, padx=10, pady=10)
        ent_pss.grid(row=1, column=1, padx=10, pady=10)
        cbox_admin.grid(row=2, column=0, columnspan=2, pady=10)
        btn_login.grid(row=0, column=0, padx=10)
        btn_back.grid(row=0, column=1, padx=10)
        login_frame.pack(anchor='s', pady=20)
        button_frame.pack(anchor='s', pady=20)      


    # functions to get the entered username
    def get_usr(self, *args):
        user = self.var_usr.get()
        return user
    
    # functions to get the entered password
    def get_pss(self, *args):
        password = self.var_pss.get()
        return password

    # login function tests the login & password adequation
    def login(self):
        tested_username = self.get_usr()
        tested_password = self.get_pss()

        user = get_login_info(tested_username)
        if user == [(tested_username, tested_password)]:
            print("vous etes connecté")
            self.master.state = "logged"
            self.back_to_menu()
