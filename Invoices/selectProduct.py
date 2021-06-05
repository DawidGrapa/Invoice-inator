import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from Validators.validators import validate_quantity
from Database.db import Database
db = Database('Database/Database.db')


class SelectProductWindow:
    def __init__(self, app, treeview):
        self.app = app
        self.window = Toplevel(app)
        self.prod_list = Treeview()
        self.selected = None
        self.frame = None
        self.width = self.app.winfo_screenwidth()
        self.height = self.app.winfo_screenheight()
        self.treeview = treeview
        self.open_products_window()

    def open_quantity_window(self):
        quantity_window = Toplevel(self.window)
        quantity_window.title("Add quantity")
        quantity_window.geometry('%dx%d+%d+%d' % (250, 150, self.width//2-250, self.height//2-150))
        quantity_window.resizable(0, 0)
        quantity_window['bg'] = '#999999'

        label = tk.Label(quantity_window, text="Quantity: ", height=2, bg="#999999")
        label.pack(pady=(10, 0))
        quantity = tk.Entry(quantity_window, width=20, bd=3)
        quantity.pack()
        quantity.focus_set()
        submit = tk.Button(quantity_window, text="Submit", command=lambda: self.add_product(quantity))
        submit.pack(pady=(10, 0))

    # Adding new product to the list of products
    def add_product(self, quantity):
        if validate_quantity(quantity)[0]:
            values = []
            values.append(self.selected[0])
            values.append(self.selected[1])
            values.append(quantity.get().replace(",", '.'))
            values.append(self.selected[2])
            values.append(str(round(float(self.selected[4]) * float(values[2]), 2)))
            values.append(self.selected[3])
            values.append(round(float(values[4]) * (100+float(values[5])) / 100, 2))

            self.treeview.insert(parent='', index='end', text="A", values=values)
            self.window.destroy()

    def show_products(self):
        self.prod_list.delete(*self.prod_list.get_children())
        for row in db.fetch_products():
            self.prod_list.insert(parent='', index='end', text="A", values=row)

    def select_item(self, event):
        try:
            if len(self.prod_list.get_children()) > 0:
                self.selected = self.prod_list.item(self.prod_list.focus())["values"]
                # Opening window to get quantity of selected product
                if self.selected:
                    self.open_quantity_window()
        except IndexError:
            pass

    # Function to show lines with searched word (from search tool)
    def show_selected(self, value):
        if value.get():
            self.prod_list.delete(*self.prod_list.get_children())
            for row in db.fetch_products():
                if any(value.get().lower() in sublist.lower() for sublist in row[1:3]):
                    self.prod_list.insert(parent='', index='end', text="A", values=row, tag=('odd',))
        else:
            self.show_products()

    def create_products_list(self):
        self.prod_list = Treeview(self.frame, height=22)

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
        scrollbar = Scrollbar(self.frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        # Set scroll to listbox
        self.prod_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.prod_list.yview)
        # Bind select
        self.prod_list.bind("<Double-1>", lambda event: self.select_item(event))

        self.show_products()
        self.prod_list.pack(fill=X)

    def open_products_window(self):
        # Creating new window
        self.window.title("Products")
        self.window.geometry('%dx%d+%d+%d' % (900, 487, self.width // 2 - 450, self.height // 2 - 240))
        self.window.resizable(0, 0)
        self.window['bg'] = '#999999'

        # Creating left frame
        self.frame = tk.Frame(self.window, width=400, height=400, relief=SUNKEN, bg='#999999')
        self.frame.pack(fill=BOTH)

        # Right side of window
        def on_click(event):
            e.configure(state=NORMAL)
            e.delete(0, END)

        # Search tool
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.show_selected(sv))
        e = Entry(self.frame, textvariable=sv, width=60)
        e.insert(0, "Search product...")
        e.configure(state=DISABLED)
        e.bind('<Button-1>', on_click)
        e.pack(side=TOP, pady=10)

        # Creating list of products
        self.create_products_list()
