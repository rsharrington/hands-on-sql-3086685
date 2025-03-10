from tkinter import ttk

import tkinter as tk

import sqlite3

# Separate connection function into its own file
def connect():

    con1 = sqlite3.connect("C:/Tools/hands-on-sql/test3.db")

    cur1 = con1.cursor()

    cur1.execute(
        "CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT)")

    con1.commit()

    con1.close()

# Separate view function into its own file
def View():

    con1 = sqlite3.connect("C:/Tools/hands-on-sql/test3.db")

    cur1 = con1.cursor()

    cur1.execute("SELECT * FROM customers")   # get info from table

    rows = cur1.fetchall()

    for row in rows:

        print(row)

        tree.insert("", tk.END, values=row)

    con1.close()


# connect to the database
connect()

root = tk.Tk()

tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="ID")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="FirstName")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="LastName")

tree.pack()

button1 = tk.Button(text="Display Data", command=View)

button1.pack(pady=10)

root.mainloop()