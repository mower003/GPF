import sqlite3
from contextlib import closing
from sqlite3 import Error

class db_EntityAddress_procedures:
    
    def __init__(self, db_location):
        self.db_location = db_location
        self.conn = None
        print(self.db_location)

    def create_base_table(self):
        self.create_connection()
        sql_statement = """ CREATE TABLE IF NOT EXISTS entity_address (
                                                entity_id INTEGER PRIMARY KEY NOT NULL,
                                                address_id TEXT NOT NULL,
                                                FOREIGN KEY (entity_id)
                                                    REFERENCES entity (id)
                                                FOREIGN KEY (address_id)
                                                    REFERENCES address (address_id)
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