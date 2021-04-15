import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS contractors (id INTEGER PRIMARY  KEY, name text, street text, zip text, city text, nip text, description text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, productname text, unit text, vat int, price float )")
        self.conn.commit()

    #About contractors
    def fetch_contractors(self):
        self.cur.execute("SELECT * from contractors")
        rows = self.cur.fetchall()
        return rows

    def insert_contractor(self, name, street, zip, city, nip, description):
        self.cur.execute("INSERT INTO contractors VALUES (NULL,?,?,?,?,?,?)", (name, street, zip, city, nip, description))
        self.conn.commit()

    def remove_contractor(self, id):
        self.cur.execute("DELETE FROM contractors WHERE id=?", (id,))
        self.conn.commit()

    def update_contractor(self, id, name, street, zip, city, nip, description):
        self.cur.execute("UPDATE contractors SET name = ?,street=?,zip=?,city=?,nip=?,description=? WHERE id = ?",(name,street,zip,city,nip,description,id))
        self.conn.commit()
    #About products
    def fetch_products(self):
        self.cur.execute("SELECT * from products")
        rows = self.cur.fetchall()
        return rows
    def insert_product(self, productname,unit, vat, price):
        self.cur.execute("INSERT INTO products VALUES (NULL, ?,?,?,?)" ,(productname,unit,vat,price))
        self.conn.commit()
    def remove_product(self,id):
        self.cur.execute("DELETE FROM products WHERE id=?",(id,))
        self.conn.commit()
    def update_product(self,id):
        self.cur.execute("UPDATE products SET productname =?, unit = ?, vat = ?, price = ?")
        self.conn.commit()