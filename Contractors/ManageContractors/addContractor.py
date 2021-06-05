import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Validators.validators import *

from Database.db import Database
db = Database('Database/Database.db')


class AddContractorWindow:
    def __init__(self, parent, app, contractor_list):
        self.app = app
        self.window = Toplevel(app)
        self.parent = parent
        self.ctr_list = contractor_list
        self.data = dict()
        self.expand_window()

    def add_to_base(self):
        res, x = validate_contractor(self.data)
        if res:
            db.insert_contractor(self.data['name'].get(), self.data['street'].get(), self.data['zip'].get(),
                                 self.data['city'].get(), self.data['nip'].get(), self.data['desc'].get())
            messagebox.showinfo("Success", "Added successfully!", parent=self.window)
            self.parent.show_contractors()
            self.window.destroy()
        else:
            messagebox.showinfo("Wrong arguments", "Wrong argument: " + str(x) + "!", parent=self.window)

    def expand_window(self):
        self.window.title("Add new contractor")
        width = self.app.winfo_screenwidth()
        height = self.app.winfo_screenheight()
        self.window.geometry('%dx%d+%d+%d' % (500, 260, width//2-250, height//2-130))
        self.window.resizable(0, 0)

        # Labels and Entries
        # Name
        name = tk.Label(self.window, text="Company Name:", height=2, padx=10)
        name.grid(row=1, column=1)
        name_input = tk.Entry(self.window, width=50, bd=3)
        name_input.grid(row=1, column=2)

        self.data['name'] = name_input

        # Street
        street = tk.Label(self.window, text="Street:", height=2, padx=10)
        street.grid(row=2, column=1)
        street_input = tk.Entry(self.window, width=50, bd=3)
        street_input.grid(row=2, column=2)

        self.data['street'] = street_input

        # Zip-code
        zipcode = tk.Label(self.window, text="Zip-Code:", height=2, padx=10)
        zipcode.grid(row=3, column=1)
        zip_input = tk.Entry(self.window, width=50, bd=3)
        zip_input.grid(row=3, column=2)

        self.data['zip'] = zip_input

        # City
        city = tk.Label(self.window, text="City:", height=2, padx=10)
        city.grid(row=4, column=1)
        city_input = tk.Entry(self.window, width=50, bd=3)
        city_input.grid(row=4, column=2)

        self.data['city'] = city_input

        # NIP
        nip = tk.Label(self.window, text="NIP:", height=2, padx=10)
        nip.grid(row=5, column=1)
        nip_input = tk.Entry(self.window, width=50, bd=3)
        nip_input.grid(row=5, column=2)

        self.data['nip'] = nip_input

        # Description
        desc = tk.Label(self.window, text="Description:", height=2, padx=10)
        desc.grid(row=6, column=1)
        desc_input = tk.Entry(self.window, width=50, bd=3)
        desc_input.grid(row=6, column=2)

        self.data['desc'] = desc_input

        # Submit button
        submit_label = tk.Button(self.window, text="Submit", command=self.add_to_base)
        submit_label.grid(row=7, column=2)
