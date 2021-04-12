import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from db import Database
from tkinter import messagebox, font
from validators import *

db = Database('contractors.db')


def select_item(event):
    try:
        if contractors_list.size()>0:
            updateContrahentButton['state'] = ACTIVE
            deleteContractorButton['state'] = ACTIVE
            global selected_item
            index = contractors_list.curselection()[0]
            selected_item = contractors_list.get(index)
    except IndexError:
        pass


def remove_contractor():
    if messagebox.askyesno("Delete", "Are you sure?",parent = contractor_window):
        db.remove_contractor(selected_item[0])
        updateContrahentButton['state'] = DISABLED
        deleteContractorButton['state'] = DISABLED
        show_contractors()



def show_contractors():
    contractors_list.delete(0, END)
    bolded = font.Font(weight='bold')  # will use the default font
    contractors_list.config(font=bolded)
    for row in db.fetch_contractors():
        if row[6]=="":
            contractors_list.insert(END, row[:6])
        else :
            contractors_list.insert(END, row)


def add_contractor_to_base(data):
    if add_contractor_validator(data):
        db.insert_contractor(data['name'].get(), data['street'].get(), data['zip'].get(), data['city'].get(), data['nip'].get(), data['desc'].get())
        messagebox.showinfo("Success", "Added successfully!", parent=contractor_add_window)
        show_contractors()
        contractor_add_window.destroy()
    else:
        messagebox.showinfo("Wrong arguments","Wrong arguments", parent=contractor_add_window)

def update_contractor_in_base(data):
    if add_contractor_validator(data):
        db.update_contractor(selected_item[0],data['name'].get(), data['street'].get(), data['zip'].get(), data['city'].get(), data['nip'].get(), data['desc'].get())
        messagebox.showinfo("Success", "Updated successfully!", parent=contractor_update_window)
        updateContrahentButton['state'] = DISABLED
        deleteContractorButton['state'] = DISABLED
        show_contractors()
        contractor_update_window.destroy()
    else:
        messagebox.showinfo("Wrong arguments","Wrong arguments",parent = contractor_update_window)


def update_contractor_window(app):
    global contractor_update_window
    contractor_update_window = Toplevel(app)
    contractor_update_window.title("Update contractor")
    contractor_update_window.minsize(500, 260)

    # Dictionary for storing collected data
    contractorData = dict()

    # Labels and Entries
    # Name
    name = tk.Label(contractor_update_window, text="Company Name:", height=2, padx=10)
    name.grid(row=1, column=1)
    nameInput = tk.Entry(contractor_update_window, width=50, bd=3)
    nameInput.grid(row=1, column=2)
    nameInput.insert(0,selected_item[1])

    contractorData['name'] = nameInput

    # Street
    street = tk.Label(contractor_update_window, text="Street:", height=2, padx=10)
    street.grid(row=2, column=1)
    streetInput = tk.Entry(contractor_update_window, width=50, bd=3)
    streetInput.grid(row=2, column=2)
    streetInput.insert(0,selected_item[2])
    contractorData['street'] = streetInput

    # ZIP-CODE
    zipCode = tk.Label(contractor_update_window, text="Zip-Code:", height=2, padx=10)
    zipCode.grid(row=3, column=1)
    zipInput = tk.Entry(contractor_update_window, width=50, bd=3)
    zipInput.grid(row=3, column=2)
    zipInput.insert(0, selected_item[3])
    contractorData['zip'] = zipInput

    # City
    city = tk.Label(contractor_update_window, text="City:", height=2, padx=10)
    city.grid(row=4, column=1)
    cityInput = tk.Entry(contractor_update_window, width=50, bd=3)
    cityInput.grid(row=4, column=2)
    cityInput.insert(0, selected_item[4])
    contractorData['city'] = cityInput

    # NIP
    nip = tk.Label(contractor_update_window, text="NIP:", height=2, padx=10)
    nip.grid(row=5, column=1)
    nipInput = tk.Entry(contractor_update_window, width=50, bd=3)
    nipInput.grid(row=5, column=2)
    nipInput.insert(0, selected_item[5])

    contractorData['nip'] = nipInput

    # Description
    desc = tk.Label(contractor_update_window, text="Description:", height=2, padx=10)
    desc.grid(row=6, column=1)
    descInput = tk.Entry(contractor_update_window, width=50, bd=3)
    descInput.grid(row=6, column=2)
    descInput.insert(0, selected_item[6])
    contractorData['desc'] = descInput

    # Submit
    submitLabel = tk.Button(contractor_update_window, text="Submit",
                            command=lambda: update_contractor_in_base(contractorData))
    submitLabel.grid(row=7, column=2)


