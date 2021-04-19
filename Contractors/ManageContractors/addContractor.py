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
        res = validate_contractor(self.data)
        if res == True:
            db.insert_contractor(self.data['name'].get(), self.data['street'].get(), self.data['zip'].get(),
                                 self.data['city'].get(), self.data['nip'].get(), self.data['desc'].get())
            messagebox.showinfo("Success", "Added successfully!", parent=self.window)
            self.parent.show_contractors()
            self.window.destroy()
        else:
            messagebox.showinfo("Wrong arguments", "Wrong argument: " + str(res) + "!", parent=self.window)

    def expand_window(self):
        self.window.title("Add new contractor")
        self.window.minsize(500, 260)
        self.window.resizable(0, 0)

        # Labels and Entries
        # Name
        name = tk.Label(self.window, text="Company Name:", height=2, padx=10)
        name.grid(row=1, column=1)
        nameInput = tk.Entry(self.window, width=50, bd=3)
        nameInput.grid(row=1, column=2)

        self.data['name'] = nameInput

        # Street
        street = tk.Label(self.window, text="Street:", height=2, padx=10)
        street.grid(row=2, column=1)
        streetInput = tk.Entry(self.window, width=50, bd=3)
        streetInput.grid(row=2, column=2)

        self.data['street'] = streetInput

        # ZIP-CODE
        zipCode = tk.Label(self.window, text="Zip-Code:", height=2, padx=10)
        zipCode.grid(row=3, column=1)
        zipInput = tk.Entry(self.window, width=50, bd=3)
        zipInput.grid(row=3, column=2)

        self.data['zip'] = zipInput

        # City
        city = tk.Label(self.window, text="City:", height=2, padx=10)
        city.grid(row=4, column=1)
        cityInput = tk.Entry(self.window, width=50, bd=3)
        cityInput.grid(row=4, column=2)

        self.data['city'] = cityInput

        # NIP
        nip = tk.Label(self.window, text="NIP:", height=2, padx=10)
        nip.grid(row=5, column=1)
        nipInput = tk.Entry(self.window, width=50, bd=3)
        nipInput.grid(row=5, column=2)

        self.data['nip'] = nipInput

        # Description
        desc = tk.Label(self.window, text="Description:", height=2, padx=10)
        desc.grid(row=6, column=1)
        descInput = tk.Entry(self.window, width=50, bd=3)
        descInput.grid(row=6, column=2)

        self.data['desc'] = descInput

        # Submit
        submitLabel = tk.Button(self.window, text="Submit", command=lambda: self.add_to_base())
        submitLabel.grid(row=7, column=2)
