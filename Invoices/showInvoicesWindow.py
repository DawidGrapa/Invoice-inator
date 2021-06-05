import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from Invoices.saveAsPdf import PDF
from Database.db import Database
db = Database('Database/Database.db')


class ShowInvoicesWindow:
    def __init__(self, app):
        self.app = app
        self.main_window = Toplevel(app)
        self.invoices_list = Treeview()
        self.selected = None
        self.delete_button = None
        self.save_button = None
        self.width = self.app.winfo_screenwidth()
        self.height = self.app.winfo_screenheight()
        self.open_invoices_window()

    def select_item(self, event):
        try:
            if len(self.invoices_list.get_children()) > 0:
                self.selected = self.invoices_list.item(self.invoices_list.focus())["values"]
                if len(self.selected) > 0:
                    self.delete_button['state'] = ACTIVE
                    self.save_button['state'] = ACTIVE
        except IndexError:
            pass

    # Function to show lines with searched word (from search tool)
    def show_selected(self, value):
        if value.get():
            self.invoices_list.delete(*self.invoices_list.get_children())
            for row in db.fetch_invoices():
                if any(value.get().lower() in sublist.lower() for sublist in row[2:6]):
                    self.invoices_list.insert(parent='', index='end', text="A", values=row[1:])
        else:
            self.show_invoices()

    def show_invoices(self):
        self.invoices_list.delete(*self.invoices_list.get_children())
        for row in db.fetch_invoices():
            self.invoices_list.insert(parent='', index='end', text="A", values=row[1:4])

    def delete_invoice(self):
        if messagebox.askyesno("Delete", "Are you sure?", parent=self.main_window):
            db.remove_invoice(self.selected[0])
            self.delete_button['state'] = DISABLED
            self.show_invoices()

    def open_invoices_window(self):
        self.main_window.title("Invoices")
        self.main_window.geometry('%dx%d+%d+%d' % (900, 487, self.width//2 - 450, self.height//2 - 240))
        self.main_window.resizable(0, 0)
        self.main_window['bg'] = '#999999'

        # Creating PanedWindow - for splitting frames in ratio
        panedwindow = Panedwindow(self.main_window, orient=HORIZONTAL)
        panedwindow.pack(fill=BOTH, expand=True)

        frame1 = tk.Frame(panedwindow, width=100, height=300, relief=SUNKEN, bg='#778899')
        frame2 = tk.Frame(panedwindow, width=400, height=400, relief=SUNKEN, bg='#999999')
        panedwindow.add(frame1, weight=1)
        panedwindow.add(frame2, weight=4)

        # Creating left frame - buttons
        delete_label = tk.Label(frame1, bg='#778899')
        delete_label.pack()
        save_label = tk.Label(frame1, bg='#778899')
        save_label.pack()

        self.delete_button = tk.Button(delete_label, text="Delete invoice", height=2, width=20, padx=5, pady=5,
                                       command=self.delete_invoice)
        self.delete_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)

        self.save_button = tk.Button(save_label, text="Save invoice", height=2, width=20, padx=5, pady=5,
                                     command=lambda: PDF())
        self.save_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)

        self.delete_button['state'] = DISABLED
        self.save_button['state'] = DISABLED

        # Creating right frame - search tool and invoices list
        def on_click(event):
            e.configure(state=NORMAL)
            e.delete(0, END)

        # Search tool
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.show_selected(sv))
        e = Entry(frame2, textvariable=sv, width=60)
        e.insert(0, "Search invoice...")
        e.configure(state=DISABLED)
        e.bind('<Button-1>', on_click)
        e.pack(side=TOP, pady=10)

        # List of invoices
        self.invoices_list = Treeview(frame2, height=23)

        self.invoices_list['columns'] = ("ID", "Name", 'Date')
        self.invoices_list.column("#0", width=0, stretch=NO)
        self.invoices_list.column("ID", anchor=W, width=30)
        self.invoices_list.column("Name", anchor=W, width=100)
        self.invoices_list.column("Date", anchor=W, width=100)

        self.invoices_list.heading("ID", text="ID", anchor=W)
        self.invoices_list.heading("Name", text="Contractor name", anchor=W)
        self.invoices_list.heading("Date", text="Date", anchor=W)

        # Create scrollbar
        scrollbar = Scrollbar(frame2)
        scrollbar.pack(side=RIGHT, fill=Y)
        # Set scroll to listbox
        self.invoices_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.invoices_list.yview)
        # Bind select
        self.invoices_list.bind("<ButtonRelease-1>", self.select_item)

        self.show_invoices()
        self.invoices_list.pack(fill=BOTH)
