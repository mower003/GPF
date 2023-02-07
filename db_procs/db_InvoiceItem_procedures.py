import sqlite3
from contextlib import closing
from sqlite3 import Error

class db_InvoiceItem_procedures:
    
    def __init__(self, db_location):
        self.db_location = db_location
        self.conn = None
        print(self.db_location)

    def create_base_table(self):
        self.create_connection()
        sql_statement = """ CREATE TABLE IF NOT EXISTS invoice_item (
                                                id INTEGER NOT NULL,
                                                invoice_id INTEGER NOT NULL,
                                                product_id INTEGER NOT NULL,
                                                case_quantity TEXT NOT NULL,
                                                quantity REAL NOT NULL,
                                                unit_price REAL NOT NULL,
                                                tax_rate REAL DEFAULT 0.0,
                                                tax_amount REAL DEFAULT 0.0,
                                                PRIMARY KEY (id, invoice_id),
                                                FOREIGN KEY (invoice_id)
                                                    REFERENCES invoice (id)
                                                FOREIGN KEY (product_id)
                                                    REFERENCES product (id)
                                                );"""
        cur = self.conn.cursor()
        cur.execute(sql_statement)
        self.conn.commit()
        self.close_connection()

    def create_connection(self):
        try:
            if self.conn == None:
                self.conn = sqlite3.connect(self.db_location)
        except Error as e:
            print(e)

    def close_connection(self):
        try:
            self.conn.close()
        except Error as e:
            print(e)

    def insert_invoice_item(self, id, invoice_id, product_id, case_quantity, quantity, unit_price, tax_rate, tax_amount):
        try:
            self.create_connection()
            sql_statement = """ INSERT INTO invoice_item (id, invoice_id, product_id, case_quantity, quantity, unit_price, tax_rate, tax_amount) VALUES (?,?,?,?,?,?,?,?)"""
            params = [id, invoice_id, product_id, case_quantity, quantity, unit_price, tax_rate, tax_amount]
            cur = self.conn.cursor()
            cur.execute(sql_statement, params)
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()
