# coding:utf-8


from utils.dbfunc import check_is_admin


class User:
    def __init__(self, username):
        self.username = username
        self.is_admin = check_is_admin(self.username)
        self.print_state("connected")


    def print_state(self, state):
        precise_admin = ""
        if self.is_admin:
            precise_admin = "(admin)"
        print(f"{self.username} {precise_admin} - {state}")

# A IMPLEMENTER
# écrire les données de connexion dans un fichier log
# format :      (<time>) <user> - dis/connected ?(admin mode)
# fichier log dans répertoire data 