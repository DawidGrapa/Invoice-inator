from Database.db import Database
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import datetime
from Invoices.selectProduct import SelectProductWindow

db = Database('Database/Database.db')


class CreateInvoice:
    def __init__(self, selected, app, main_app, top):
        self.window = main_app
        self.selected = selected
        self.contractors_window = app
        self.top = top
        self.date = None
        self.payment = None
        self.prod_list = None
        self.create_invoice_window()

    def clean_window(self):
        for widget in self.top.frame2.winfo_children():
            widget.destroy()
            self.top.createInvoice_button['state'] = NORMAL
            self.top.company_button['state'] = NORMAL

    def add_invoice(self):
        db.add_invoice(self.selected[1], self.date.get(), self.payment.get())
        last = db.get_last_invoice()
        for line in self.prod_list.get_children():
            last = db.get_last_invoice()
            db.add_invoice_product(last[0], self.prod_list.item(line)['values'][1], self.prod_list.item(line)['values'][2], self.prod_list.item(line)['values'][3], self.prod_list.item(line)['values'][4], self.prod_list.item(line)['values'][5])

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
        invoice_no_input.insert(0, db.get_last_invoice()[0]+1)
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
        self.date = DateEntry(label1, width=12, bg="darkblue", fg="white", date_pattern='dd/mm/y', year=year)
        self.date.grid(row=1, column=5)

        paid = tk.Label(label1, bg="orange", text="Payment: ", height=1)
        paid.grid(row=1, column=6, padx=(10, 0))

        self.payment = Combobox(label1, width=13, state="readonly")
        self.payment.bind("<<ComboboxSelected>>", lambda e: label1.focus())
        self.payment['values'] = ("cash", "bank transfer")
        self.payment.current(1)
        self.payment.grid(row=1, column=7)

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

        # Third row - buttons
        label3 = tk.Label(self.window, bg="#f8deb4")
        label3.pack(side=tk.TOP, anchor='w', pady=(15, 0))

        add_product = tk.Button(label3, text="Add product", height=1, width=15, command=lambda:SelectProductWindow(self.window, self.prod_list))
        add_product.grid(row=1, column=1, padx=(0, 6))

        delete_product = tk.Button(label3, text="Delete product", height=1, width=15)
        delete_product['state'] = DISABLED
        delete_product.grid(row=1, column=2)

        # Fourth row - products treeview
        label4 = tk.Label(self.window, bg="#f8deb4")
        label4.pack(side=tk.TOP, anchor='w')

        # trying to change colors...
        style = Style().configure("Treeview", background="#383838", foreground="blue", fieldbackground="red")
        self.prod_list = Treeview(label4, height=22, style="Treeview")

        self.prod_list['columns'] = ("ID", "ProductName", 'Quantity', 'Unit', 'netto', 'VAT', 'brutto')
        self.prod_list.column("#0", width=0, stretch=NO)
        self.prod_list.column("ID", anchor=W, width=40)
        self.prod_list.column("ProductName", anchor=W, width=150)
        self.prod_list.column('Quantity', anchor=W, width=80)
        self.prod_list.column("Unit", anchor=W, width=55)
        self.prod_list.column("netto", anchor=W, width=85)
        self.prod_list.column("VAT", anchor=W, width=55)
        self.prod_list.column("brutto", anchor=W, width=85)

        self.prod_list.heading("ID", text="ID", anchor=W)
        self.prod_list.heading("ProductName", text="Product Name", anchor=W)
        self.prod_list.heading("Quantity", text="Quantity", anchor=W)
        self.prod_list.heading("Unit", text="Unit", anchor=W)
        self.prod_list.heading("netto", text="Netto", anchor=W)
        self.prod_list.heading("VAT", text="VAT", anchor=W)
        self.prod_list.heading("brutto", text="Brutto", anchor=W)

        self.prod_list.grid(row=1, column=1, pady=(1, 0))

        # Fifth row - more buttons
        label5 = tk.Label(self.window, bg="#f8deb4")
        label5.pack(side=tk.TOP, anchor='w')

        save = tk.Button(label5, text="Save", height=1, width=15, command=self.add_invoice)
        save.grid(row=1, column=1, padx=(0, 6))

        cancel = tk.Button(label5, text="Cancel", height=1, width=15, command=self.clean_window)
        cancel.grid(row=1, column=2)
