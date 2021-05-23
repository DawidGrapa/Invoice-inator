from tkinter import *
from tkinter.font import Font
from tkinter import font, messagebox
from Company.editCompany import EditCompany
from Database.db import Database
import tkinter as tk
from tkinter.font import Font

from Validators.validators import validate_company

db = Database('Database/Database.db')


class CompanyWindow:
    def __init__(self, app):
        self.app = app
        self.window = Toplevel(app)
        self.company = db.get_company()
        self.data = dict()
        self.open_window()

    def update(self):
        res, x = validate_company(self.data)
        if res:
            if self.company:
                db.update_company(1, self.data['name'].get(), self.data['street'].get(), self.data['zip'].get(),
                                  self.data['city'].get(), self.data['nip'].get(), self.data['bank'].get())
                messagebox.showinfo("Success", "Updated successfully!", parent=self.window)
            else:
                db.add_company(self.data['name'].get(), self.data['street'].get(), self.data['zip'].get(),
                               self.data['city'].get(), self.data['nip'].get(), self.data['bank'].get())
                messagebox.showinfo("Success", "Updated successfully!", parent=self.window)
            self.window.destroy()
        else:
            messagebox.showinfo("Wrong arguments", "Wrong argument: " + str(x) + "!", parent=self.window)

    def open_window(self):
        self.window.title("Company")
        self.window.geometry("600x440")
        self.window.resizable(0, 0)
        self.window['bg'] = '#778899'

        font = Font(family="Bookman Old Style", size=16)
        font_small = Font(family="Bookman Old Style", size=12)

        # Name
        name = tk.Label(self.window, text="Company Name:", bg="#778899", font=font, padx=10)
        name.pack()
        name_input = tk.Entry(self.window, width=50, bd=3, bg="lightgrey", font=font_small)
        name_input.pack()
        self.data['name'] = name_input

        # Street
        street = tk.Label(self.window, text="Street:", bg="#778899",font=font, padx=10)
        street.pack()
        street_input = tk.Entry(self.window, width=50, bd=3, bg="lightgrey", font=font_small)
        street_input.pack()
        self.data['street'] = street_input

        # ZIP-CODE
        zipcode = tk.Label(self.window, text="Zip-Code:", bg="#778899", font=font, padx=10)
        zipcode.pack()
        zip_input = tk.Entry(self.window, width=50, bd=3, bg="lightgrey", font=font_small)
        zip_input.pack()
        self.data['zip'] = zip_input

        # City
        city = tk.Label(self.window, text="City:", bg="#778899", font=font, padx=10)
        city.pack()
        city_input = tk.Entry(self.window, width=50, bd=3, bg="lightgrey", font=font_small)
        city_input.pack()
        self.data['city'] = city_input

        # NIP
        nip = tk.Label(self.window, text="NIP:", bg="#778899", font=font, padx=10)
        nip.pack()
        nip_input = tk.Entry(self.window, width=50, bd=3, bg="lightgrey", font=font_small)
        nip_input.pack()
        self.data['nip'] = nip_input

        # Bank account number
        bank = tk.Label(self.window, text="Bank account number:", bg="#778899", font=font, padx=10)
        bank.pack()
        bank_input = tk.Entry(self.window, width=50, bd=3, bg="lightgrey", font=font_small)
        bank_input.pack()
        self.data['bank'] = bank_input

        # Buttons
        update_button = tk.Button(self.window, text="Update", command=self.update, width=20, height=2)
        update_button.pack(pady=20)
        if self.company:
            name_input.insert(0, self.company[0][1])
            street_input.insert(0, self.company[0][2])
            zip_input.insert(0, self.company[0][3])
            city_input.insert(0, self.company[0][4])
            nip_input.insert(0, self.company[0][5])
            bank_input.insert(0, self.company[0][6])
