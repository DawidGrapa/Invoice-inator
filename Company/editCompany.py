import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Validators.validators import *
from Database.db import Database

db = Database('Database/Database.db')

class EditCompany:
    def __init__(self, app):
        self.app = app
        self.window = Toplevel(app)
        self.company = db.get_company()
        self.data = dict()
        self.open_window()

    def update(self):
        if self.company:
            db.update_company(1, self.data['name'].get(), self.data['street'].get(), self.data['zip'].get(),
                                 self.data['city'].get(), self.data['nip'].get(), self.data['bank'].get())
            messagebox.showinfo("Success", "Updated successfully!", parent=self.window)
        else:
            db.add_company(self.data['name'].get(), self.data['street'].get(), self.data['zip'].get(),
                                 self.data['city'].get(), self.data['nip'].get(), self.data['bank'].get())
            messagebox.showinfo("Success", "Updated successfully!", parent=self.window)
        self.app.destroy()

    def open_window(self):
        self.window.title("Company")
        self.window.minsize(500, 260)

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

        # ZIP-CODE
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

        # Bank account number
        bank = tk.Label(self.window, text="Bank account number:", height=2, padx=10)
        bank.grid(row=6, column=1)
        bank_input = tk.Entry(self.window, width=50, bd=3)
        bank_input.grid(row=6, column=2)
        self.data['bank'] = bank_input

        #Buttons
        update_button = tk.Button(self.window, text="Update", padx=5, command=self.update)
        update_button.grid(row=7, column=2)
        if self.company:
            name_input.insert(0, self.company[0][1])
            street_input.insert(0, self.company[0][2])
            zip_input.insert(0, self.company[0][3])
            city_input.insert(0, self.company[0][4])
            nip_input.insert(0, self.company[0][5])
            bank_input.insert(0, self.company[0][6])