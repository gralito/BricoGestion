# coding:utf-8

from graphics.cscreens import CustomScreen

class ControlBoard(CustomScreen):
    def __init__(self, username):
        super().__init__(f'Control Board - {username}')
        self.username = username
        


