import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from db import Database
from tkinter import messagebox, font

db = Database('contractors.db')

def select_item(event):
    try:
        global selected_item
        index = contractors_list.curselection()[0]
        selected_item = contractors_list.get(index)
    except IndexError:
        pass

def remove_contractor():
    if messagebox.askyesno("Delete","Are you sure?"):
        db.remove_contractor(selected_item[0])
        show_contractors()

def show_contractors():
    contractors_list.delete(0, END)
    bolded = font.Font(weight='bold')  # will use the default font
    contractors_list.config(font=bolded)
    for row in db.fetch_contractors():
        contractors_list.insert(END, row[:6])




def print_collected_data(data):
    for key, el in data.items():
        print(key, ': ', el.get())


def add_contractor_window(app):
    newWindow = Toplevel(app)
    newWindow.title("Add new contractor")
    newWindow.minsize(500, 260)

    # Dictionary for storing collected data
    contractorData = dict()

    # Labels and Entries
    # Name
    name = tk.Label(newWindow, text="Company Name:", height=2, padx=10)
    name.grid(row=1, column=1)
    nameInput = tk.Entry(newWindow, width=50, bd=3)
    nameInput.grid(row=1, column=2)

    contractorData['name'] = nameInput

    # Street
    street = tk.Label(newWindow, text="Street:", height=2, padx=10)
    street.grid(row=2, column=1)
    streetInput = tk.Entry(newWindow, width=50, bd=3)
    streetInput.grid(row=2, column=2)

    contractorData['street'] = streetInput

    # ZIP-CODE
    zipCode = tk.Label(newWindow, text="Zip-Code:", height=2, padx=10)
    zipCode.grid(row=3, column=1)
    zipInput = tk.Entry(newWindow, width=50, bd=3)
    zipInput.grid(row=3, column=2)

    contractorData['zip'] = zipInput

    # City
    city = tk.Label(newWindow, text="City:", height=2, padx=10)
    city.grid(row=4, column=1)
    cityInput = tk.Entry(newWindow, width=50, bd=3)
    cityInput.grid(row=4, column=2)

    contractorData['city'] = cityInput

    # NIP
    nip = tk.Label(newWindow, text="NIP:", height=2, padx=10)
    nip.grid(row=5, column=1)
    nipInput = tk.Entry(newWindow, width=50, bd=3)
    nipInput.grid(row=5, column=2)

    contractorData['nip'] = nipInput

    # Description
    desc = tk.Label(newWindow, text="Description:", height=2, padx=10)
    desc.grid(row=6, column=1)
    descInput = tk.Entry(newWindow, width=50, bd=3)
    descInput.grid(row=6, column=2)

    contractorData['desc'] = descInput

    # Submit
    submitLabel = tk.Button(newWindow, text="Submit", command=lambda: print_collected_data(contractorData))
    submitLabel.grid(row=7, column=2)


def open_contractors_window(app):
    # Creating new window
    newWindow = Toplevel(app)
    newWindow.title("Contractors")
    newWindow.geometry('700x500')
    newWindow.minsize(650, 100)
    newWindow['bg'] = '#f8deb4'

    # Creating PanedWindow - for splitting frames in ratio
    panedwindow = Panedwindow(newWindow, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)

    # Creating Left Frame
    fram1 = tk.Frame(panedwindow, width=100, height=300, relief=SUNKEN, bg='#f8deb4')
    fram2 = tk.Frame(panedwindow, width=400, height=400, relief=SUNKEN, bg='#94dbd6')
    panedwindow.add(fram1, weight=1)
    panedwindow.add(fram2, weight=4)

    addContLabel = tk.Label(fram1)
    addContLabel.pack()
    deleteContLabel = tk.Label(fram1)
    deleteContLabel.pack()

    addContrahentButton = tk.Button(addContLabel, text="Add new contractor", height=2, width=20,
                                    command=lambda: add_contractor_window(newWindow))
    addContrahentButton.pack(fill=BOTH, side=LEFT, expand=True)
    deleteContractorButton = tk.Button(deleteContLabel, text="Delete contractor", height=2, width=20,
                                       command=remove_contractor)
    deleteContractorButton.pack(fill=BOTH, side=LEFT, expand=True)

    #Right side of window
    global contractors_list
    contractors_list = Listbox(fram2, height=20, width=70, border=0)
    contractors_list.grid(row=3, column=0, columnspan=4, rowspan=10, pady=20, padx=20)
    # Create scrollbar
    scrollbar = Scrollbar(fram2)
    scrollbar.grid(row=4, column=5)
    # Set scroll to listbox
    contractors_list.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=contractors_list.yview)
    # Bind select
    contractors_list.bind('<<ListboxSelect>>', select_item)

    show_contractors()



