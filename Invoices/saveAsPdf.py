import subprocess
from tkinter import filedialog

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas

from Database.db import Database
db = Database('Database/Database.db')


def PDF(id=None):
    company = db.get_company()
    if not id:
        last_invoice = db.get_last_invoice()
    else:
        last_invoice = db.get_invoice(id)
    # Invoice format
    invoice_id = str(last_invoice[1])
    issue_date = last_invoice[3]
    invoice_format = last_invoice[5]
    payment_type = last_invoice[4]
    # Contractor data
    contractor_name = last_invoice[2]
    contractor_street = last_invoice[6]
    contractor_zip = last_invoice[7]
    contractor_city = last_invoice[8]
    contractor_nip = last_invoice[9]

    # Company data
    company_name = company[1]
    company_street = company[2]
    company_zip = company[3]
    company_city = company[4]
    company_nip = company[5]
    company_bank = company[6]

    # Creating pdf file
    selected_folder = filedialog.askdirectory()
    file_name = selected_folder + "/Invoice_" + invoice_id + ".pdf"

    c = canvas.Canvas(file_name, pagesize=A4)
    c.setFont("Helvetica", 10)
    width, height = A4

    # Placing logo, invoice number and issue date
    c.drawImage('Media/soy_invoice.png', 50, height - 120, mask="auto", height=60, width=300)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(420, height - 85, "Invoice number:")
    c.setFont("Helvetica", 10)
    c.drawString(420, height - 100, invoice_id + invoice_format)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(420, height - 125, "Issue date:")
    c.setFont("Helvetica", 10)
    c.drawString(420, height - 140, issue_date)

    # Placing company's info
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 185, "Seller:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 200, company_name)
    c.drawString(50, height - 215, company_street)
    c.drawString(50, height - 230, company_zip + " " + company_city)
    c.drawString(50, height - 245, "NIP: " + " " + company_nip)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 260, "Bank account number:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 275, company_bank)

    # Placing contractor's info
    c.setFont("Helvetica-Bold", 12)
    c.drawString(420, height - 185, "Customer:")
    c.setFont("Helvetica", 10)
    c.drawString(420, height - 200, contractor_name)
    c.drawString(420, height - 215, contractor_street)
    c.drawString(420, height - 230, contractor_zip + " " + contractor_city)
    c.drawString(420, height - 245, "NIP: " + " " + contractor_nip)

    # Placing payment info
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 310, "Payment type:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 325, payment_type)

    # Placing products' data
    data = [['ID', 'Product name', 'Quantity', 'Unit', 'Unit value', 'Netto value', 'VAT [%]', 'Brutto value']]
    netto = 0
    brutto = 0
    gap = 400

    products = db.fetch_invoice_products(invoice_id)

    for idx, p in enumerate(products):
        data.append([str(idx+1), p[1], p[2], p[3], str('{:.2f}'.format(float(p[7]))), str('{:.2f}'.format(float(p[4]))),
                     p[5], str('{:.2f}'.format(float(p[6])))])
        netto += float(p[4])
        brutto += float(p[6])
        gap += 17

    t = Table(data, [20, 120, 60, 40, 67, 67, 56, 77])
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.25, colors.black),
                           ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                           ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
                           ('ALIGN', (2, 0), (-1, -1), 'RIGHT')]))
    t.wrap(width, height)
    t.drawOn(c, 50, (height - gap))

    # Placing total value and signatures
    height -= gap
    c.setFont("Helvetica-Bold", 10)
    c.drawString(450, height - 30, "Netto value:  " + str('{:.2f}'.format(netto)))
    c.drawString(450, height - 50, "Brutto value: " + str('{:.2f}'.format(brutto)))

    c.drawString(50, height - 150,  "......................................")
    c.drawString(420, height - 150, "......................................")
    c.drawString(60, height - 170, "Seller's Signature")
    c.drawString(421, height - 170, "Customer's Signature")

    # Saving file and opening it
    c.showPage()
    c.save()
    subprocess.Popen([file_name], shell=True)
