import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from Database.db import Database
from Contractors.ManageContractors.addContractor import AddContractorWindow
from Contractors.ManageContractors.updateContractor import UpdateContractorWindow

db = Database('Database/Database.db')


class ContractorsWindow:
    def __init__(self, app):
        self.app = app
        self.main_window = Toplevel(app)
        self.ctr_list = Treeview()
        self.selected = None
        self.frame1 = None
        self.frame2 = None
        self.add_button = tk.Button()
        self.update_button = tk.Button()
        self.delete_button = tk.Button()
        self.open_contractors_window()

    def show_contractors(self):
        self.ctr_list.delete(*self.ctr_list.get_children())
        for row in db.fetch_contractors():
            if row[6] == "":
                self.ctr_list.insert(parent='', index='end', text="A", values=row[:6])
            else:
                self.ctr_list.insert(parent='', index='end', text="A", values=row)

    def select_item(self, event):
        try:
            if len(self.ctr_list.get_children()) > 0:
                self.selected = self.ctr_list.item(self.ctr_list.focus())["values"]
                if len(self.selected) > 0:
                    self.update_button['state'] = ACTIVE
                    self.delete_button['state'] = ACTIVE
        except IndexError:
            pass

    def remove_contractor(self):
        if tk.messagebox.askyesno("Delete", "Are you sure?", parent=self.main_window):
            db.remove_contractor(self.selected[0])
            self.update_button['state'] = DISABLED
            self.delete_button['state'] = DISABLED
            self.show_contractors()

    def show_selected(self, value):
        if value.get():
            self.ctr_list.delete(*self.ctr_list.get_children())
            for row in db.fetch_contractors():
                if any(value.get().lower() in sublist.lower() for sublist in row[1:]):
                    if row[6] == "":
                        self.ctr_list.insert(parent='', index='end', text="A", values=row[:6])
                    else:
                        self.ctr_list.insert(parent='', index='end', text="A", values=row)
        else:
            self.show_contractors()

    def create_contractors_list(self):
        self.ctr_list = Treeview(self.frame2, height=23)

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
        scrollbar = Scrollbar(self.frame2)
        scrollbar.pack(side=RIGHT, fill=Y)
        # Set scroll to listbox
        self.ctr_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.ctr_list.yview)
        # Bind select
        self.ctr_list.bind("<ButtonRelease-1>", self.select_item)

        self.show_contractors()
        self.ctr_list.pack(fill=BOTH)

    def open_contractors_window(self):
        # Creating new window
        self.main_window.title("Contractors")
        self.main_window.geometry('900x487')
        self.main_window.resizable(0, 0)
        self.main_window['bg'] = '#999999'

        # Creating PanedWindow - for splitting frames in ratio
        panedwindow = Panedwindow(self.main_window, orient=HORIZONTAL)
        panedwindow.pack(fill=BOTH, expand=True)

        # Creating Left Frame
        self.frame1 = tk.Frame(panedwindow, width=100, height=300, relief=SUNKEN, bg='#778899')
        self.frame2 = tk.Frame(panedwindow, width=400, height=400, relief=SUNKEN, bg='#999999')
        panedwindow.add(self.frame1, weight=1)
        panedwindow.add(self.frame2, weight=4)

        add_label = tk.Label(self.frame1, bg='#778899')
        add_label.pack()
        update_label = tk.Label(self.frame1, bg='#778899')
        update_label.pack()
        delete_label = tk.Label(self.frame1, bg='#778899')
        delete_label.pack()

        self.add_button = tk.Button(add_label, text="Add new contractor", height=2, width=20, padx=5, pady=5,
                                    command=lambda: AddContractorWindow(self, self.main_window, self.ctr_list))

        self.update_button = tk.Button(update_label, text="Update contractor", height=2, width=20, padx=5, pady=5,
                                       command=lambda: UpdateContractorWindow(self, self.main_window, self.ctr_list,
                                                                              self.selected))

        self.delete_button = tk.Button(delete_label, text="Delete contractor", height=2, width=20, padx=5, pady=5,
                                       command=self.remove_contractor)
        self.add_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        self.update_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        self.delete_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)

        self.update_button['state'] = DISABLED
        self.delete_button['state'] = DISABLED

        # Right side of window
        def on_click(event):
            e.configure(state=NORMAL)
            e.delete(0, END)

        # Search tool
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.show_selected(sv))
        e = Entry(self.frame2, textvariable=sv, width=60)
        e.insert(0, "Search contractor...")
        e.configure(state=DISABLED)
        e.bind('<Button-1>', on_click)
        e.pack(side=TOP, pady=10)

        # contractors_list
        self.create_contractors_list()
