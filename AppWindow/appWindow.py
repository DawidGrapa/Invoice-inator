import subprocess
import os
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

from Company.companyWindow import CompanyWindow
from Contractors.showContactorsWindow import ContractorsWindow
from Invoices.chooseContractorWindow import ChooseContractorWindow
from Invoices.showInvoicesWindow import ShowInvoicesWindow
from Products.showProductsWindow import ProductsWindow
from PopUpWindows.aboutUsWindow import open_about_us_window
from PopUpWindows.dateFormatSettings import DateFormatSettings

from Database.db import Database
db = Database('Database/Database.db')


class AppWindow:
    def __init__(self):
        self.app = Tk()
        self.soyphoto = PhotoImage(file='Media/soy.png')
        self.color1 = '#778899'
        self.color2 = '#999999'

        self.menu = Menu(self.app)
        self.panedwindow = Panedwindow(self.app, orient=HORIZONTAL)
        self.frame1 = tk.Frame(self.panedwindow, relief=SUNKEN, bg=self.color1)
        self.frame2 = tk.Frame(self.panedwindow, relief=SUNKEN, bg=self.color2)
        self.createInvoice_button = None
        self.company_button = None

        self.create_app_window()

    # Opening new window so that we can create an invoice
    def start_creating_invoice(self):
        if db.get_company():
            ChooseContractorWindow(self.frame2, self)
        else:
            tk.messagebox.showinfo(title="Error", message="You have to add your company first!")

    @staticmethod
    def open_getting_started():
        this_folder = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(this_folder, '../Media/getting_started.pdf')
        subprocess.Popen([file_name], shell=True)

    # Creating top menu
    def create_menu(self):
        settings_menu = Menu(self.menu, tearoff=False)

        help_menu = Menu(self.menu, tearoff=False)
        help_menu.add_command(label="Getting started", command=self.open_getting_started)
        help_menu.add_separator()
        help_menu.add_command(label="About us", command=lambda: open_about_us_window(self.app))

        settings_menu.add_command(label="Invoice settings", command=lambda: DateFormatSettings(self.app))

        self.menu.add_cascade(label="Settings", menu=settings_menu)
        self.menu.add_cascade(label="Help", menu=help_menu)

    def create_app_window(self):
        self.app.title("invoice-inator")
        self.app.state("zoomed")
        self.app.iconphoto(True, self.soyphoto)
        self.app.config(menu=self.menu)

        self.create_menu()

        # Splitting main window
        self.panedwindow.pack(fill=BOTH, expand=1)
        self.panedwindow.add(self.frame1, weight=1)
        self.panedwindow.add(self.frame2, weight=15)

        # Creating 5 main buttons
        create_invoice = tk.Label(self.frame1, bg=self.color1)
        invoices = tk.Label(self.frame1, bg=self.color1)
        contractors = tk.Label(self.frame1, bg=self.color1)
        products = tk.Label(self.frame1, bg=self.color1)
        company = tk.Label(self.frame1, bg=self.color1)
        create_invoice.pack()
        invoices.pack()
        contractors.pack()
        products.pack()
        company.pack()

        # Adding logo at the bottom
        logo = Image.open('Media/soy_invoice.png')
        logo_resized = logo.resize((320, 70), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo_resized)
        logo_label = Label(self.frame1, image=logo)
        logo_label.pack(side=tk.BOTTOM, pady=30)

        # Creating buttons part2 :)
        create_button_png = PhotoImage(file='Media/create_button.png')
        invoices_button_png = PhotoImage(file='Media/invoices_button.png')
        contractors_button_png = PhotoImage(file='Media/contractors_button.png')
        products_button_png = PhotoImage(file='Media/products_button.png')
        company_button_png = PhotoImage(file='Media/company_button.png')

        self.createInvoice_button = tk.Button(create_invoice, image=create_button_png, highlightthickness=0, bd=0,
                                              command=self.start_creating_invoice, borderwidth=0)
        invoices_button = tk.Button(invoices, image=invoices_button_png, highlightthickness=0, bd=0,
                                    command=lambda: ShowInvoicesWindow(self.app))
        contractors_button = tk.Button(contractors, image=contractors_button_png, highlightthickness=0, bd=0,
                                       command=lambda: ContractorsWindow(self.app))

        products_button = tk.Button(products, image=products_button_png, highlightthickness=0, bd=0,
                                    command=lambda: ProductsWindow(self.app))
        self.company_button = tk.Button(company, image=company_button_png, highlightthickness=0, bd=0,
                                        command=lambda: CompanyWindow(self.app))

        self.createInvoice_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        invoices_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        contractors_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        products_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        self.company_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)

        # Starting the program
        self.app.mainloop()
