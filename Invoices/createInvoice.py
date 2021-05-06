from Database.db import Database
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import datetime

db = Database('Database/Database.db')


class CreateInvoice:
    def __init__(self, selected, app, main_app):
        self.window = main_app
        self.selected = selected
        self.contractors_window = app
        self.create_invoice_window()

    def create_invoice_window(self):
        self.contractors_window.destroy()

        # First row
        label1 = tk.Label(self.window, bg="#f8deb4")
        label1.pack(side=tk.TOP, anchor='w')

        invoice_no = tk.Label(label1, bg="orange", text="Invoice number: ", height=1, padx=5)
        invoice_no.grid(row=1, column=1)

        def on_click(event):
            invoice_no_input.configure(state=NORMAL)
            invoice_no_input.delete(0, END)

        invoice_no_input = tk.Entry(label1, width=5)
        invoice_no_input.insert(0, "1")
        invoice_no_input.configure(state=DISABLED)
        invoice_no_input.bind('<Button-1>', on_click)
        invoice_no_input.bind("<Return>", lambda e: label1.focus())
        invoice_no_input.grid(row=1, column=2, pady=1)

        invoice_no_pattern = tk.Text(label1, bg="lightgrey", width=10, height=1)
        invoice_no_pattern.insert(1.0, "AB/CD/EF")
        invoice_no_pattern.configure(state='disabled')
        invoice_no_pattern.grid(row=1, column=3)

        issue_date = tk.Label(label1, bg="orange", text="Issue date: ", height=1)
        issue_date.grid(row=1, column=4, padx=(10, 0))

        year = datetime.datetime.today().year
        date = DateEntry(label1, width=12, bg="darkblue", fg="white", date_pattern='dd/mm/y', year=year)
        date.grid(row=1, column=5)

        paid = tk.Label(label1, bg="orange", text="Payment: ", height=1)
        paid.grid(row=1, column=6, padx=(10, 0))

        suwak = Combobox(label1, width=13, state="readonly")
        suwak.bind("<<ComboboxSelected>>", lambda e: label1.focus())
        suwak['values'] = ("cash", "bank transfer")
        suwak.current(1)
        suwak.grid(row=1, column=7)

        # Second row
        label2 = tk.Label(self.window, bg="#f8deb4")
        label2.pack(side=tk.TOP, anchor='w')

        name = tk.Label(label2, bg="orange", text="Contractor name: ", height=1, padx=4)
        name.grid(row=1, column=1)

        contractor_name = tk.Text(label2, bg="lightgrey", width=10, height=1)
        contractor_name.insert(1.0, self.selected[1])
        contractor_name.configure(state='disabled')
        contractor_name.grid(row=1, column=2)

        nip = tk.Label(label2, bg="orange", text="NIP: ", height=1)
        nip.grid(row=1, column=3, padx=(10, 0))

        contractor_nip = tk.Text(label2, bg="lightgrey", width=10, height=1)
        contractor_nip.insert(1.0, self.selected[5])
        contractor_nip.configure(state='disabled')
        contractor_nip.grid(row=1, column=4)
