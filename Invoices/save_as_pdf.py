from tkinter import filedialog
import os

from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet

from Database.db import Database

db = Database('Database/Database.db')


class PDF:
    def __init__(self):
        selected_folder = filedialog.askdirectory()
        last = db.get_last_invoice()
        file_name = selected_folder+"/Invoice_"+str(last[0])+".pdf"

        company = db.get_company()[0]
        last = db.get_last_invoice()
        contractor = db.get_contractor(last[5])
        products = db.fetch_invoice_products(last[0])

        c = canvas.Canvas(file_name, pagesize=A4)
        c.setFont("Helvetica", 10)
        width, height = A4

        # Image and date and no
        c.drawImage('Media/soy.jpg', 50, height - 135, mask="auto", height=50, width=50)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(420, height - 85, "Invoice number:")
        c.setFont("Helvetica", 10)
        c.drawString(420, height - 100, str(last[0]) + '/' + last[4])
        c.drawString(420, height - 140, last[2])
        c.setFont("Helvetica-Bold", 10)
        c.drawString(420, height - 125, "Issue date:")

        # company info
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, height - 185, "Seller:")
        c.setFont("Helvetica", 10)
        c.drawString(50, height - 200, company[1])
        c.drawString(50, height - 215, company[2])
        c.drawString(50, height - 230, company[3] + " " + company[4])
        c.drawString(50, height - 245, "NIP: " + " " + company[5])
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, height - 260, "Bank account number:")
        c.setFont("Helvetica", 10)
        c.drawString(50, height - 275, company[6])

        # contractor
        c.setFont("Helvetica-Bold", 12)
        c.drawString(420, height - 185, "Customer:")
        c.setFont("Helvetica", 10)
        c.drawString(420, height - 200, contractor[1])
        c.drawString(420, height - 215, contractor[2])
        c.drawString(420, height - 230, contractor[3] + " " + contractor[4])
        c.drawString(420, height - 245, "NIP: " + " " + contractor[5])

        # payment
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, height - 310, "Payment type:")
        c.setFont("Helvetica", 10)
        c.drawString(50, height - 325, last[3])

        minus = 400

        data = []

        data.append(['ID', 'Product name', 'Quantity', 'Unit', 'Netto price', 'VAT', 'Brutto price'])
        netto = 0
        brutto = 0
        for id, p in enumerate(products):
            data.append([str(id + 1), p[1], p[2], p[3], p[4], p[5], p[6]])
            netto += float(p[4])
            brutto += float(p[6])
            minus += 17

        t = Table(data, [20, 170, 70, 40, 80, 40, 80])
        t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
                               ('ALIGN', (2, 0), (-1, -1), 'RIGHT')]))
        w, h = t.wrap(width, height)
        t.drawOn(c, 50, (height - minus))

        height -= minus

        c.setFont("Helvetica-Bold", 10)
        c.drawString(450, height - 30, "Netto value: " + str(netto))
        c.drawString(450, height - 50, "Brutto value: " + str(brutto))

        c.drawString(50, height - 150, "......................................")
        c.drawString(420, height - 150, "......................................")
        c.drawString(60, height - 170, "Seller's Signature")
        c.drawString(421, height - 170, "Customer's Signature")




        # zapis do pliku
        c.showPage()
        c.save()
        import subprocess
        subprocess.Popen([file_name], shell=True)