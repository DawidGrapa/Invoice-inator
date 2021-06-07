import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

import datetime
from tkcalendar import DateEntry

from Invoices.selectProductWindow import SelectProductWindow
from Invoices.saveAsPdf import PDF
from Validators.validators import validate_invoice_no

from Database.db import Database
db = Database('Database/Database.db')


class CreateInvoiceWindow:
    def __init__(self, selected, app, main_app, top_app):
        self.window = main_app
        self.selected = selected
        self.contractors_window = app
        self.color = "#999999"
        self.top_app = top_app

        self.date = None
        self.payment = None
        self.prod_list = None
        self.selected_product = None
        self.cancel = None
        self.delete_product = None
        self.invoice_no_pattern = None
        self.invoice_no_input = None

        self.settings = db.get_settings()
        self.create_invoice_window()

    # Insert date format
    def insert_pattern(self):
        today = datetime.date.today()
        res = self.settings[1]
        year = today.strftime("/%Y")
        month = today.strftime("/%m")

        if res == "InvoiceNo/Month":
            self.invoice_no_pattern.insert(1.0, month)
        elif res == "InvoiceNo/Month/Year":
            self.invoice_no_pattern.insert(1.0, month + year)
        elif res == "InvoiceNo/Year":
            self.invoice_no_pattern.insert(1.0, year)

    # Destroying window - right side of main app
    def clean_window(self):
        for widget in self.top_app.frame2.winfo_children():
            widget.destroy()
            self.top_app.createInvoice_button['state'] = NORMAL

    # Deleting product from treeview on delete button
    def delete_from_treeview(self):
        x = self.prod_list.selection()[0]
        self.prod_list.delete(x)
        self.delete_product['state'] = DISABLED

    def save_as_pdf(self):
        PDF()
        self.clean_window()

    def add_invoice(self):
        # Validating data
        if validate_invoice_no(self.invoice_no_input.get()) is False:
            tk.messagebox.showinfo(title="Error!", message="Wrong invoice number!")
        elif len(db.check_id(self.invoice_no_input.get())):
            tk.messagebox.showinfo(title="Error!", message="Invoice with this number exists!")
        elif len(self.prod_list.get_children()) == 0:
            tk.messagebox.showinfo(title="Error!", message="Add some products!")

        # Adding to database
        elif self.prod_list.get_children() and not len(db.check_id(self.invoice_no_input.get())):
            db.add_invoice(self.invoice_no_input.get(), self.selected[1], self.date.get(), self.payment.get(),
                           str(self.invoice_no_pattern.get(1.0, "end-1c")), self.selected[2], self.selected[3], self.selected[4], self.selected[5])
            last = db.get_last_invoice()

            for line in self.prod_list.get_children():
                product = db.get_product(self.prod_list.item(line)['values'][0])
                db.add_invoice_product(last[1], self.prod_list.item(line)['values'][1],
                                       self.prod_list.item(line)['values'][2], self.prod_list.item(line)['values'][3],
                                       self.prod_list.item(line)['values'][4], self.prod_list.item(line)['values'][5],
                                       self.prod_list.item(line)['values'][6], product[4])
            self.save_as_pdf()

    def select_item(self, event):
        try:
            if len(self.prod_list.get_children()) > 0:
                self.selected_product = self.prod_list.item(self.prod_list.focus())["values"]
                if self.selected_product:
                    self.delete_product['state'] = ACTIVE
        except IndexError:
            pass

    def create_products_list(self):
        prod_label = tk.Label(self.window, bg=self.color)
        prod_label.pack(side=tk.TOP, anchor='w')

        self.prod_list = Treeview(prod_label, height=24)
        self.prod_list.tag_configure('odd', background='#E8E8E8')
        self.prod_list['columns'] = ("ID", "ProductName", 'Quantity', 'Unit', 'Netto', 'VAT', 'Brutto')
        self.prod_list.column("#0", width=0, stretch=NO)
        self.prod_list.column("ID", anchor=W, width=40)
        self.prod_list.column("ProductName", anchor=W, width=300)
        self.prod_list.column('Quantity', anchor=W, width=90)
        self.prod_list.column("Unit", anchor=W, width=65)
        self.prod_list.column("Netto", anchor=W, width=95)
        self.prod_list.column("VAT", anchor=W, width=65)
        self.prod_list.column("Brutto", anchor=W, width=95)

        self.prod_list.heading("ID", text="ID", anchor=W)
        self.prod_list.heading("ProductName", text="Product Name", anchor=W)
        self.prod_list.heading("Quantity", text="Quantity", anchor=W)
        self.prod_list.heading("Unit", text="Unit", anchor=W)
        self.prod_list.heading("Netto", text="Netto", anchor=W)
        self.prod_list.heading("VAT", text="VAT", anchor=W)
        self.prod_list.heading("Brutto", text="Brutto", anchor=W)

        self.prod_list.bind("<ButtonRelease-1>", self.select_item)

        self.prod_list.grid(row=1, column=1, pady=(1, 0))

    # Big function to create big window:)
    def create_invoice_window(self):
        self.contractors_window.destroy()

        font = Font(family="Bookman Old Style", size=16)
        font_small = Font(family="Bookman Old Style", size=12)

        # First row - invoice number, date format, issue date and payment format
        label1 = tk.Label(self.window, bg=self.color)
        label1.pack(side=tk.TOP, anchor='w')

        invoice_no = tk.Label(label1, bg=self.color, text="Invoice number: ", font=font, height=2, padx=5, pady=1)
        invoice_no.grid(row=1, column=1)

        def on_click(event):
            self.invoice_no_input.configure(state=NORMAL)
            self.invoice_no_input.delete(0, END)

        self.invoice_no_input = tk.Entry(label1, font=font_small, width=5)
        self.invoice_no_input.insert(0, db.get_last_invoice()[1] + 1)
        self.invoice_no_input.configure(state=DISABLED)
        self.invoice_no_input.bind('<Button-1>', on_click)
        self.invoice_no_input.bind("<Return>", lambda e: label1.focus())
        self.invoice_no_input.grid(row=1, column=2, pady=1)

        self.invoice_no_pattern = tk.Text(label1, bg="lightgrey", font=font_small, width=10, height=1)
        self.insert_pattern()
        self.invoice_no_pattern.configure(state='disabled')
        self.invoice_no_pattern.grid(row=1, column=3)

        issue_date = tk.Label(label1, bg=self.color, text="Issue date: ", font=font, height=2)
        issue_date.grid(row=1, column=4, padx=(10, 0))

        year = datetime.datetime.today().year
        self.date = DateEntry(label1, width=12, bg="darkblue", fg="white", font=font_small, date_pattern='dd/mm/y',
                              year=year)
        self.date.grid(row=1, column=5)

        paid = tk.Label(label1, bg=self.color, text="Payment: ", font=font, height=2)
        paid.grid(row=1, column=6, padx=(10, 0))

        self.payment = Combobox(label1, width=13, state="readonly", font=font_small)
        self.payment.bind("<<ComboboxSelected>>", lambda e: label1.focus())
        self.payment['values'] = ("cash", "bank transfer")
        self.payment.current(1)
        self.payment.grid(row=1, column=7)

        # Second row - contractor data
        label2 = tk.Label(self.window, bg=self.color)
        label2.pack(side=tk.TOP, anchor='w')

        name = tk.Label(label2, bg=self.color, text="Contractor name: ", font=font, height=1, padx=4)
        name.grid(row=1, column=1)

        contractor_name = tk.Text(label2, bg="lightgrey", font=font_small, width=20, height=1)
        contractor_name.insert(1.0, self.selected[1])
        contractor_name.configure(state='disabled')
        contractor_name.grid(row=1, column=2)

        nip = tk.Label(label2, bg=self.color, text="NIP: ", font=font, height=1)
        nip.grid(row=1, column=3, padx=(10, 0))

        contractor_nip = tk.Text(label2, bg="lightgrey", font=font_small, width=12, height=1)
        contractor_nip.insert(1.0, self.selected[5])
        contractor_nip.configure(state='disabled')
        contractor_nip.grid(row=1, column=4)

        # Third row - buttons
        label3 = tk.Label(self.window, bg=self.color)
        label3.pack(side=tk.TOP, anchor='w', pady=(15, 0))

        add_product = tk.Button(label3, text="Add product", height=1, width=15,
                                command=lambda: SelectProductWindow(self.window, self.prod_list))
        add_product.grid(row=1, column=1, padx=(0, 6))

        self.delete_product = tk.Button(label3, text="Delete product", height=1, width=15,
                                        command=self.delete_from_treeview)
        self.delete_product['state'] = DISABLED
        self.delete_product.grid(row=1, column=2)

        # Fourth row - list of products on invoice
        self.create_products_list()

        # Fifth row - more buttons
        label5 = tk.Label(self.window, bg=self.color)
        label5.pack(side=tk.TOP, anchor='w')

        save = tk.Button(label5, text="Save", height=1, width=15, command=self.add_invoice)
        save.grid(row=1, column=1, padx=(0, 6))

        self.cancel = tk.Button(label5, text="Cancel", height=1, width=15, command=self.clean_window)
        self.cancel.grid(row=1, column=2)
