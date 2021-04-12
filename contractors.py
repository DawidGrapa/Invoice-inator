import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from db import Database
from tkinter import messagebox, font
from validators import *

db = Database('contractors.db')


def select_item(event):
    try:
        if contractorsList.size()>0:
            updateContrahentButton['state'] = ACTIVE
            deleteContractorButton['state'] = ACTIVE
            global selectedItem
            index = contractorsList.curselection()[0]
            selectedItem = contractorsList.get(index)
    except IndexError:
        pass


def remove_contractor():
    if messagebox.askyesno("Delete", "Are you sure?", parent = contractorMainWindow):
        db.remove_contractor(selectedItem[0])
        updateContrahentButton['state'] = DISABLED
        deleteContractorButton['state'] = DISABLED
        show_contractors()


def show_contractors():
    contractorsList.delete(0, END)
    bolded = font.Font(weight='bold')  # will use the default font
    contractorsList.config(font=bolded)
    for row in db.fetch_contractors():
        if row[6] == "":
            contractorsList.insert(END, row[:6])
        else:
            contractorsList.insert(END, row)


def add_contractor_to_base(data):
    res = add_contractor_validator(data)
    if res == True:
        db.insert_contractor(data['name'].get(), data['street'].get(), data['zip'].get(), data['city'].get(), data['nip'].get(), data['desc'].get())
        messagebox.showinfo("Success", "Added successfully!", parent=contractorAddWindow)
        show_contractors()
        contractorAddWindow.destroy()
    else:
        messagebox.showinfo("Wrong arguments","Wrong argument: " + str(res) +"!", parent=contractorAddWindow)


def update_contractor_in_base(data):
    res = add_contractor_validator(data)
    if res == True:
        db.update_contractor(selectedItem[0], data['name'].get(), data['street'].get(), data['zip'].get(), data['city'].get(), data['nip'].get(), data['desc'].get())
        messagebox.showinfo("Success", "Updated successfully!", parent=contractorUpdateWindow)
        updateContrahentButton['state'] = DISABLED
        deleteContractorButton['state'] = DISABLED
        show_contractors()
        contractorUpdateWindow.destroy()
    else:
        messagebox.showinfo("Wrong arguments","Wrong argument: " + str(res) +"!", parent=contractorUpdateWindow)


def update_contractor_window(app):
    global contractorUpdateWindow
    contractorUpdateWindow = Toplevel(app)
    contractorUpdateWindow.title("Update contractor")
    contractorUpdateWindow.minsize(500, 260)

    # Dictionary for storing collected data
    contractorData = dict()

    # Labels and Entries
    # Name
    name = tk.Label(contractorUpdateWindow, text="Company Name:", height=2, padx=10)
    name.grid(row=1, column=1)
    nameInput = tk.Entry(contractorUpdateWindow, width=50, bd=3)
    nameInput.grid(row=1, column=2)
    nameInput.insert(0, selectedItem[1])

    contractorData['name'] = nameInput

    # Street
    street = tk.Label(contractorUpdateWindow, text="Street:", height=2, padx=10)
    street.grid(row=2, column=1)
    streetInput = tk.Entry(contractorUpdateWindow, width=50, bd=3)
    streetInput.grid(row=2, column=2)
    streetInput.insert(0, selectedItem[2])
    contractorData['street'] = streetInput

    # ZIP-CODE
    zipCode = tk.Label(contractorUpdateWindow, text="Zip-Code:", height=2, padx=10)
    zipCode.grid(row=3, column=1)
    zipInput = tk.Entry(contractorUpdateWindow, width=50, bd=3)
    zipInput.grid(row=3, column=2)
    zipInput.insert(0, selectedItem[3])
    contractorData['zip'] = zipInput

    # City
    city = tk.Label(contractorUpdateWindow, text="City:", height=2, padx=10)
    city.grid(row=4, column=1)
    cityInput = tk.Entry(contractorUpdateWindow, width=50, bd=3)
    cityInput.grid(row=4, column=2)
    cityInput.insert(0, selectedItem[4])
    contractorData['city'] = cityInput

    # NIP
    nip = tk.Label(contractorUpdateWindow, text="NIP:", height=2, padx=10)
    nip.grid(row=5, column=1)
    nipInput = tk.Entry(contractorUpdateWindow, width=50, bd=3)
    nipInput.grid(row=5, column=2)
    nipInput.insert(0, selectedItem[5])

    contractorData['nip'] = nipInput

    # Description
    desc = tk.Label(contractorUpdateWindow, text="Description:", height=2, padx=10)
    desc.grid(row=6, column=1)
    descInput = tk.Entry(contractorUpdateWindow, width=50, bd=3)
    descInput.grid(row=6, column=2)
    if len(selectedItem) > 6:
        descInput.insert(0, selectedItem[6])
    contractorData['desc'] = descInput

    # Submit
    submitLabel = tk.Button(contractorUpdateWindow, text="Submit",
                            command=lambda: update_contractor_in_base(contractorData))
    submitLabel.grid(row=7, column=2)


