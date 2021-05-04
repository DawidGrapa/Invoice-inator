from PopUpWindows.about_us_window import *
from Products.products import *
from Contractors.contractors import *
from Invoices.invoices import *
from Invoices.invoices import ChooseContractorWindow
from Contractors.contractors import ContractorsWindow
from Products.products import ProductsWindow


class MainWindow:
    def __init__(self):
        self.app = Tk()
        self.photo = PhotoImage(file='Media/soy.png')
        self.my_menu = Menu(self.app)
        self.panedwindow = Panedwindow(self.app, orient=HORIZONTAL)
        self.frame1 = tk.Frame(self.panedwindow, width=100, relief=SUNKEN, bg='#f8deb4')
        self.frame2 = tk.Frame(self.panedwindow, width=400, relief=SUNKEN, bg='#f8deb4')

        self.createMainWindow()

    def createMainWindow(self):
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

        # splitting main window

        self.panedwindow.pack(fill=BOTH, expand=0)

        self.panedwindow.add(self.frame1, weight=1)
        self.panedwindow.add(self.frame2, weight=15)

        createInvoice = tk.Label(self.frame1, bg='#f8deb4')
        createInvoice.pack()
        contractors = tk.Label(self.frame1, bg='#f8deb4')
        contractors.pack()
        products = tk.Label(self.frame1, bg='#f8deb4')
        products.pack()

        self.createInvoice_button = tk.Button(createInvoice, text="Create Invoice", height=2,
                                              width=20, padx=2, pady=5,
                                              command=lambda: ChooseContractorWindow(self.frame2))

        self.contractors_button = tk.Button(contractors, text="Show contractors", height=2, width=20, padx=2, pady=5,
                                            command=lambda: ContractorsWindow(self.app))

        self.products_button = tk.Button(products, text="Show products", height=2, width=20, padx=2, pady=5,
                                         command=lambda: ProductsWindow(self.app))

        self.createInvoice_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        self.contractors_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        self.products_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)

        self.app.mainloop()
