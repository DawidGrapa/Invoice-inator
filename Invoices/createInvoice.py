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



