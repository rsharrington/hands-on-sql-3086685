import sqlite3

def connect():

    try:
        con1 = sqlite3.connect("C:/Tools/hands-on-sql/test.db")

    #cur1 = con1.cursor()

    #cur1.execute(
    #    "CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
        print("\nConnection to SQLite successful!\n")
    except sqlite3.Error as err:
        print(f"Error: '{err}'")

    con1.commit()

    con1.close()
