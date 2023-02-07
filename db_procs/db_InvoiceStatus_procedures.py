from socket import create_connection
import sqlite3
from contextlib import closing
from sqlite3 import Error

class db_InvoiceStatus_procedures:
    
    def __init__(self, db_location):
        self.db_location = db_location
        self.conn = None
        print(self.db_location)

    def create_base_table(self):
        self.create_connection()
        sql_statement = """ CREATE TABLE IF NOT EXISTS invoice_status (
                                                id INTEGER PRIMARY KEY NOT NULL,
                                                description TEXT NOT NULL
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

    def create_status_entries(self):
        self.create_connection()
        sql_statement = """ INSERT INTO invoice_status (id, description) VALUES (1, 'Issued')"""
        cur = self.conn.cursor()
        cur.execute(sql_statement)
        self.conn.commit()
        sql_statement = """ INSERT INTO invoice_status (id, description) VALUES (2, 'Paid')"""
        cur = self.conn.cursor()
        cur.execute(sql_statement)
        self.conn.commit()
        sql_statement = """ INSERT INTO invoice_status (id, description) VALUES (3, 'Deleted')"""
        cur = self.conn.cursor()
        cur.execute(sql_statement)
        self.conn.commit()
        sql_statement = """ INSERT INTO invoice_status (id, description) VALUES (4, 'Credited')"""
        cur = self.conn.cursor()
        cur.execute(sql_statement)
        self.conn.commit()
        sql_statement = """ INSERT INTO invoice_status (id, description) VALUES (5, 'Voided')"""
        cur = self.conn.cursor()
        cur.execute(sql_statement)
        self.conn.commit()
        self.close_connection()