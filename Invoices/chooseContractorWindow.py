from tkinter import *
from tkinter.ttk import *
from Invoices.createInvoiceWindow import CreateInvoiceWindow

from Database.db import Database
db = Database('Database/Database.db')


class ChooseContractorWindow:
    def __init__(self, app, main_app):
        self.main_app = main_app
        self.app = app
        self.main_window = Toplevel(app)
        self.color = '#999999'
        self.selected = None
        self.ctr_list = Treeview()
        self.choose_contractor_window()

    def create_contractors_list(self):
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

    def show_contractors(self):
        self.ctr_list.delete(*self.ctr_list.get_children())
        for row in db.fetch_contractors():
            if row[6] == "":
                self.ctr_list.insert(parent='', index='end', text=row[5], values=row[:6])
            else:
                self.ctr_list.insert(parent='', index='end', text=row[5], values=row)

    def select_item(self, event):
        try:
            if len(self.ctr_list.get_children()) > 0:
                self.selected = self.ctr_list.item(self.ctr_list.focus())["values"]
                self.selected[5] = self.ctr_list.item(self.ctr_list.focus())["text"]
                if self.selected:
                    self.create_invoice()
        except IndexError:
            pass

    # Function to show lines with searched word (from search tool)
    def show_selected(self, value):
        if value.get():
            self.ctr_list.delete(*self.ctr_list.get_children())
            for row in db.fetch_contractors():
                if any(value.get().lower() in sublist.lower() for sublist in row[1:]):
                    if row[6] == "":
                        self.ctr_list.insert(parent='', index='end', text=row[5], values=row[:6])
                    else:
                        self.ctr_list.insert(parent='', index='end', text=row[5], values=row)
        else:
            self.show_contractors()

    def create_invoice(self):
        CreateInvoiceWindow(self.selected, self.main_window, self.app, self.main_app)
        self.main_app.createInvoice_button['state'] = DISABLED

    def choose_contractor_window(self):
        self.main_window.title("Choose contractor")
        width = self.app.winfo_screenwidth()
        height = self.app.winfo_screenheight()
        self.main_window.geometry('%dx%d+%d+%d' % (900, 487, width // 2 - 450, height // 2 - 240))
        self.main_window.resizable(0, 0)
        self.main_window['bg'] = self.color

        # Right side of window
        def on_click(event):
            e.configure(state=NORMAL)
            e.delete(0, END)

        # Search tool
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.show_selected(sv))
        e = Entry(self.main_window, textvariable=sv, width=60)
        e.insert(0, "Search contractor...")
        e.configure(state=DISABLED)
        e.bind('<Button-1>', on_click)
        e.pack(side=TOP, pady=10)

        # Creating list of contractors
        self.create_contractors_list()

        # Bind select
        self.ctr_list.bind("<Double-1>", self.select_item)

        self.show_contractors()
        self.ctr_list.pack(fill=BOTH)
