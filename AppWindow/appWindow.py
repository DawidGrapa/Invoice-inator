from Company.companyWindow import CompanyWindow
from PopUpWindows.about_us_window import *
from Products.products import *
from Contractors.contractors import *
from Invoices.invoices import *
from Invoices.invoices import ChooseContractorWindow
from Contractors.contractors import ContractorsWindow
from Products.products import ProductsWindow
from Invoices.showInvoices import ShowInvoicesWindow
from PopUpWindows.settings import Settings

class AppWindow:
    def __init__(self):
        self.app = Tk()
        self.photo = PhotoImage(file='Media/soy.png')
        self.my_menu = Menu(self.app)
        self.panedwindow = Panedwindow(self.app, orient=HORIZONTAL)
        self.leftLabelColor = '#778899'
        self.buttonColor = '#E6E6FA'
        self.createInvoice_button = None
        self.company_button = None
        self.frame1 = tk.Frame(self.panedwindow, relief=SUNKEN, bg=self.leftLabelColor)
        self.frame2 = tk.Frame(self.panedwindow, relief=SUNKEN, bg='#f8deb4')
        self.create_app_window()

    def start_creating_invoice(self):
        if db.get_company():
            ChooseContractorWindow(self.frame2, self)
        else:
            messagebox.showinfo(title="Error", message="You have to add your company first!")

    def create_app_window(self):
        self.app.title("invoice-inator")
        self.app.state("zoomed")
        self.app['bg'] = '#f8deb4'
        self.app.iconphoto(True, self.photo)
        self.app.config(menu=self.my_menu)

        settings_menu = Menu(self.my_menu, tearoff=False)

        help_menu = Menu(self.my_menu, tearoff=False)
        help_menu.add_command(label="Getting started")
        help_menu.add_separator()
        help_menu.add_command(label="About us", command=lambda: open_about_us_window(self.app))

        settings_menu.add_command(label= "Invoice settings", command = lambda: Settings(self.app))

        self.my_menu.add_cascade(label="Settings", menu=settings_menu)
        self.my_menu.add_cascade(label="Help", menu=help_menu)

        # Splitting main window
        self.panedwindow.pack(fill=BOTH, expand=1)

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

        self.app.mainloop()
