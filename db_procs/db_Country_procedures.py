import sqlite3
from contextlib import closing
from sqlite3 import Error

class db_Country_procedures:
    
    def __init__(self, db_location):
        self.db_location = db_location
        self.conn = None
        #print(self.db_location)

    def create_base_table(self):
        self.create_connection()
        sql_statement = """ CREATE TABLE IF NOT EXISTS country (
                                                country_code TEXT PRIMARY KEY NOT NULL,
                                                full_name TEXT NOT NULL
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

    def insert_country(self, country_code, full_name):
        try:
            self.create_connection()
            sql_statement = """ INSERT INTO country (country_code, full_name) VALUES (?,?)"""
            params = [country_code, full_name]
            cur = self.conn.cursor()
            cur.execute(sql_statement, params)
            self.conn.commit()
            self.close_connection()
        except Error as e:
            print(e)