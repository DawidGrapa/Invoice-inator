import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from Contractors.ManageContractors.addContractor import AddContractorWindow
from Contractors.ManageContractors.updateContractor import UpdateContractorWindow

from Database.db import Database
db = Database('Database/Database.db')


class ContractorsWindow:
    def __init__(self, app):
        self.app = app
        self.main_window = Toplevel(app)
        self.color1 = '#778899'
        self.color2 = '#999999'
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

    def remove_contractor(self):
        if tk.messagebox.askyesno("Delete", "Are you sure?", parent=self.main_window):
            db.remove_contractor(self.selected[0])
            self.update_button['state'] = DISABLED
            self.delete_button['state'] = DISABLED
            self.show_contractors()

    def select_item(self, event):
        try:
            if len(self.ctr_list.get_children()) > 0:
                self.selected = self.ctr_list.item(self.ctr_list.focus())["values"]
                if len(self.selected) > 0:
                    self.update_button['state'] = ACTIVE
                    self.delete_button['state'] = ACTIVE
        except IndexError:
            pass

    # Function to show lines with searched word (from search tool)
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
        self.main_window.title("Contractors")
        width = self.app.winfo_screenwidth()
        height = self.app.winfo_screenheight()
        self.main_window.geometry('%dx%d+%d+%d' % (900, 487, width//2-450, height//2-243))
        self.main_window.resizable(0, 0)
        self.main_window['bg'] = self.color2

        # Creating PanedWindow - for splitting frames in ratio
        panedwindow = Panedwindow(self.main_window, orient=HORIZONTAL)
        panedwindow.pack(fill=BOTH, expand=True)

        self.frame1 = tk.Frame(panedwindow, width=100, height=300, relief=SUNKEN, bg=self.color1)
        self.frame2 = tk.Frame(panedwindow, width=400, height=400, relief=SUNKEN, bg=self.color2)
        panedwindow.add(self.frame1, weight=1)
        panedwindow.add(self.frame2, weight=4)

        # Creating left frame - buttons
        add_label = tk.Label(self.frame1, bg=self.color1)
        add_label.pack()
        update_label = tk.Label(self.frame1, bg=self.color1)
        update_label.pack()
        delete_label = tk.Label(self.frame1, bg=self.color1)
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

        # Creating right frame - search tool and contractors list
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

        # Creating list of contractors
        self.create_contractors_list()
