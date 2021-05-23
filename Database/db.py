import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS contractors (id INTEGER PRIMARY  KEY, name text, street text, zip text, "
            "city text, nip text, description text)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, productname text, unit text, vat int, "
            "price float )")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS company (id INTEGER PRIMARY KEY, companyname text, street text, zip text, "
            "city text, nip text, account_number text)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS invoices (id INTEGER PRIMARY  KEY, invoice_id integer, companyname text, date text, payment text, format text, company_id integer)"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS invoice_products (invoice_id INTEGER, product_name text, quantity text, unit text, netto text, vat text, brutto text, unit_price text)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS settings (id INTEGER PRIMARY KEY, format text)"
        )
        self.conn.commit()


    # About contractors
    def fetch_contractors(self):
        self.cur.execute("SELECT * from contractors")
        rows = self.cur.fetchall()
        return rows

    def insert_contractor(self, name, street, zip, city, nip, description):
        self.cur.execute("INSERT INTO contractors VALUES (NULL,?,?,?,?,?,?)",
                         (name, street, zip, city, nip, description))
        self.conn.commit()

    def remove_contractor(self, id):
        self.cur.execute("DELETE FROM contractors WHERE id=?", (id,))
        self.conn.commit()

    def update_contractor(self, id, name, street, zip, city, nip, description):
        self.cur.execute("UPDATE contractors SET name=?,street=?,zip=?,city=?,nip=?,description=? WHERE id=?",
                         (name, street, zip, city, nip, description, id))
        self.conn.commit()

    def get_contractor(self, id):
        self.cur.execute("SELECT * from contractors where id=?", (id,))
        result = self.cur.fetchone()
        return result

    # About products
    def fetch_products(self):
        self.cur.execute("SELECT * from products")
        rows = self.cur.fetchall()
        return rows

    def get_product(self, id):
        self.cur.execute("SELECT * FROM products WHERE id = ?", (id,))
        result = self.cur.fetchone()
        return result

    def insert_product(self, productname, unit, vat, price):
        self.cur.execute("INSERT INTO products VALUES (NULL, ?,?,?,?)", (productname, unit, vat, price))
        self.conn.commit()

    def remove_product(self, id):
        self.cur.execute("DELETE FROM products WHERE id=?", (id,))
        self.conn.commit()

    def update_product(self, id, name, unit, vat, price):
        self.cur.execute("UPDATE products SET productname=?, unit=?, vat=?, price=? WHERE id=?",
                         (name, unit, vat, price, id))
        self.conn.commit()

    # about own company
    def get_company(self):
        self.cur.execute("SELECT * from company")
        rows = self.cur.fetchall()
        return rows

    def add_company(self, company, street, zip, city, nip, bank):
        self.cur.execute("INSERT INTO company VALUES (NULL, ?, ?, ?, ?, ?, ?)", (company, street, zip, city, nip, bank))
        self.conn.commit()

    def update_company(self, id, company, street, zip, city, nip, bank):
        self.cur.execute(
            "UPDATE company SET companyname=?, street=?, zip=?, city=?, nip=?, account_number=? WHERE id=?",
            (company, street, zip, city, nip, bank, id))
        self.conn.commit()

    def remove_company(self, id):
        self.cur.execute("DELETE FROM company WHERE id=?", (id,))
        self.conn.commit()

    #settings
    def add_settings(self, format):
        self.cur.execute("INSERT INTO settings VALUES (NULL, ?)", (format,))
        self.conn.commit()

    def update_settings(self,id , format):
        self.cur.execute(
            "UPDATE settings SET format=? WHERE id=?", (format, id,)
        )
        self.conn.commit()

    def get_settings(self):
        self.cur.execute("SELECT * from settings")
        row = self.cur.fetchone()
        return row

    # invoices
    def add_invoice(self, invoice_id, name, date, payment, format, company_id):
        self.cur.execute("INSERT INTO invoices VALUES (NULL,?, ?, ?, ?, ?, ?)", (invoice_id ,name, date, payment, format, company_id))
        self.conn.commit()

    def get_last_invoice(self):
        self.cur.execute("SELECT * FROM invoices ORDER BY id DESC LIMIT 1")
        result = self.cur.fetchone()
        if result:
            return result
        else:
            return [0,0]

    def add_invoice_product(self, invoice_id, product_name, quantity, unit, netto, vat, brutto, unit_price):
        self.cur.execute("INSERT INTO invoice_products VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                         (invoice_id, product_name, quantity, unit, netto, vat, brutto, unit_price))
        self.conn.commit()

    def check_id(self, id):
        self.cur.execute("SELECT invoice_id from invoices where invoice_id = ?", (id,))
        rows = self.cur.fetchall()
        return rows

    def fetch_invoices(self):
        self.cur.execute("SELECT * from invoices")
        rows = self.cur.fetchall()
        rows.sort(key=lambda x: x[0], reverse=1)
        return rows

    def remove_invoice(self, id):
        self.cur.execute("DELETE FROM invoices WHERE invoice_id=?", (id,))
        self.cur.execute("DELETE FROM invoice_products WHERE invoice_id=?", (id,))
        self.conn.commit()

    def fetch_invoice_products(self, id):
        self.cur.execute("SELECT * from invoice_products WHERE invoice_id=?", (id,))
        rows = self.cur.fetchall()
        return rows
