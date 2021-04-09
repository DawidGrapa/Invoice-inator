import tkinter as tk
from tkinter import *
from tkinter.ttk import *
#
# def save(contractor):
#     print(contractor)

def addContractor(app):
    newWindow = Toplevel(app)
    newWindow.title("Add new contractor")
    newWindow.minsize(600, 600)

    #Name
    name = tk.Label(newWindow, text="Company Name:", height=2,padx=10)
    name.grid(row=1, column=1)

    nameInput = tk.Entry(newWindow, width=50, bd=3)
    nameInput.grid(row=1, column=2)

    #Street
    street = tk.Label(newWindow,text="Street:",height = 2,padx=10)
    street.grid(row=2,column=1)

    streetInput = tk.Entry(newWindow, width=50, bd=3)
    streetInput.grid(row=2, column=2)

    #ZIP-CODE
    zip_code = tk.Label(newWindow,text="Zip-Code:",height = 2,padx=10)
    zip_code.grid(row=3,column=1)

    zipInput = tk.Entry(newWindow, width=50, bd=3)
    zipInput.grid(row=3, column=2)

    #City
    city = tk.Label(newWindow, text="City:", height=2, padx=10)
    city.grid(row=4, column=1)

    cityInput = tk.Entry(newWindow, width=50, bd=3)
    cityInput.grid(row=4, column=2)


    # #Submit
    # submitLabel = tk.Button(newWindow,text="Submit",command = lambda: save())
    # submitLabel.grid(row=3,column=1)




def open_contractors_window(app):
    newWindow = Toplevel(app)
    newWindow.title("Contractors")
    newWindow.geometry('700x500')
    newWindow['bg'] = '#f8deb4'
    newWindow.minsize(600,100)
    # Create Panedwindow
    panedwindow = Panedwindow(newWindow, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)
    # Create Frams
    fram1 = tk.Frame(panedwindow, width=100, height=300, relief=SUNKEN)
    fram2 = tk.Frame(panedwindow, width=400, height=400, relief=SUNKEN,bg = '#94dbd6')
    panedwindow.add(fram1, weight=1)
    panedwindow.add(fram2, weight=4)

    L1 = tk.Label(fram1)
    L1.pack()
    L2 = tk.Label(fram1)
    L2.pack()

    addContrahentButton = tk.Button(L1,text="Add new contractor",height=2,width = 20,command = lambda: addContractor(newWindow))
    addContrahentButton.pack(fill=BOTH,side=LEFT, expand=True)
    deleteContractorButton = tk.Button(L2,text="Delete contractor",height=2,width=20)
    deleteContractorButton.pack(fill=BOTH,side=LEFT, expand=True)