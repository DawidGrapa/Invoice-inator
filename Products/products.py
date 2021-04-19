from tkinter.ttk import *
from Products.ManageProducts.addProduct import *
from Products.ManageProducts.deleteProduct import remove_product

db = Database('Database/Database.db')


def select_item(event, productsList, update, delete):
    try:
        if len(productsList.get_children())>0:
            global selectedItem
            selectedItem = productsList.item(productsList.focus())["values"]
            if len(selectedItem) > 0:
                update['state'] = ACTIVE
                delete['state'] = ACTIVE
    except IndexError:
        pass


def open_products_window(app):
    # Creating new window
    productsMainWindow = Toplevel(app)
    productsMainWindow.title("Products")
    productsMainWindow.geometry('900x487')
    productsMainWindow.resizable(0, 0)
    productsMainWindow['bg'] = '#f8deb4'

    # Creating PanedWindow - for splitting frames in ratio
    panedwindow = Panedwindow(productsMainWindow, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)

    # Creating Left Frame
    fram1 = tk.Frame(panedwindow, width=100, height=300, relief=SUNKEN, bg='#f8deb4')
    fram2 = tk.Frame(panedwindow, width=400, height=400, relief=SUNKEN, bg='#94dbd6')
    panedwindow.add(fram1, weight=1)
    panedwindow.add(fram2, weight=4)

    #Creating Buttons
    addProductLabel = tk.Label(fram1)
    addProductLabel.pack()
    updateProductLabel = tk.Label(fram1)
    updateProductLabel.pack()
    deleteProductLabel = tk.Label(fram1)
    deleteProductLabel.pack()

    addProductButton = tk.Button(addProductLabel, text="Add new product", height=2, width=20, padx=5, pady=5, command = lambda: add_product_window(productsMainWindow, productsList))
    addProductButton.pack(fill=BOTH, side=LEFT, expand=True)

    updateProductButton = tk.Button(updateProductLabel, text="Update product", height=2, width=20, padx=5, pady=5)
    updateProductButton.pack(fill=BOTH, side=LEFT, expand=True)

    deleteProductButton = tk.Button(deleteProductLabel, text="Delete product", height=2, width=20, padx=5, pady=5, command = lambda : remove_product(productsMainWindow, selectedItem,updateProductButton, deleteProductButton, productsList))
    deleteProductButton.pack(fill=BOTH, side=LEFT, expand=True)

    updateProductButton['state'] = DISABLED
    deleteProductButton['state'] = DISABLED

    # Right side of window
    productsList = Treeview(fram2, height=23)

    productsList['columns'] = ("ID", "ProductName", 'Unit', 'VAT', 'Price')
    productsList.column("#0", width=0, stretch=NO)
    productsList.column("ID", anchor=W, width=30)
    productsList.column("ProductName", anchor=W, width=100)
    productsList.column("Unit", anchor=W, width=100)
    productsList.column("VAT", anchor=W, width=100)
    productsList.column("Price", anchor=W, width=100)

    productsList.heading("ID", text="ID", anchor=W)
    productsList.heading("ProductName", text="Product Name", anchor=W)
    productsList.heading("Unit", text="Unit", anchor=W)
    productsList.heading("VAT", text="VAT", anchor=W)
    productsList.heading("Price", text="Netto price", anchor=W)

    # Create scrollbar
    scrollbar = Scrollbar(fram2)
    scrollbar.pack(side=RIGHT, fill=Y)
    # Set scroll to listbox
    productsList.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=productsList.yview)
    # Bind select
    productsList.bind("<ButtonRelease-1>", lambda event: select_item(event, productsList,updateProductButton,deleteProductButton))

    show_products(productsList)
    productsList.pack(fill=BOTH)