import tkinter as tk
from tkinter import *
from Database.db import Database
from tkinter import messagebox
from tkinter.ttk import *
from Products.ManageProducts.addProduct import AddProductWindow

db = Database('Database/Database.db')


class ProductsWindow:
    def __init__(self, app):
        self.app = app
        self.window = Toplevel(app)
        self.prod_list = Treeview()
        self.selected = None
        self.add_button = tk.Button()
        self.update_button = tk.Button()
        self.delete_button = tk.Button()
        self.open_products_window()

    def select_item(self, event):
        try:
            if len(self.prod_list.get_children()) > 0:
                self.selected = self.prod_list.item(self.prod_list.focus())["values"]
                if len(self.selected) > 0:
                    self.update_button['state'] = ACTIVE
                    self.delete_button['state'] = ACTIVE
        except IndexError:
            pass

    def show_products(self):
        self.prod_list.delete(*self.prod_list.get_children())
        for row in db.fetch_products():
            self.prod_list.insert(parent='', index='end', text="A", values=row)

    def remove_product(self):
        if messagebox.askyesno("Delete", "Are you sure?", parent=self.window):
            db.remove_product(self.selected[0])
            self.update_button['state'] = DISABLED
            self.delete_button['state'] = DISABLED
            self.show_products()

    def open_products_window(self):
        # Creating new window
        self.window.title("Products")
        self.window.geometry('900x487')
        self.window.resizable(0, 0)
        self.window['bg'] = '#f8deb4'

        # Creating PanedWindow - for splitting frames in ratio
        panedwindow = Panedwindow(self.window, orient=HORIZONTAL)
        panedwindow.pack(fill=BOTH, expand=True)

        # Creating Left Frame
        fram1 = tk.Frame(panedwindow, width=100, height=300, relief=SUNKEN, bg='#f8deb4')
        fram2 = tk.Frame(panedwindow, width=400, height=400, relief=SUNKEN, bg='#94dbd6')
        panedwindow.add(fram1, weight=1)
        panedwindow.add(fram2, weight=4)

        # Creating Buttons
        add_label = tk.Label(fram1)
        update_label = tk.Label(fram1)
        delete_label = tk.Label(fram1)
        add_label.pack()
        update_label.pack()
        delete_label.pack()

        self.add_button = tk.Button(add_label, text="Add new product", height=2, width=20, padx=5, pady=5,
                                    command=lambda: AddProductWindow(self, self.window, self.prod_list))
        self.add_button.pack(fill=BOTH, side=LEFT, expand=True)

        self.update_button = tk.Button(update_label, text="Update product", height=2, width=20, padx=5, pady=5)
        self.update_button.pack(fill=BOTH, side=LEFT, expand=True)

        self.delete_button = tk.Button(delete_label, text="Delete product", height=2, width=20, padx=5, pady=5,
                                       command=lambda: self.remove_product())
        self.delete_button.pack(fill=BOTH, side=LEFT, expand=True)

        self.update_button['state'] = DISABLED
        self.delete_button['state'] = DISABLED

        # Right side of window
        self.prod_list = Treeview(fram2, height=23)

        self.prod_list['columns'] = ("ID", "ProductName", 'Unit', 'VAT', 'Price')
        self.prod_list.column("#0", width=0, stretch=NO)
        self.prod_list.column("ID", anchor=W, width=30)
        self.prod_list.column("ProductName", anchor=W, width=100)
        self.prod_list.column("Unit", anchor=W, width=100)
        self.prod_list.column("VAT", anchor=W, width=100)
        self.prod_list.column("Price", anchor=W, width=100)

        self.prod_list.heading("ID", text="ID", anchor=W)
        self.prod_list.heading("ProductName", text="Product Name", anchor=W)
        self.prod_list.heading("Unit", text="Unit", anchor=W)
        self.prod_list.heading("VAT", text="VAT", anchor=W)
        self.prod_list.heading("Price", text="Netto price", anchor=W)

        # Create scrollbar
        scrollbar = Scrollbar(fram2)
        scrollbar.pack(side=RIGHT, fill=Y)
        # Set scroll to listbox
        self.prod_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.prod_list.yview)
        # Bind select
        self.prod_list.bind("<ButtonRelease-1>", lambda event: self.select_item(event))

        self.show_products()
        self.prod_list.pack(fill=BOTH)