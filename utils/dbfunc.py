# coding:utf-8
# some tools to work with databases in the App
# using SQLite3 package


# imports
import sqlite3


# a tool to send an Sqlite3 request
def runQuery(sql, data=None, receive=False):
    try:
        connection = sqlite3.connect("data/app_data.db")
        cursor = connection.cursor()
        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)
        if receive:
            result = cursor.fetchall()
            connection.close()
            return result
        else:
            connection.commit()
    except Exception as e:
        print(e)
        connection.rollback
    finally:
        connection.close()


# a first time method to create the database
# and the users table
def firstTimeDB():
        # creates the users table
        # toDo : db encryption
        create_table_users = """CREATE TABLE users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    usr_username TEXT NOT NULL UNIQUE,
                    usr_password TEXT,
                    usr_is_admin INTEGER DEFAULT 0)"""
        runQuery(create_table_users)

        # create the main catalog, containing every possible items
        create_main_catalog = """CREATE TABLE main_catalog(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    item_name TEXT NOT NULL UNIQUE,
                    item_category TEXT NOT NULL)"""
        runQuery(create_main_catalog)

        # creates the administrator (me)
        # will be removed in a later version
        # create_user("julien", "ju", 1)
        # create_stock_list("julien")



def create_user(username, password, is_admin=0):
    query = """INSERT INTO users
                (usr_username, usr_password, usr_is_admin)
                VALUES (?, ?, ?)"""
    data = (username, password, is_admin)
    runQuery(query, data)


def create_stock_list(user):
    list_name = f"{user}_stocklist"
    query = f"""CREATE TABLE {list_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                stock_name TEXT UNIQUE NOT NULL
                )"""
    runQuery(query)
        

def create_stock(stock_name):
    query = f"""CREATE TABLE {stock_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name TEXT UNIQUE NOT NULL,
                    qty INTEGER DEFAULT 0,
                    cat TEXT,
                    qty_min INTEGER,
                    low_stock INTEGER DEFAULT 0
                    )"""
    runQuery(query)



def get_login_info(username):
    data = (username,)
    query = """SELECT usr_username, usr_password FROM users
            WHERE usr_username = ?"""
    result = runQuery(query, data, True)
    return(result)


def check_user_availability(username):
    query = """SELECT usr_username FROM users WHERE usr_username = ?"""
    data = (username,)
    result = runQuery(query, data, True)
    if result == []:
        return True
    else:
        return False


def check_is_admin(username):
    query = """SELECT usr_is_admin FROM users WHERE usr_username = ?"""
    data = (username, )
    result = runQuery(query, data, True)
    print(result)
    if result == [(1,)]:
        return True
    else:
        return False

#-----------------A IMPLEMENTER------------------
# a function to remove a user (admin required)

# a function to add an item to a stock

# a function to remove an item from the stock

#-----------------TEST------------------
if __name__ == "__main__":
    pass