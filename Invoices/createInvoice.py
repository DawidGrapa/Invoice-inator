from tkinter import messagebox

from Database.db import Database
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkcalendar import DateEntry
import datetime
from Invoices.selectProduct import SelectProductWindow
from Invoices.save_as_pdf import PDF
from tkinter.font import Font
from Validators.validators import validate_invoice_no

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
        self.selected_product = None
        self.cancel = None
        self.delete_product = None
        self.invoice_no_pattern = None
        self.invoice_no_input = None
        self.settings = db.get_settings()
        self.create_invoice_window()

    def insert_pattern(self):
        today = datetime.date.today()
        res = self.settings[1]
        year = today.strftime("/%Y")
        month = today.strftime("/%m")
        day = today.strftime("%m/%d/%y")

        if res == "InvoiceNo/Month":
            self.invoice_no_pattern.insert(1.0, month)
        elif res == "InvoiceNo/Month/Year":
            self.invoice_no_pattern.insert(1.0, month + year)
        elif res == "InvoiceNo/Year":
            self.invoice_no_pattern.insert(1.0, year)

    def clean_window(self):
        for widget in self.top.frame2.winfo_children():
            widget.destroy()
            self.top.createInvoice_button['state'] = NORMAL
            self.top.company_button['state'] = NORMAL

    def delete_from_treeview(self):
        x = self.prod_list.selection()[0]
        self.prod_list.delete(x)
        self.delete_product['state'] = DISABLED

    def save_as_pdf(self):
        PDF()
        self.clean_window()

    def add_invoice(self):
        if validate_invoice_no(self.invoice_no_input.get()) is False:
            messagebox.showinfo(title="Error!", message="Wrong invoice number!")

        elif len(db.check_id(self.invoice_no_input.get())):
            messagebox.showinfo(title="Error!", message="Invoice with this number exists!")

        elif len(self.prod_list.get_children()) == 0:
            messagebox.showinfo(title="Error!", message="Add some products!")

        elif self.prod_list.get_children() and not len(db.check_id(self.invoice_no_input.get())):
            db.add_invoice(self.invoice_no_input.get(), self.selected[1], self.date.get(), self.payment.get(),
                           str(self.invoice_no_pattern.get(1.0, "end-1c")), self.selected[0])
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

    def create_invoice_window(self):
        self.contractors_window.destroy()
        bg = "#f8deb4"

        font = Font(family="Bookman Old Style", size=16)
        font_small = Font(family="Bookman Old Style", size=12)
        # First row
        label1 = tk.Label(self.window, bg=bg)
        label1.pack(side=tk.TOP, anchor='w')

        invoice_no = tk.Label(label1, bg=bg, text="Invoice number: ", font=font, height=2, padx=5, pady=1)
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

        issue_date = tk.Label(label1, bg=bg, text="Issue date: ", font=font, height=2)
        issue_date.grid(row=1, column=4, padx=(10, 0))

        year = datetime.datetime.today().year
        self.date = DateEntry(label1, width=12, bg="darkblue", fg="white", font=font_small, date_pattern='dd/mm/y',
                              year=year)
        self.date.grid(row=1, column=5)

        paid = tk.Label(label1, bg=bg, text="Payment: ", font=font, height=2)
        paid.grid(row=1, column=6, padx=(10, 0))

        self.payment = Combobox(label1, width=13, state="readonly", font=font_small)
        self.payment.bind("<<ComboboxSelected>>", lambda e: label1.focus())
        self.payment['values'] = ("cash", "bank transfer")
        self.payment.current(1)
        self.payment.grid(row=1, column=7)

        # Second row
        label2 = tk.Label(self.window, bg="#f8deb4")
        label2.pack(side=tk.TOP, anchor='w')

        name = tk.Label(label2, bg=bg, text="Contractor name: ", font=font, height=1, padx=4)
        name.grid(row=1, column=1)

        contractor_name = tk.Text(label2, bg="lightgrey", font=font_small, width=20, height=1)
        contractor_name.insert(1.0, self.selected[1])
        contractor_name.configure(state='disabled')
        contractor_name.grid(row=1, column=2)

        nip = tk.Label(label2, bg=bg, text="NIP: ", font=font, height=1)
        nip.grid(row=1, column=3, padx=(10, 0))

        contractor_nip = tk.Text(label2, bg="lightgrey", font=font_small, width=12, height=1)
        contractor_nip.insert(1.0, self.selected[5])
        contractor_nip.configure(state='disabled')
        contractor_nip.grid(row=1, column=4)

        # Third row - buttons
        label3 = tk.Label(self.window, bg=bg)
        label3.pack(side=tk.TOP, anchor='w', pady=(15, 0))

        add_product = tk.Button(label3, text="Add product", height=1, width=15,
                                command=lambda: SelectProductWindow(self.window, self.prod_list))
        add_product.grid(row=1, column=1, padx=(0, 6))

        self.delete_product = tk.Button(label3, text="Delete product", height=1, width=15,
                                        command=self.delete_from_treeview)
        self.delete_product['state'] = DISABLED
        self.delete_product.grid(row=1, column=2)

        # Fourth row - products treeview
        label4 = tk.Label(self.window, bg=bg)
        label4.pack(side=tk.TOP, anchor='w')

        # trying to change colors...
        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Bookmark Old Style', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Bookmark Old Style', 13))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.prod_list = Treeview(label4, height=24, style="mystyle.Treeview")
        self.prod_list.tag_configure('odd', background='#E8E8E8')
        self.prod_list['columns'] = ("ID", "ProductName", 'Quantity', 'Unit', 'netto', 'VAT', 'brutto')
        self.prod_list.column("#0", width=0, stretch=NO)
        self.prod_list.column("ID", anchor=W, width=40)
        self.prod_list.column("ProductName", anchor=W, width=300)
        self.prod_list.column('Quantity', anchor=W, width=90)
        self.prod_list.column("Unit", anchor=W, width=65)
        self.prod_list.column("netto", anchor=W, width=95)
        self.prod_list.column("VAT", anchor=W, width=65)
        self.prod_list.column("brutto", anchor=W, width=95)

        self.prod_list.heading("ID", text="ID", anchor=W)
        self.prod_list.heading("ProductName", text="Product Name", anchor=W)
        self.prod_list.heading("Quantity", text="Quantity", anchor=W)
        self.prod_list.heading("Unit", text="Unit", anchor=W)
        self.prod_list.heading("netto", text="Netto", anchor=W)
        self.prod_list.heading("VAT", text="VAT", anchor=W)
        self.prod_list.heading("brutto", text="Brutto", anchor=W)

        self.prod_list.bind("<ButtonRelease-1>", self.select_item)

        self.prod_list.grid(row=1, column=1, pady=(1, 0))

        # Fifth row - more buttons
        label5 = tk.Label(self.window, bg="#f8deb4")
        label5.pack(side=tk.TOP, anchor='w')

        save = tk.Button(label5, text="Save", height=1, width=15, command=self.add_invoice)
        save.grid(row=1, column=1, padx=(0, 6))

        self.cancel = tk.Button(label5, text="Cancel", height=1, width=15, command=self.clean_window)
        self.cancel.grid(row=1, column=2)
