from tkinter import *
from tkinter.ttk import Combobox

from Database.db import Database

db = Database('Database/Database.db')


class Settings:
    def __init__(self, app):
        self.format = None
        self.app = app
        self.window = Toplevel(self.app)
        self.open_settings_window()

    def save_settings(self):
        if db.get_settings():
            db.update_settings(1, self.format.get())
        else:
            db.add_settings(self.format.get())

    def open_settings_window(self):
        self.window.title("Settings")
        self.window.geometry('400x400')
        self.window.resizable(0, 0)
        self.window['bg'] = '#f8deb4'
        text = Text(self.window, bg="#ffccb3", font="Times 13", height=1)
        text.insert(INSERT, "Select format:")
        text.config(state=DISABLED)

        self.format = Combobox(self.window, width=27, text="Select format:")
        self.format.bind("<<ComboboxSelected>>", lambda e: self.window.focus())
        self.format['values'] = ('InvoiceNo/Month/Year', 'InvoiceNo/Year', 'InvoiceNo/Month')
        self.format.current(0)

        save = Button(self.window, text="Save", command=lambda: self.save_settings())

        text.pack(padx=20, pady=10)
        self.format.pack()
        save.pack(pady=20)
