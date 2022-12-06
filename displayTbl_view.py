from tkinter import ttk

import sqlite3



def View():

    con1 = sqlite3.connect("C:/Tools/hands-on-sql/test2.db")

    cur1 = con1.cursor()

    cur1.execute("SELECT * FROM customers")

    rows = cur1.fetchall()

    for row in rows:

        print(row)

        tree.insert("", tk.END, values=row)

    con1.close()

    tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')


tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="ID")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="FNAME")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="LNAME")

tree.pack()

button1 = tk.Button(text="Display data", command=View)

button1.pack(pady=10)