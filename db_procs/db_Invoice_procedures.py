from asyncio.windows_events import NULL
import sqlite3
from contextlib import closing
from sqlite3 import Error

class db_Invoice_procedures:
    
    def __init__(self, db_location):
        self.db_location = db_location
        self.conn = None
        print(self.db_location)

    def create_base_table(self):
        self.create_connection()
        sql_statement = """ CREATE TABLE IF NOT EXISTS invoice (
                                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                creation_date TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now', 'localtime')) NOT NULL,
                                                delivery_date TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now', 'localtime')) NOT NULL,
                                                note TEXT,
                                                issuer_id INTEGER DEFAULT 37,
                                                buyer_id INTEGER NOT NULL,
                                                status INTEGER DEFAULT 1,
                                                discount_rate DEFAULT 0,
                                                subtotal REAL DEFAULT 0.00,
                                                tax_total REAL DEFAULT 0.00,
                                                credit_invoice_num INTEGER,
                                                FOREIGN KEY (issuer_id) REFERENCES entity (id)
                                                FOREIGN KEY (buyer_id) REFERENCES entity (id)
                                                FOREIGN KEY (status) REFERENCES invoice_status (id)
                                                ); """
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

    #In: invoiceParamList must be a properly ordered list in the order of the insert signature.
    
    def insert_invoice(self, invoiceParamList=None):
        if invoiceParamList is None:
            print("from insert_invoice: No invoice parameters supplied!")
        else:
            try:
                self.create_connection()
                sql_statement = """ INSERT INTO invoice (creation_date, delivery_date, note, issuer_id, buyer_id, status, discount_rate, subtotal, tax_total, credit_invoice_num)
                                VALUES (?,?,?,?,?,?,?,?,?,?)"""
                cur = self.conn.cursor()
                cur.execute(sql_statement, invoiceParamList)
                self.conn.commit()
            except Error as e:
                print(e)
            finally:
                self.close_connection()

    def get_invoice_by_invoice_id(self, invoice_id=None):
        if invoice_id is None:
            print("Error, no invoice id supplied")
        else:
            try:
                self.create_connection()
                invoice_id_as_list = [invoice_id]
                sql_statement = """ SELECT * FROM invoice where id = ?"""
                cur = self.conn.cursor()
                cur.execute(sql_statement, invoice_id_as_list)
                row = cur.fetchone()

                return row
            except Error as e:
                print(e)
            finally:
                self.close_connection()