import sqlite3
from contextlib import closing
from sqlite3 import Error

class db_Entity_procedures:
    
    def __init__(self, db_location):
        self.db_location = db_location
        self.conn = None
        print(self.db_location)

    def create_base_table(self):
        self.create_connection()
        sql_statement = """ CREATE TABLE IF NOT EXISTS entity (
                                                id INTEGER PRIMARY KEY NOT NULL,
                                                name TEXT NOT NULL,
                                                is_active INTEGER NOT NULL,
                                                street_name TEXT,
                                                street_number TEXT,
                                                city TEXT,
                                                state TEXT,
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

    def insert_entity_simple(self, id, name, is_active=1):
        try:
            self.create_connection()
            sql_statement = """ INSERT INTO entity (id, name, is_active) VALUES (?,?,?) """
            params = [id, name, is_active]
            cur = self.conn.cursor()
            cur.execute(sql_statement, params)
            self.conn.commit()

            return cur.lastrowid
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def insert_entity_full(self, entityParamList=None):
        try:
            self.create_connection()
            sql_statement = """ INSERT INTO entity (id, name, is_active, street_name, street_number, city, state, zip, country) VALUES (?,?,?,?,?,?,?,?,?) """
            cur = self.conn.cursor()
            cur.execute(sql_statement, entityParamList)
            self.conn.commit()

            return cur.lastrowid
        except Error as e:
            print(e)
        finally:
            self.close_connection()
    
    def edit_customer(self, customer):
        sql_statement = """ UPDATE entity SET 
        id = ?, 
        name = ?, 
        is_active = ? """

        cur = self.conn.cursor()
        cur.execute(sql_statement, customer)
        self.conn.commit()
    
    def get_entities(self):
        try:
            self.create_connection()
            sql_statement = """ SELECT * FROM entity """
            cur = self.conn.cursor()
            cur.execute(sql_statement)
            rows = cur.fetchall()

            return rows
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def get_entity_names(self):
        try:
            self.create_connection()
            sql_statement = """ SELECT name FROM entity """
            cur = self.conn.cursor()
            cur.row_factory = lambda cursor, row: row[0]
            cur.execute(sql_statement)
            rows = cur.fetchall()
            cur.row_factory = None

            return rows
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def get_entity_by_id(self, id):
        try:
            self.create_connection()
            sql_statement = """ SELECT * FROM entity where id = ? """
            cur = self.conn.cursor()
            cur.row_factory = lambda cursor, row: row[0]
            cur.execute(sql_statement, [id])
            rows = cur.fetchall()
            cur.row_factory = None

            return rows
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def get_entity_by_name(self, name):
        try:
            self.create_connection()
            sql_statement = """ SELECT * FROM entity where name = ? """
            cur = self.conn.cursor()
            cur.row_factory = lambda cursor, row: row[0]
            cur.execute(sql_statement, [name])
            rows = cur.fetchall()
            cur.row_factory = None

            return rows
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def get_all_entities_simple(self):
        try:
            self.create_connection()
            sql_statement = """ SELECT id, name, street_name, street_number, city, state, zip, country, is_active FROM entity WHERE is_active = 1 """
            cur = self.conn.cursor()
            cur.execute(sql_statement)
            rows = cur.fetchall()

            return rows
        except Error as e:
            print(e)
        finally:
            self.close_connection()
    
    def delete_entity(self, cust_id):
        try:
            self.create_connection()
            sql_statement = """DELETE FROM entity WHERE id = ? """
            cur = self.conn.cursor()
            cur.execute(sql_statement, [cust_id])
            self.conn.commit()

            return True
        except Error as e:
            print(e)
        finally:
            self.close_connection()