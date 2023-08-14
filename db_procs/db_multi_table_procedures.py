import sqlite3
from contextlib import closing
from sqlite3 import Error

class db_multi_table_procedures():

    def __init__(self, db_location):
        self.db_location = db_location
        self.conn = None
        #print(self.db_location)

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

# Query returns all invoice_item products from a date range.

#SELECT invoice.id, invoice.ship_date, invoice_item.product_id, invoice_item.case_quantity, invoice_item.quantity, invoice_item.unit_price, invoice_item.product_id, (invoice_item.quantity * invoice_item.unit_price) AS line_total 
#FROM invoice JOIN invoice_item 
#ON invoice.id = invoice_item.invoice_id 
#WHERE invoice.invoice_date BETWEEN '08-01-2023' AND '08-31-2023';


# Query that returns cumulative product quantity and dollars sold for a given date range for each unique product.

# SELECT invoice_item.product_id, SUM(invoice_item.quantity) AS product_qty_total, SUM(invoice_item.quantity * invoice_item.unit_price) AS product_dollar_total
# FROM invoice JOIN invoice_item
# ON invoice.id = invoice_item.invoice_id 
# WHERE invoice.invoice_date BETWEEN '08-01-2023' AND '08-31-2023' 
# GROUP BY invoice_item.product_id;
# ===== RETURNED =====
# product_id  product_qty_total  product_dollar_total
# ----------  -----------------  --------------------
# 1           1518617.41         1518717.41
# 2           24691.34           24691.34

    def get_product_breakdown_data(self, date_range):
        self.create_connection()
        sql_statement = """ SELECT invoice_item.product_id, SUM(invoice_item.quantity) AS product_qty_total, SUM(invoice_item.quantity * invoice_item.unit_price) AS product_dollar_total
                            FROM invoice JOIN invoice_item
                            ON invoice.id = invoice_item.invoice_id 
                            WHERE invoice.invoice_date BETWEEN ? AND ? 
                            GROUP BY invoice_item.product_id; """
        cur = self.conn.cursor()
        cur.execute(sql_statement, date_range)
        row = cur.fetchall()
        print("FROM DB",row)
        return row
    
    def get_product_breakdown_data_by_product_and_date_range(self, product_id, date_range):

        self.create_connection()
        sql_statement = """ SELECT invoice_item.product_id, SUM(invoice_item.quantity) AS product_qty_total, SUM(invoice_item.quantity * invoice_item.unit_price) AS product_dollar_total
                            FROM invoice JOIN invoice_item
                            ON invoice.id = invoice_item.invoice_id 
                            WHERE invoice.invoice_date BETWEEN ? AND ?
                            AND invoice_item.product_id = ?; """
        dbargs = date_range + [product_id]
        #print("DB ARGS ", dbargs)
        cur = self.conn.cursor()
        cur.execute(sql_statement, dbargs)
        row = cur.fetchall()
        #print("FROM DB",row)
        return row
