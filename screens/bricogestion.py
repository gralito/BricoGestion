# coding:utf-8
# main screen of the application

# imports
import customtkinter as ctk
from graphics.cmenubtn import CustomButton

from utils.const import *
import screens.loginscreen as lgs
import screens.createscreen as crs
from screens.controlboard import ControlBoard


# main class, representing the application
# will have three subclasses : DefaultScreen, LoggedScreen and AdminMode
class BricoGestion(ctk.CTk):
    
    # class variable    :   indicates the state of the connexion
    #                       "off" -- no user logged
    #                       "logged" -- a regular user is logged
    #                       "admin" -- an admin user is logged
    

    def __init__(self):
        ctk.set_appearance_mode("dark")
        super().__init__()
        self.title("BricoGestion v1.0")
        self.geometry(APP_SIZE)
        self.configure(background=BROWN_BG)

        # variables
        self.state = "off"
        self.current_user = None
        self.login_screen = None

        # widgets
        lbl_title = ctk.CTkLabel(self, text='BricoGestion',
                font=('Tahoma', 24), corner_radius=5, 
                height=75, width=250,
                fg_color=BROWN_BG)
        lbl_title.pack(pady=50, expand=ctk.YES)

        btn_enter = CustomButton(self, 'Login', self.login)
        btn_quit = CustomButton(self, 'Quit', self.quit)
        btn_create = CustomButton(self, 'Register', self.register)
        
        # packing
        btn_enter.pack(pady=10)
        btn_create.pack(pady=10)
        btn_quit.pack(pady=10)

        if self.state == "logged":
            self.launch_cboard()
    
    # callback of the login button
    def login(self):
        self.withdraw()
        self.login_screen = lgs.LoginScreen(self.launch_cboard)


    # callback of the register button
    def register(self):
        self.withdraw()
        register_screen = crs.CreateScreen()


    # the control board
    def launch_cboard(self, user):
        self.login_screen.destroy()
        self.withdraw()
        self.control_board = ControlBoard(user)


    

