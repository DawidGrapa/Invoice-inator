import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Database.db import Database
from Validators.validators import *

db = Database('Database/Database.db')


class AddProductWindow:
    def __init__(self, parent, app, product_list):
        self.parent = parent
        self.app = app
        self.window = Toplevel(app)
        self.pr_list = product_list
        self.data = dict()
        self.expand_window()

    def add_to_base(self):
        res, x = validate_product(self.data)
        if res:
            db.insert_product(self.data['name'].get(), self.data['unit'].get(), self.data['vat'].get(), self.data['price'].get())
            messagebox.showinfo("Success", "Added successfully!", parent=self.window)
            self.parent.show_products()
            self.window.destroy()
        else:
            messagebox.showinfo("Wrong arguments", "Wrong argument: " + str(x) + "!", parent=self.window)

    def expand_window(self):
        self.window.title("Add new product")
        self.window.minsize(450, 200)
        self.window.resizable(0, 0)

        # Labels and Entries
        # Name
        name = tk.Label(self.window, text="Product Name:", height=2, padx=10)
        name.grid(row=1, column=1)
        nameInput = tk.Entry(self.window, width=50, bd=3)
        nameInput.grid(row=1, column=2)

        self.data['name'] = nameInput

        # Unit
        unit = tk.Label(self.window, text="Unit:", height=2, padx=10)
        unit.grid(row=2, column=1)
        unitInput = tk.Entry(self.window, width=50, bd=3)
        unitInput.grid(row=2, column=2)

        self.data['unit'] = unitInput

        # VAT
        vat = tk.Label(self.window, text="VAT value in %:", height=2, padx=10)
        vat.grid(row=3, column=1)
        vatInput = tk.Entry(self.window, width=50, bd=3)
        vatInput.grid(row=3, column=2)

        self.data['vat'] = vatInput

        # Price
        price = tk.Label(self.window, text="Unit price:", height=2, padx=10)
        price.grid(row=4, column=1)
        priceInput = tk.Entry(self.window, width=50, bd=3)
        priceInput.grid(row=4, column=2)

        self.data['price'] = priceInput

        # Submit
        submitLabel = tk.Button(self.window, text="Submit", command=self.add_to_base)
        submitLabel.grid(row=7, column=2)