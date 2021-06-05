from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter.ttk import Combobox

from Database.db import Database
db = Database('Database/Database.db')


# Class used for creating small window where date format is chosen
class DateFormatSettings:
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
        messagebox.showinfo(title="Success", message="Saved!")
        self.window.destroy()

    def open_settings_window(self):
        self.window.title("Settings")
        self.window.resizable(0, 0)
        self.window['bg'] = '#778899'

        width = self.app.winfo_screenwidth()
        height = self.app.winfo_screenheight()
        self.window.geometry('%dx%d+%d+%d' % (300, 150, width // 2 - 150, height // 2 - 75))

        font = Font(family="Bookman Old Style", size=16)
        text = Text(self.window, bg="lightgrey", font=font, height=1)
        text.insert(INSERT, "Select date format")
        text.config(state=DISABLED)

        self.format = Combobox(self.window, width=27, state='readonly', text="Select format:")
        self.format.bind("<<ComboboxSelected>>", lambda e: self.window.focus())
        self.format['values'] = ('InvoiceNo/Month/Year', 'InvoiceNo/Year', 'InvoiceNo/Month')
        self.format.current(0)

        save = Button(self.window, text="Save", command=lambda: self.save_settings())

        text.pack(padx=20, pady=10)
        self.format.pack()
        save.pack(pady=20)
