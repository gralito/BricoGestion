# coding:utf-8
# main screen of the application

# imports
import customtkinter as ctk
from graphics.cmenubtn import CustomButton

from utils.const import *
import screens.loginscreen as lgs
import screens.createscreen as crs


# main class, representing the application
# will have three subclasses : DefaultScreen, LoggedScreen and AdminMode
class BricoGestion(ctk.CTk):
    
    # class variable    :   indicates the state of the connexion
    #                       "off" -- no user logged
    #                       "logged" -- a regular user is logged
    #                       "admin" -- an admin user is logged
    state = "off"

    def __init__(self):
        ctk.set_appearance_mode("dark")
        super().__init__()
        self.title("BricoGestion v1.0")
        self.geometry(APP_SIZE)
        self.configure(background=BROWN_BG)

        # widgets
        lbl_title = ctk.CTkLabel(self, text='BricoGestion',
                font=('Tahoma', 24), corner_radius=5, 
                height=75, width=250,
                fg_color=BROWN_BG)
        lbl_title.pack(pady=50, expand=ctk.YES)

        btn_enter = CustomButton(self, 'Login', self.login)
        btn_quit = CustomButton(self, 'Quit', self.quit)
        btn_create = CustomButton(self, 'Register', self.register)
        
        # placement
        btn_enter.pack(pady=10)
        btn_create.pack(pady=10)
        btn_quit.pack(pady=10)

    
    # callback of the login button
    def login(self):
        self.withdraw()
        login_screen = lgs.LoginScreen()

    # callback of the register button
    def register(self):
        self.withdraw()
        register_screen = crs.CreateScreen()



    

