import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Validators.validators import *
from Database.db import Database

db = Database('Database/Database.db')


class UpdateProductWindow:
    def __init__(self, parent_window, app, product_list, selected):
        self.window = Toplevel(app)
        self.parent = parent_window
        self.pr_list = product_list
        self.data = dict()
        self.selected = selected
        self.expand_window()

    def update_in_base(self):
        res, x = validate_product(self.data)
        if res:
            db.update_product(self.selected[0], self.data['name'].get(), self.data['unit'].get(), self.data['vat'].get(), self.data['price'].get())
            messagebox.showinfo("Success", "Updated successfully!", parent=self.window)
            self.parent.update_button['state'] = DISABLED
            self.parent.delete_button['state'] = DISABLED
            self.parent.show_products()
            self.window.destroy()
        else:
            messagebox.showinfo("Wrong arguments", "Wrong argument: " + str(x) + "!", parent=self.window)

    def expand_window(self):
        self.window.title("Update product")
        self.window.minsize(450, 200)
        self.window.resizable(0, 0)

        # Labels and Entries
        # Name
        name = tk.Label(self.window, text="Product Name:", height=2, padx=10)
        name.grid(row=1, column=1)
        name_input = tk.Entry(self.window, width=50, bd=3)
        name_input.grid(row=1, column=2)
        name_input.insert(0, self.selected[1])

        self.data['name'] = name_input

        # Unit
        unit = tk.Label(self.window, text="Unit:", height=2, padx=10)
        unit.grid(row=2, column=1)
        unit_input = tk.Entry(self.window, width=50, bd=3)
        unit_input.grid(row=2, column=2)
        unit_input.insert(0, self.selected[2])

        self.data['unit'] = unit_input

        # VAT
        vat = tk.Label(self.window, text="VAT value in %:", height=2, padx=10)
        vat.grid(row=3, column=1)
        vat_input = tk.Entry(self.window, width=50, bd=3)
        vat_input.grid(row=3, column=2)
        vat_input.insert(0, self.selected[3])

        self.data['vat'] = vat_input

        # Price
        price = tk.Label(self.window, text="Unit price:", height=2, padx=10)
        price.grid(row=4, column=1)
        price_input = tk.Entry(self.window, width=50, bd=3)
        price_input.grid(row=4, column=2)
        price_input.insert(0, self.selected[4])

        self.data['price'] = price_input

        # Submit
        submit_label = tk.Button(self.window, text="Submit", command=self.update_in_base)
        submit_label.grid(row=7, column=2)
