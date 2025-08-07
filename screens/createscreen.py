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
from utils.msgbox import warning_infos
from utils.dbfunc import create_user, check_user_availability, create_stock_list
from graphics.cscreens import CustomScreen

class CreateScreen(CustomScreen):
    def __init__(self):
        super().__init__('Registration')

        # variables
        self.var_ent_usr = tk.StringVar()
        self.var_ent_pwd = tk.StringVar()
        self.var_ent_cpwd = tk.StringVar()
        
        # frames
        ent_frame = ctk.CTkFrame(self.content_frame, fg_color=BROWN_BG)
        btn_frame = ctk.CTkFrame(self.content_frame, fg_color=TITLE_GRAY)

        # widgets 
        lbl_usr = ctk.CTkLabel(ent_frame, text='Username >')
        lbl_pwd = ctk.CTkLabel(ent_frame, text='Password >')
        lbl_cpwd = ctk.CTkLabel(ent_frame, text='Confirm >')
        ent_usr = ctk.CTkEntry(ent_frame, textvariable=self.var_ent_usr)
        ent_pwd = ctk.CTkEntry(ent_frame, textvariable=self.var_ent_pwd, show='*')
        ent_cpwd = ctk.CTkEntry(ent_frame, textvariable=self.var_ent_cpwd, show='*')       
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
        ent_frame.pack(anchor='n', pady=20)
        btn_frame.pack(anchor='n', pady=20)


    # the validate button
    def validate(self):
        usr = self.get_usr()
        pwd = self.get_pwd()
        cpwd = self.get_cpwd()

        if usr == "" or pwd == "" or cpwd == "":
            warning_infos(self, "Informations missing !")
        elif check_user_availability(usr):
            create_user(usr, pwd, 0)
            create_stock_list(usr)
            self.back_to_menu()
        else:
            message = f"le pseudo {usr} est déjà utilisé"
            warning_infos(self, message)

    
    # functions to get the entered username
    def get_usr(self, *args):
        user = self.var_ent_usr.get()
        return user


    # functions to get the entered password
    def get_pwd(self, *args):
        password = self.var_ent_pwd.get()
        return password


    # functions to get the confirmed password
    def get_cpwd(self, *args):
        cpassword = self.var_ent_cpwd.get()
        return cpassword