def add_contractor_window(app):
    global contractor_add_window
    contractor_add_window = Toplevel(app)
    contractor_add_window.title("Add new contractor")
    contractor_add_window.minsize(500, 260)

    # Dictionary for storing collected data
    contractorData = dict()

    # Labels and Entries
    # Name
    name = tk.Label(contractor_add_window, text="Company Name:", height=2, padx=10)
    name.grid(row=1, column=1)
    nameInput = tk.Entry(contractor_add_window, width=50, bd=3)
    nameInput.grid(row=1, column=2)

    contractorData['name'] = nameInput

    # Street
    street = tk.Label(contractor_add_window, text="Street:", height=2, padx=10)
    street.grid(row=2, column=1)
    streetInput = tk.Entry(contractor_add_window, width=50, bd=3)
    streetInput.grid(row=2, column=2)

    contractorData['street'] = streetInput

    # ZIP-CODE
    zipCode = tk.Label(contractor_add_window, text="Zip-Code:", height=2, padx=10)
    zipCode.grid(row=3, column=1)
    zipInput = tk.Entry(contractor_add_window, width=50, bd=3)
    zipInput.grid(row=3, column=2)

    contractorData['zip'] = zipInput

    # City
    city = tk.Label(contractor_add_window, text="City:", height=2, padx=10)
    city.grid(row=4, column=1)
    cityInput = tk.Entry(contractor_add_window, width=50, bd=3)
    cityInput.grid(row=4, column=2)

    contractorData['city'] = cityInput

    # NIP
    nip = tk.Label(contractor_add_window, text="NIP:", height=2, padx=10)
    nip.grid(row=5, column=1)
    nipInput = tk.Entry(contractor_add_window, width=50, bd=3)
    nipInput.grid(row=5, column=2)

    contractorData['nip'] = nipInput

    # Description
    desc = tk.Label(contractor_add_window, text="Description:", height=2, padx=10)
    desc.grid(row=6, column=1)
    descInput = tk.Entry(contractor_add_window, width=50, bd=3)
    descInput.grid(row=6, column=2)

    contractorData['desc'] = descInput

    # Submit
    submitLabel = tk.Button(contractor_add_window, text="Submit", command=lambda: add_contractor_to_base(contractorData))
    submitLabel.grid(row=7, column=2)


def open_contractors_window(app):
    # Creating new window
    global contractor_window
    contractor_window = Toplevel(app)
    contractor_window.title("Contractors")
    contractor_window.geometry('900x500')
    contractor_window.minsize(900, 100)
    contractor_window['bg'] = '#f8deb4'

    # Creating PanedWindow - for splitting frames in ratio
    panedwindow = Panedwindow(contractor_window, orient=HORIZONTAL)
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
                                    command=lambda: add_contractor_window(contractor_window))
    addContrahentButton.pack(fill=BOTH, side=LEFT, expand=True)

    global updateContrahentButton
    updateContrahentButton = tk.Button(updateContLabel, text="Update contractor", height=2, width=20, padx=5, pady=5,
                                    command=lambda: update_contractor_window(contractor_window))
    updateContrahentButton.pack(fill=BOTH, side=LEFT, expand=True)

    global deleteContractorButton
    deleteContractorButton = tk.Button(deleteContLabel, text="Delete contractor", height=2, width=20, padx = 5, pady=5,
                                       command=remove_contractor)
    deleteContractorButton.pack(fill=BOTH, side=LEFT, expand=True)

    updateContrahentButton['state']=DISABLED
    deleteContractorButton['state']=DISABLED
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

