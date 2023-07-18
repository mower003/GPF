import sqlite3
from contextlib import closing
from sqlite3 import Error

class db_Product_procedures:
    def __init__(self, db_location):
        self.db_location = db_location
        self.conn = None
        #print(self.db_location)

    def create_base_table(self):
        self.create_connection()
        sql_statement = """ CREATE TABLE IF NOT EXISTS product (
                                                id INTEGER PRIMARY KEY NOT NULL,
                                                name TEXT NOT NULL,
                                                description TEXT,
                                                unit_price REAL,
                                                case_style TEXT,
                                                note TEXT
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

    def insert_product(self, productParamList):
        if productParamList is None:
            print("from insert_product: No product parameters supplied!")
        else:
            try:
                #print("INSIDE DB INSERT: ", productParamList)
                self.create_connection()
                sql_statement = """ INSERT INTO product (id, name, description, unit_price, case_style, note) VALUES (?,?,?,?,?,?) """
                cur = self.conn.cursor()
                cur.execute(sql_statement, productParamList)
                self.conn.commit()
            except Error as e:
                print(e)
            finally:
                self.close_connection()

    def get_products(self):
        try:
            self.create_connection()
            sql_statement = """ SELECT id, name, description, unit_price, case_style, note FROM product; """
            cur = self.conn.cursor()
            cur.execute(sql_statement)
            rows = cur.fetchall()
            
            return rows
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def get_product_by_id(self, prod_id):
        self.create_connection()
        sql_statement = """ SELECT * FROM product WHERE id = ? """
        cur = self.conn.cursor()
        cur.execute(sql_statement, [prod_id])
        rows = cur.fetchall()
        
        return rows[0]

    def update_product(self, productObjAsList):
        self.create_connection()
        #print("INSIDE DB CONN UPDATE", productObjAsList)
        sql_statement = """ UPDATE product SET 
            name = ?, 
            description = ?,
            unit_price = ?,
            case_style = ?,
            note = ?
        WHERE id = ? """
        cur = self.conn.cursor()
        cur.execute(sql_statement, productObjAsList)
        self.conn.commit()


    def delete_product(self, prod_id):
        sql_statement = """DELETE FROM products WHERE id = ?"""
        cur = self.conn.cursor()
        cur.execute(sql_statement, prod_id)
        self.conn.commit()