import tkinter as tk
from tkinter import *
from tkinter.ttk import *

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

    addContrahentButton = tk.Button(L1,text="Add new contractor",height=2,width = 20)
    addContrahentButton.pack(fill=BOTH,side=LEFT, expand=True)
    deleteContractorButton = tk.Button(L2,text="Delete contractor",height=2,width=20)
    deleteContractorButton.pack(fill=BOTH,side=LEFT, expand=True)