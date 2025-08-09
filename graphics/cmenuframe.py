# coding:utf-8
# the dynamic Menu in the Control Board
# modes : main_menu
#       : stocks    (create, remove, use)
#       : items     (create, remove)        => operates on main catalog

import customtkinter as ctk
from graphics.cmenubtn import CustomButton


class CustomMenuFrame(ctk.CTkFrame):
    def __init__(self, window,function=None, mode='default'):
        super().__init__(window)
        
        # variables
        self.mode = mode
        self.container = window
        self.logoff = function

        # widgets
        lbl_menu = ctk.CTkLabel(self, text='Main Menu', fg_color='transparent')     
        btn_mode_stock = CustomButton(self, 'Stocks', self.enter_mode_stock)
        btn_mode_item = CustomButton(self, 'Items', self.enter_mode_item)
        btn_stock_create = CustomButton(self, 'Create Stock', self.create_stock)
        btn_stock_remove = CustomButton(self, 'Remove Stock', self.remove_stock)
        btn_stock_select = CustomButton(self, 'Select Stock', self.select_stock)       
        btn_item_create = CustomButton(self, 'Create Item', self.create_item)
        btn_item_remove = CustomButton(self, 'Remove Item', self.remove_item)      
        btn_logoff = CustomButton(self, 'Log Off', self.logoff)
        # btn_back = CustomButton(self, 'Log Off', self.back)

        # conditionnal packing
        lbl_menu.pack()
        if self.mode == 'default':
            btn_mode_stock.pack(padx=20, pady=30)
            btn_mode_item.pack(padx=20, pady=30)
            btn_logoff.pack(padx=20, pady=30)
        elif self.mode == 'stock':
            btn_stock_select.pack(padx=20, pady=30)
            btn_stock_create.pack(padx=20, pady=30)
            btn_stock_remove.pack(padx=20, pady=30)
        elif self.mode == 'item':
            btn_item_create.pack(padx=20, pady=30)
            btn_item_remove.pack(padx=20, pady=30)
        # btn_back.pack(padx=20, pady=30)
    

    def enter_mode_stock(self):
        pass


    def enter_mode_item(self):
        pass


    def create_stock(self):
        pass

    
    def remove_stock(self):
        pass


    def select_stock(self):
        pass


    def create_item(self):
        pass


    def remove_item(self):
        pass


    def back(self):
        pass
