from Database.db import Database
from tkinter import *
from tkinter.ttk import *
from Invoices.createInvoice import CreateInvoice

db = Database('Database/Database.db')


class ChooseContractorWindow:
    def __init__(self, app):
        self.app = app
        self.main_window = Toplevel(app)
        self.selected = None
        self.ctr_list = Treeview()

        self.choose_contractor_window()

    def show_contractors(self):
        self.ctr_list.delete(*self.ctr_list.get_children())
        for row in db.fetch_contractors():
            if row[6] == "":
                self.ctr_list.insert(parent='', index='end', text="A", values=row[:6])
            else:
                self.ctr_list.insert(parent='', index='end', text="A", values=row)

    def show_selected(self, value):
        if value.get():
            self.ctr_list.delete(*self.ctr_list.get_children())
            for row in db.fetch_contractors():
                if any(value.get().lower() in sublist for sublist in row[1:]):
                    if row[6] == "":
                        self.ctr_list.insert(parent='', index='end', text="A", values=row[:6])
                    else:
                        self.ctr_list.insert(parent='', index='end', text="A", values=row)
        else:
            self.show_contractors()

    def select_item(self, event):
        try:
            if len(self.ctr_list.get_children()) > 0:
                self.selected = self.ctr_list.item(self.ctr_list.focus())["values"]
                CreateInvoice(self.main_window, self.selected)
        except IndexError:
            pass

    def choose_contractor_window(self):
        self.main_window.title("Choose contractor")
        self.main_window.geometry('900x487')
        self.main_window.resizable(0, 0)
        self.main_window['bg'] = '#f8deb4'

        # Right side of window
        def on_click(event):
            e.configure(state=NORMAL)
            e.delete(0, END)

        # search tool
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.show_selected(sv))
        e = Entry(self.main_window, textvariable=sv, width=60)
        e.insert(0, "Search contractor...")
        e.configure(state=DISABLED)
        e.bind('<Button-1>', on_click)
        e.pack(side=TOP, pady=10)
        self.ctr_list = Treeview(self.main_window, height=23)

        self.ctr_list['columns'] = ("ID", "Name", 'Street', 'Zip-Code', 'City', 'NIP', 'Desc')
        self.ctr_list.column("#0", width=0, stretch=NO)
        self.ctr_list.column("ID", anchor=W, width=30)
        self.ctr_list.column("Name", anchor=W, width=100)
        self.ctr_list.column("Street", anchor=W, width=100)
        self.ctr_list.column("Zip-Code", anchor=W, width=100)
        self.ctr_list.column("City", anchor=W, width=100)
        self.ctr_list.column("NIP", anchor=W, width=100)
        self.ctr_list.column("Desc", anchor=W, width=100)

        self.ctr_list.heading("ID", text="ID", anchor=W)
        self.ctr_list.heading("Name", text="Name", anchor=W)
        self.ctr_list.heading("Street", text="Street", anchor=W)
        self.ctr_list.heading("Zip-Code", text="Zip-Code", anchor=W)
        self.ctr_list.heading("City", text="City", anchor=W)
        self.ctr_list.heading("NIP", text="NIP", anchor=W)
        self.ctr_list.heading("Desc", text="Desc", anchor=W)

        # Create scrollbar
        scrollbar = Scrollbar(self.main_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        # Set scroll to listbox
        self.ctr_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.ctr_list.yview)
        # Bind select
        self.ctr_list.bind("<Double-1>", self.select_item)

        self.show_contractors()
        self.ctr_list.pack(fill=BOTH)
