# coding:utf-8

########################
#     BricoGestion     #
########################

"""
a simple App to handle your home sotcks
dev           : J.ROUSSEL
v1.0          : initial version
"""

# imports
from screens.bricogestion import BricoGestion
import os
import utils.dbfunc as dbfunc

# main program
if __name__ == "__main__":
    # checking if the database already exists
    if not os.path.isfile("data/app_data.db"):
        dbfunc.firstTimeDB()
    app = BricoGestion()
    app.mainloop()