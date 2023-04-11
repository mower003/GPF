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
        #Status should be 0 for unpaid, 1 for paid
        sql_statement = """ CREATE TABLE IF NOT EXISTS invoice (
                                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                creation_date TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now', 'localtime')) NOT NULL,
                                                delivery_date TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now', 'localtime')) NOT NULL,
                                                note TEXT,
                                                issuer_id INTEGER DEFAULT 37,
                                                buyer_id INTEGER NOT NULL,
                                                status INTEGER NOT NULL,
                                                discount_amount NOT NULL,
                                                subtotal REAL NOT NULL,
                                                tax_total REAL,
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

                
    def update_invoice(self, invoiceList=None):
        self.create_connection()
        sql_statement = """ UPDATE invoice SET creation_date = ?, delivery_date = ?, note = ?, issuer_id = ?, buyer_id = ?, status = ?, discount_rate = ?, subtotal = ?, tax_total = ?, credit_invoice_num = ?
                                WHERE id = ? """
        cur = self.conn.cursor()
        cur.execute(sql_statement, invoiceList)
        self.conn.commit()
        

    def next_invoice_number(self):
        try:
            self.create_connection()
            sql_statement = """ SELECT MAX(id) FROM invoice """
            cur = self.conn.cursor()
            cur.execute(sql_statement)
            row = cur.fetchone()

            return row
        except Error as e:
            print(e)

    def get_invoice_by_invoice_id(self, invoice_id=None):
        self.create_connection()
        sql_statement = """ SELECT * FROM invoice where id = ?"""
        cur = self.conn.cursor()
        cur.execute(sql_statement, [invoice_id])
        row = cur.fetchone()

        return row

    def get_invoice_by_customer_id(self, customer_id):
        if customer_id is None:
            print("Error, no customer name supplied")
        else:
            try:
                self.create_connection()
                customer_id_as_list = [customer_id]
                sql_statement = """ SELECT * FROM invoice where id = ?"""
                cur = self.conn.cursor()
                cur.execute(sql_statement, customer_id_as_list)
                row = cur.fetchall()

                return row
            except Error as e:
                print(e)

    def get_invoices_by_search_params(self, selected_cust, start_date, end_date, invoice_status):
        self.create_connection()
        sql_statement = """ SELECT * FROM invoice WHERE buyer_id = ? AND (creation_date BETWEEN ? AND ?) AND status = ?"""
        cur = self.conn.cursor()
        cur.execute(sql_statement, [selected_cust, start_date, end_date, invoice_status])
        rows = cur.fetchall()

        return rows
    
    def get_recent_invoices(self, todaysDate):
        self.create_connection()
        sql_statement = """ SELECT * FROM invoice WHERE creation_date <= ? LIMIT 50 """
        cur = self.conn.cursor()
        cur.execute(sql_statement, [todaysDate])
        rows = cur.fetchall()

        return rows
    
    def update_paid_status(self, invoice_number, paid_status):
        self.create_connection()
        sql_statement = """ UPDATE invoice SET status = ? WHERE id = ? """
        #print("updating" + str(invoice_number) + str(paid_status))
        cur = self.conn.cursor()
        cur.execute(sql_statement, [paid_status, invoice_number])
        self.conn.commit()