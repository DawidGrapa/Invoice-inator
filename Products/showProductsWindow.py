import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from Products.ManageProducts.addProduct import AddProductWindow
from Products.ManageProducts.updateProduct import UpdateProductWindow
from Database.db import Database
db = Database('Database/Database.db')


class ProductsWindow:
    def __init__(self, app):
        self.app = app
        self.window = Toplevel(app)
        self.prod_list = Treeview()
        self.selected = None
        self.frame2 = None
        self.add_button = tk.Button()
        self.update_button = tk.Button()
        self.delete_button = tk.Button()
        self.open_products_window()

    def show_products(self):
        self.prod_list.delete(*self.prod_list.get_children())
        for row in db.fetch_products():
            self.prod_list.insert(parent='', index='end', text="A", values=row)

    def remove_product(self):
        if tk.messagebox.askyesno("Delete", "Are you sure?", parent=self.window):
            db.remove_product(self.selected[0])
            self.update_button['state'] = DISABLED
            self.delete_button['state'] = DISABLED
            self.show_products()

    def select_item(self, event):
        try:
            if len(self.prod_list.get_children()) > 0:
                self.selected = self.prod_list.item(self.prod_list.focus())["values"]
                if len(self.selected) > 0:
                    self.update_button['state'] = ACTIVE
                    self.delete_button['state'] = ACTIVE
        except IndexError:
            pass

    # Function to show lines with searched word (from search tool)
    def show_selected(self, value):
        if value.get():
            self.prod_list.delete(*self.prod_list.get_children())
            for row in db.fetch_products():
                if any(value.get().lower() in sublist.lower() for sublist in row[1:3]):
                    self.prod_list.insert(parent='', index='end', text="A", values=row)
        else:
            self.show_products()

    def create_products_list(self):
        self.prod_list = Treeview(self.frame2, height=22)

        self.prod_list['columns'] = ("ID", "ProductName", 'Unit', 'VAT', 'Unit price')
        self.prod_list.column("#0", width=0, stretch=NO)
        self.prod_list.column("ID", anchor=W, width=30)
        self.prod_list.column("ProductName", anchor=W, width=100)
        self.prod_list.column("Unit", anchor=W, width=100)
        self.prod_list.column("VAT", anchor=W, width=100)
        self.prod_list.column("Unit price", anchor=W, width=100)

        self.prod_list.heading("ID", text="ID", anchor=W)
        self.prod_list.heading("ProductName", text="Product Name", anchor=W)
        self.prod_list.heading("Unit", text="Unit", anchor=W)
        self.prod_list.heading("VAT", text="VAT", anchor=W)
        self.prod_list.heading("Unit price", text="Unit price", anchor=W)

        # Create scrollbar
        scrollbar = Scrollbar(self.frame2)
        scrollbar.pack(side=RIGHT, fill=Y)
        # Set scroll to listbox
        self.prod_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.prod_list.yview)
        # Bind select
        self.prod_list.bind("<ButtonRelease-1>", lambda event: self.select_item(event))

        self.show_products()
        self.prod_list.pack(fill=BOTH)

    def open_products_window(self):
        self.window.title("Products")
        self.window.resizable(0, 0)
        self.window['bg'] = '#999999'

        width = self.app.winfo_screenwidth()
        height = self.app.winfo_screenheight()
        self.window.geometry('%dx%d+%d+%d' % (900, 487, width//2-450, height//2-243))

        # Creating PanedWindow - for splitting frames in ratio
        panedwindow = Panedwindow(self.window, orient=HORIZONTAL)
        panedwindow.pack(fill=BOTH, expand=True)

        frame1 = tk.Frame(panedwindow, width=100, height=300, relief=SUNKEN, bg='#778899')
        self.frame2 = tk.Frame(panedwindow, width=400, height=400, relief=SUNKEN, bg='#999999')
        panedwindow.add(frame1, weight=1)
        panedwindow.add(self.frame2, weight=4)

        # Creating left frame - buttons
        add_label = tk.Label(frame1, bg='#778899')
        update_label = tk.Label(frame1, bg='#778899')
        delete_label = tk.Label(frame1, bg='#778899')
        add_label.pack()
        update_label.pack()
        delete_label.pack()

        self.add_button = tk.Button(add_label, text="Add new product", height=2, width=20, padx=5, pady=5,
                                    command=lambda: AddProductWindow(self, self.window, self.prod_list))
        self.add_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)

        self.update_button = tk.Button(update_label, text="Update product", height=2, width=20, padx=5, pady=5,
                                       command=lambda: UpdateProductWindow(self, self.window, self.prod_list,
                                                                           self.selected))
        self.update_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)

        self.delete_button = tk.Button(delete_label, text="Delete product", height=2, width=20, padx=5, pady=5,
                                       command=lambda: self.remove_product())
        self.delete_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)

        self.update_button['state'] = DISABLED
        self.delete_button['state'] = DISABLED

        # Creating right frame - search tool and a list of products
        def on_click(event):
            e.configure(state = NORMAL)
            e.delete(0, END)

        # Search tool
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.show_selected(sv))
        e = Entry(self.frame2, textvariable=sv, width = 60)
        e.insert(0, "Search product...")
        e.configure(state=DISABLED)
        e.bind('<Button-1>', on_click)
        e.pack(side = TOP, pady =10)

        # List of products
        self.create_products_list()
