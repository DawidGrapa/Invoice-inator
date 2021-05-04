from Database.db import Database
from tkinter import *
from tkinter.ttk import *
import tkinter as tk

db = Database('Database/Database.db')


class CreateInvoice:
    def __init__(self, selected, app, main_app):
        self.window = main_app
        self.selected = selected
        self.contractors_window = app
        self.create_invoice_window()


    def create_invoice_window(self):
        self.contractors_window.destroy()
        name = tk.Label(self.window, text=self.selected, height=2, padx=10)
        name.grid(row=1, column=1)

