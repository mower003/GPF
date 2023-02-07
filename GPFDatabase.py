import sqlite3
from sqlite3 import Error
class GPFDatabase:

    def __init__(self):
        self.conn = None
        self.db_location = r"database\sqlite\db\sqlitetest.db"
    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_location)
        except Error as e:
            print(e)

    def create_table(self, create_table_statement):
        try:
            c = self.conn.cursor()
            c.execute(create_table_statement)
        except Error as e:
            print(e)

    def execute_table_create(self):
        #db_location = r"database\sqlite\db\sqlitetest.db"

        db_create_customers_statement = """ CREATE TABLE IF NOT EXISTS customers (
                                                customer_id INTEGER PRIMARY KEY,
                                                customer_name TEXT NOT NULL,
                                                address TEXT NOT NULL,
                                                city TEXT,
                                                state TEXT,
                                                zip TEXT
                                                ); """
        #PLEASE REMEMBER TO CHANGE THE QUERIES TO ACCURATELY REFLECT THAT THIS TABLE IS NOW CALLED PRODUCTS!
        #NO LONGER VEGETABLE_ID, NO LONGER VEGETABLE_NAME.
        db_create_products_statement = """ CREATE TABLE IF NOT EXISTS products (
                                                product_id INTEGER PRIMARY KEY,
                                                product_name TEXT NOT NULL,
                                                description TEXT,
                                                product_price REAL
                                                ); """

        db_create_invoices_statement = """ CREATE TABLE IF NOT EXISTS invoices (
                                                invoice_num INTEGER PRIMARY KEY AUTOINCREMENT,
                                                discount REAL NOT NULL,
                                                date TEXT,
                                                customer_id INTEGER NOT NULL,
                                                FOREIGN KEY (customer_id)
                                                    REFERENCES customers (customer_id)
                                                ); """
        
        db_create_lineitems_statement = """ CREATE TABLE IF NOT EXISTS lineitems (
                                                line_id TEXT PRIMARY KEY,
                                                quantity INTEGER NOT NULL,
                                                cases TEXT NOT NULL,
                                                product_id INTEGER NOT NULL,
                                                description TEXT NOT NULL,
                                                price_per_qty REAL NOT NULL,
                                                invoice_num INTEGER NOT NULL,
                                                FOREIGN KEY (invoice_num)
                                                    REFERENCES invoices (invoice_num)
                                                ); """

        #conn = create_connection()

        if self.conn is not None:
            print("creating tables")
            self.create_table(db_create_customers_statement)
            self.create_table(db_create_invoices_statement)
            self.create_table(db_create_lineitems_statement)
            self.create_table(db_create_products_statement)
            self.conn.commit()
            #conn.close()

        else:
            print("Error establishing connection to database.")

    def insert_customer(self, customer):
        if self.conn is not None:
            sql_statement = """ INSERT INTO customers (customer_id,customer_name,address, city, state, zip) VALUES (?,?,?,?,?,?) """
            cur = self.conn.cursor()
            cur.execute(sql_statement, customer)
            self.conn.commit()
        else:
            print("Not connected to database!")

        return cur.lastrowid
    
    def edit_customer(self, customer):
        sql_statement = """ UPDATE customers SET 
        customer_name = ?, 
        address = ?, 
        city = ?, 
        state = ?, 
        zip = ?
        WHERE customer_id = ? """

        cur = self.conn.cursor()
        cur.execute(sql_statement, customer)
        self.conn.commit()
    
    def get_customers(self):
        sql_statement = """ SELECT * FROM customers """
        cur = self.conn.cursor()
        cur.execute(sql_statement)
        rows = cur.fetchall()

        return rows

    def get_customer_names(self):
        sql_statement = """ SELECT customer_name FROM customers """
        cur = self.conn.cursor()
        cur.row_factory = lambda cursor, row: row[0]
        cur.execute(sql_statement)
        rows = cur.fetchall()
        cur.row_factory = None

        return rows

    def delete_customer(self, cust_id):
        sql_statement = """DELETE FROM customers WHERE customer_id = ?"""
        cur = self.conn.cursor()
        cur.execute(sql_statement, cust_id)
        self.conn.commit()
    
    def get_products(self):
        sql_statement = """ SELECT * FROM products """
        cur = self.conn.cursor()
        cur.execute(sql_statement)
        rows = cur.fetchall()

        return rows

    def get_product_by_id(self, prod_id):
        sql_statement = """ SELECT * FROM products WHERE product_id = ? """
        cur = self.conn.cursor()
        cur.execute(sql_statement, prod_id)
        row = cur.fetchall()

        return row

    def insert_product(self, prod):
        sql_statement = """ INSERT INTO products (product_id, product_name, description, product_price) VALUES (?,?,?,?) """
        cur = self.conn.cursor()
        cur.execute(sql_statement, prod)
        self.conn.commit()

        return cur.lastrowid

    def edit_product(self, prod):
        sql_statement = """ UPDATE products SET 
        product_name = ?, 
        description = ?,
        product_price = ?
        WHERE product_id = ? """

        cur = self.conn.cursor()
        cur.execute(sql_statement, prod)
        self.conn.commit()


    def delete_product(self, prod_id):
        sql_statement = """DELETE FROM products WHERE product_id = ?"""
        cur = self.conn.cursor()
        cur.execute(sql_statement, prod_id)
        self.conn.commit()

    def insert_invoice(self, invoice):
        sql_statement = """ INSERT INTO invoices (discount, date, customer_id) VALUES (?,?,?) """
        cur = self.conn.cursor()
        cur.execute(sql_statement, invoice)
        self.conn.commit()

        return cur.lastrowid

    def get_invoice_by_custID(self, cust_id):
        sql_statement = """ SELECT * FROM invoices WHERE customer_id = ? """
        cur = self.conn.cursor()
        cur.execute(sql_statement, cust_id)
        rows = cur.fetchall()

        return rows

    def get_invoice_list(self):
        sql_statement = """ SELECT invoice_num FROM invoices """
        cur = self.conn.cursor()
        cur.row_factory = lambda cursor, row: row[0]
        cur.execute(sql_statement)
        rows = cur.fetchall()
        cur.row_factory = None

        return rows

    def get_invoice_by_invoicenum(self, inv_num):
        sql_statement = """ SELECT invoices.invoice_num, invoices.customer_id, date, discount,
        customers.customer_name, customers.address, customers.state, customers.city, customers.zip
        FROM invoices 
        INNER JOIN customers ON invoices.customer_id = customers.customer_id 
        WHERE invoices.invoice_num = ? """
        cur = self.conn.cursor()
        cur.execute(sql_statement, inv_num)
        rows = cur.fetchall()

        return rows

    def get_next_inv_num(self):
        sql_statement = """ SELECT MAX(invoice_num) FROM invoices """
        cur = self.conn.cursor()
        cur.execute(sql_statement)
        row = cur.fetchone()

        return row

    def insert_line_item(self, line_item):
        sql_statement = """ INSERT INTO lineitems (line_id, quantity, cases, product_id, description, price_per_qty, invoice_num ) VALUES (?,?,?,?,?,?,?) """
        cur = self.conn.cursor()
        cur.execute(sql_statement, line_item)
        self.conn.commit()

        return cur.lastrowid
    
    def get_line_items_by_invid(self, inv_id):
        sql_statement = """ SELECT * FROM lineitems WHERE invoice_num = ? """
        cur = self.conn.cursor()
        cur.execute(sql_statement, inv_id)
        rows = cur.fetchall()

        return rows
    
    def close_connection(self):
        if self.conn is not None:
            self.conn.close()