def add_contractor_window(app):
    global contractorAddWindow
    contractorAddWindow = Toplevel(app)
    contractorAddWindow.title("Add new contractor")
    contractorAddWindow.minsize(500, 260)

    # Dictionary for storing collected data
    contractorData = dict()

    # Labels and Entries
    # Name
    name = tk.Label(contractorAddWindow, text="Company Name:", height=2, padx=10)
    name.grid(row=1, column=1)
    nameInput = tk.Entry(contractorAddWindow, width=50, bd=3)
    nameInput.grid(row=1, column=2)

    contractorData['name'] = nameInput

    # Street
    street = tk.Label(contractorAddWindow, text="Street:", height=2, padx=10)
    street.grid(row=2, column=1)
    streetInput = tk.Entry(contractorAddWindow, width=50, bd=3)
    streetInput.grid(row=2, column=2)

    contractorData['street'] = streetInput

    # ZIP-CODE
    zipCode = tk.Label(contractorAddWindow, text="Zip-Code:", height=2, padx=10)
    zipCode.grid(row=3, column=1)
    zipInput = tk.Entry(contractorAddWindow, width=50, bd=3)
    zipInput.grid(row=3, column=2)

    contractorData['zip'] = zipInput

    # City
    city = tk.Label(contractorAddWindow, text="City:", height=2, padx=10)
    city.grid(row=4, column=1)
    cityInput = tk.Entry(contractorAddWindow, width=50, bd=3)
    cityInput.grid(row=4, column=2)

    contractorData['city'] = cityInput

    # NIP
    nip = tk.Label(contractorAddWindow, text="NIP:", height=2, padx=10)
    nip.grid(row=5, column=1)
    nipInput = tk.Entry(contractorAddWindow, width=50, bd=3)
    nipInput.grid(row=5, column=2)

    contractorData['nip'] = nipInput

    # Description
    desc = tk.Label(contractorAddWindow, text="Description:", height=2, padx=10)
    desc.grid(row=6, column=1)
    descInput = tk.Entry(contractorAddWindow, width=50, bd=3)
    descInput.grid(row=6, column=2)

    contractorData['desc'] = descInput

    # Submit
    submitLabel = tk.Button(contractorAddWindow, text="Submit", command=lambda: add_contractor_to_base(contractorData))
    submitLabel.grid(row=7, column=2)


def open_contractors_window(app):
    # Creating new window
    global contractorMainWindow
    contractorMainWindow = Toplevel(app)
    contractorMainWindow.title("Contractors")
    contractorMainWindow.geometry('900x500')
    contractorMainWindow.minsize(900, 100)
    contractorMainWindow['bg'] = '#f8deb4'

    # Creating PanedWindow - for splitting frames in ratio
    panedwindow = Panedwindow(contractorMainWindow, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)

    # Creating Left Frame
    fram1 = tk.Frame(panedwindow, width=100, height=300, relief=SUNKEN, bg='#f8deb4')
    fram2 = tk.Frame(panedwindow, width=400, height=400, relief=SUNKEN, bg='#94dbd6')
    panedwindow.add(fram1, weight=1)
    panedwindow.add(fram2, weight=4)

    addContLabel = tk.Label(fram1)
    addContLabel.pack()
    updateContLabel = tk.Label(fram1)
    updateContLabel.pack()
    deleteContLabel = tk.Label(fram1)
    deleteContLabel.pack()


    addContrahentButton = tk.Button(addContLabel, text="Add new contractor", height=2, width=20, padx = 5, pady=5,
                                    command=lambda: add_contractor_window(contractorMainWindow))
    addContrahentButton.pack(fill=BOTH, side=LEFT, expand=True)

    global updateContrahentButton
    updateContrahentButton = tk.Button(updateContLabel, text="Update contractor", height=2, width=20, padx=5, pady=5,
                                       command=lambda: update_contractor_window(contractorMainWindow))
    updateContrahentButton.pack(fill=BOTH, side=LEFT, expand=True)

    global deleteContractorButton
    deleteContractorButton = tk.Button(deleteContLabel, text="Delete contractor", height=2, width=20, padx = 5, pady=5,
                                       command=remove_contractor)
    deleteContractorButton.pack(fill=BOTH, side=LEFT, expand=True)

    updateContrahentButton['state'] = DISABLED
    deleteContractorButton['state'] = DISABLED

    # Right side of window
    global contractorsList
    contractorsList = Listbox(fram2, height=20, width=70, border=0)
    contractorsList.grid(row=3, column=0, columnspan=4, rowspan=10, pady=20, padx=20)
    # Create scrollbar
    scrollbar = Scrollbar(fram2)
    scrollbar.grid(row=4, column=5)
    # Set scroll to listbox
    contractorsList.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=contractorsList.yview)
    # Bind select
    contractorsList.bind('<<ListboxSelect>>', select_item)

    show_contractors()

