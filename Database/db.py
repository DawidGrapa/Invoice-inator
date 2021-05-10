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
            "CREATE TABLE IF NOT EXISTS invoices (id INTEGER PRIMARY  KEY, companyname text, date text, payment text)"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS invoice_products (invoice_id INTEGER, product_name text, quantity text, unit text, price text, vat text)")
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

    # About products
    def fetch_products(self):
        self.cur.execute("SELECT * from products")
        rows = self.cur.fetchall()
        return rows

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

    # invoices
    def add_invoice(self, name, date, payment):
        self.cur.execute("INSERT INTO invoices VALUES (NULL, ?, ?, ?)", (name, date, payment))
        self.conn.commit()

    def get_last_invoice(self):
        self.cur.execute("SELECT * FROM invoices ORDER BY id DESC LIMIT 1")
        result = self.cur.fetchone()
        if result:
            return result
        else:
            return [0]

    def add_invoice_product(self, invoice_id, product_name, quantity, unit, price, vat):
        self.cur.execute("INSERT INTO invoice_products VALUES (?, ?, ?, ?, ?, ?)",
                         (invoice_id, product_name, quantity, unit, price, vat))
        self.conn.commit()
