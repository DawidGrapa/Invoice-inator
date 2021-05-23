from tkinter import *
from tkinter.font import Font
from tkinter import font, messagebox
from Company.editCompany import EditCompany
from Database.db import Database
import tkinter as tk
from tkinter.font import Font

db = Database('Database/Database.db')


class CompanyWindow:
    def __init__(self, app):
        self.app = app
        self.window = Toplevel(app)
        self.company = db.get_company()
        self.fontStyle = font.Font(family="Dotum", size=15)
        self.help = ["Company name: ", "Street: ", "Zip-code: ", "City: ", "NIP: ", "Bank account: "]
        self.type = ""
        self.create()

    def fill(self):
        font = Font(family="Bookman Old Style", size=16)
        font_small = Font(family="Bookman Old Style", size=12)
        if self.company:
            for i in range(len(self.company[0]) - 1):
                left = tk.Label(self.window, text=self.help[i].upper(), bg='#778899',
                                font=font)
                x = StringVar()
                x.set(str(self.company[0][i + 1]))
                # TODO we to zmien

                text = Text(self.window, bg="lightgrey", font=font, height=1)
                text.insert(INSERT, x.get())
                text.config(state=DISABLED)
                left.pack()
                text.pack(padx=10)
                self.type = "Update"
        else:
            text = Text(self.window, bg="#f8deb4", height=1)
            text.tag_configure("center", justify='center')
            text.insert(INSERT, "You haven't added any company so far")
            text.tag_add("center", "1.0", "end")
            text.config(state=DISABLED)
            text.pack(pady=10, padx=10)
            self.type = "Add"

    def delete(self):
        if messagebox.askyesno("Delete", "Are you sure?", parent=self.window):
            db.remove_company(1)
            self.window.destroy()

    def create(self):
        self.window.title("Company")
        if self.company:
            self.window.geometry('600x450')
        else:
            self.window.geometry('600x120')
        self.window.resizable(0, 0)
        self.window['bg'] = '#778899'
        self.fill()

        update = tk.Button(self.window, text=self.type, padx=20, pady=10, command=lambda: EditCompany(self.window))
        update.pack(pady=(15, 10))

        if self.company:
            delete = tk.Button(self.window, text="Delete", padx=20, pady=10, command=self.delete)
            delete.pack()