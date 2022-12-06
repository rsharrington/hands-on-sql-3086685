import sqlite3

def connect():

    con1 = sqlite3.connect("C:/Tools/hands-on-sql/test2.db")

    cur1 = con1.cursor()

    cur1.execute(
        "CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")

    con1.commit()

    con1.close()
