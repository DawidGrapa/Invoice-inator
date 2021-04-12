import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS contractors (id INTEGER PRIMARY  KEY, name text, street text, zip text, city text, nip text, description text)")
        self.conn.commit()

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

