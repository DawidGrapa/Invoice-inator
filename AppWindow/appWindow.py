from tkinter import font
from Company.companyWindow import CompanyWindow
from PopUpWindows.about_us_window import *
from Products.products import *
from Contractors.contractors import *
from Invoices.invoices import *
from Invoices.invoices import ChooseContractorWindow
from Contractors.contractors import ContractorsWindow
from Products.products import ProductsWindow


class AppWindow:
    def __init__(self):
        self.app = Tk()
        self.photo = PhotoImage(file='Media/soy.png')
        self.my_menu = Menu(self.app)
        self.panedwindow = Panedwindow(self.app, orient=HORIZONTAL)
        self.leftLabelColor = '#778899'
        self.buttonColor = '#E6E6FA'
        self.createInvoice_button = None
        self.frame1 = tk.Frame(self.panedwindow, width=100, relief=SUNKEN, bg=self.leftLabelColor)
        self.frame2 = tk.Frame(self.panedwindow, width=400, relief=SUNKEN, bg='#f8deb4')
        self.myFont = font.Font(family='AngsanaUPC')
        self.create_app_window()

    def create_app_window(self):
        self.app.title("TBD Manager")
        self.app.state("zoomed")
        self.app['bg'] = '#f8deb4'
        self.app.iconphoto(True, self.photo)
        self.app.config(menu=self.my_menu)

        settings_menu = Menu(self.my_menu, tearoff=False)

        help_menu = Menu(self.my_menu, tearoff=False)
        help_menu.add_command(label="Getting started")
        help_menu.add_separator()
        help_menu.add_command(label="About us", command=lambda: open_about_us_window(self.app))

        self.my_menu.add_cascade(label="Settings", menu=settings_menu)
        self.my_menu.add_cascade(label="Help", menu=help_menu)

        # Splitting main window
        self.panedwindow.pack(fill=BOTH, expand=0)

        self.panedwindow.add(self.frame1, weight=1)
        self.panedwindow.add(self.frame2, weight=15)

        create_invoice = tk.Label(self.frame1, bg=self.leftLabelColor)
        invoices = tk.Label(self.frame1, bg=self.leftLabelColor)
        contractors = tk.Label(self.frame1, bg=self.leftLabelColor)
        products = tk.Label(self.frame1, bg=self.leftLabelColor)
        company = tk.Label(self.frame1, bg=self.leftLabelColor)
        create_invoice.pack()
        invoices.pack()
        contractors.pack()
        products.pack()
        company.pack()

        self.createInvoice_button = tk.Button(create_invoice, text="Create Invoice", bg=self.buttonColor, height=2,
                                              width=20, command=lambda: ChooseContractorWindow(self.frame2, self))
        invoices_button = tk.Button(invoices, text="Show invoices", height=2, width=20, bg=self.buttonColor)
        contractors_button = tk.Button(contractors, text="Show contractors", height=2, width=20, bg=self.buttonColor,
                                       command=lambda: ContractorsWindow(self.app))

        products_button = tk.Button(products, text="Show products", height=2, width=20, bg=self.buttonColor,
                                    command=lambda: ProductsWindow(self.app))
        company_button = tk.Button(company, text="My company", height=2, width=20, bg=self.buttonColor,
                                   command=lambda: CompanyWindow(self.app))

        products_button['font'] = self.myFont
        self.createInvoice_button['font'] = self.myFont
        invoices_button['font'] = self.myFont
        contractors_button['font'] = self.myFont
        company_button['font'] = self.myFont

        self.createInvoice_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        invoices_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        contractors_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        products_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        company_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)

        self.app.mainloop()
