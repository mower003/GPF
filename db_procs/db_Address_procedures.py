import sqlite3
from contextlib import closing
from sqlite3 import Error

class db_Address_procedures:
    
    def __init__(self, db_location):
        self.db_location = db_location
        self.conn = None
        #print(self.db_location)

    def create_base_table(self):
        self.create_connection()
        sql_statement = """ CREATE TABLE IF NOT EXISTS address (
                                                street_name TEXT NOT NULL,
                                                street_number TEXT,
                                                city TEXT,
                                                zip TEXT,
                                                country TEXT,
                                                FOREIGN KEY (country)
                                                    REFERENCES country (code)
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

    def insert_address(self, id, street_name, street_number, city, zip, country):
        try:
            self.create_connection()
            sql_statement = """ INSERT INTO address (id, street_name, street_number, city, zip, country) VALUES (?,?,?,?,?,?)"""
            params = [id, street_name, street_number, city, zip, country]
            cur = self.conn.cursor()
            cur.execute(sql_statement, params)
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()