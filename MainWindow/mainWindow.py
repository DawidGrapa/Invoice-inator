from tkinter import font

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
        self.leftLabelColor = '#778899'
        self.frame1 = tk.Frame(self.panedwindow, width=100, relief=SUNKEN, bg=self.leftLabelColor)
        self.frame2 = tk.Frame(self.panedwindow, width=400, relief=SUNKEN, bg='#f8deb4')
        self.myFont = font.Font(family='Monoton')
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

        createInvoice = tk.Label(self.frame1, bg=self.leftLabelColor)
        createInvoice.pack()
        invoices = tk.Label(self.frame1, bg=self.leftLabelColor)
        invoices.pack()
        contractors = tk.Label(self.frame1, bg=self.leftLabelColor)
        contractors.pack()
        products = tk.Label(self.frame1, bg=self.leftLabelColor)
        products.pack()

        createInvoice_button = tk.Button(createInvoice, text="Create Invoice", bg="#B0C4DE", height=2,
                                              width=20,
                                              command=lambda: ChooseContractorWindow(self.frame2))
        invoices_button = tk.Button(invoices, text="Show invoices", height = 2, width=20)
        contractors_button = tk.Button(contractors, text="Show contractors", height=2, width=20,
                                            command=lambda: ContractorsWindow(self.app))

        products_button = tk.Button(products, text="Show products", height=2, width=20,
                                         command=lambda: ProductsWindow(self.app))

        products_button['font']=self.myFont
        createInvoice_button['font'] = self.myFont
        invoices_button['font'] = self.myFont
        contractors_button['font'] = self.myFont

        createInvoice_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        invoices_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        contractors_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)
        products_button.pack(fill=BOTH, side=LEFT, expand=True, pady=10)

        self.app.mainloop()
