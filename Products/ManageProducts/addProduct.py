import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Validators.validators import *
from Database.db import Database

db = Database('Database/Database.db')

def show_products(productsList):
    productsList.delete(*productsList.get_children())
    for row in db.fetch_products():
        productsList.insert(parent='', index='end', text="A", values=row)


def add_product_to_base(data, productAddWindow, productsList):
    res = add_product_validator(data)
    if res == True:
        db.insert_product(data['name'].get(), data['unit'].get(), data['vat'].get(), data['price'].get())
        messagebox.showinfo("Success", "Added successfully!", parent=productAddWindow)
        show_products(productsList)
        productAddWindow.destroy()
    else:
        messagebox.showinfo("Wrong arguments","Wrong argument: " + str(res) +"!", parent=productAddWindow)

def add_product_window(app, productsList):
    productAddWindow = Toplevel(app)
    productAddWindow.title("Add new product")
    productAddWindow.minsize(450, 200)
    productAddWindow.resizable(0,0)

    # Dictionary for storing collected data
    productData = dict()

    # Labels and Entries
    # Name
    name = tk.Label(productAddWindow, text="Product Name:", height=2, padx=10)
    name.grid(row=1, column=1)
    nameInput = tk.Entry(productAddWindow, width=50, bd=3)
    nameInput.grid(row=1, column=2)

    productData['name'] = nameInput

    # Unit
    unit = tk.Label(productAddWindow, text="Unit:", height=2, padx=10)
    unit.grid(row=2, column=1)
    unitInput = tk.Entry(productAddWindow, width=50, bd=3)
    unitInput.grid(row=2, column=2)

    productData['unit'] = unitInput

    # VAT
    vat = tk.Label(productAddWindow, text="VAT value in %:", height=2, padx=10)
    vat.grid(row=3, column=1)
    vatInput = tk.Entry(productAddWindow, width=50, bd=3)
    vatInput.grid(row=3, column=2)

    productData['vat'] = vatInput

    # Price
    price = tk.Label(productAddWindow, text="Price:", height=2, padx=10)
    price.grid(row=4, column=1)
    priceInput = tk.Entry(productAddWindow, width=50, bd=3)
    priceInput.grid(row=4, column=2)

    productData['price'] = priceInput

    # Submit
    submitLabel = tk.Button(productAddWindow, text="Submit", command=lambda: add_product_to_base(productData, productAddWindow, productsList))
    submitLabel.grid(row=7, column=2)