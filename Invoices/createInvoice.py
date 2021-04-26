from Database.db import Database
from tkinter import *
from tkinter.ttk import *

db = Database('Database/Database.db')

class CreateInvoice:
    def __init__(self, app, selected):
        self.app = app
        self.main_window = Toplevel(app)
        self.selected = selected
        self.create_invoice_window()

    def create_invoice_window(self):
        print(self.selected)
