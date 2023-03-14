from asyncio.windows_events import NULL
import sqlite3
from datetime import datetime
from Invoice import InvoiceObj as InvObj
from Entity import EntityObj as EntObj
from Product import ProductObj as ProdObj


from db_procs.db_Address_procedures import db_Address_procedures as db_conn_address
from db_procs.db_Country_procedures import db_Country_procedures as db_conn_country
from db_procs.db_Entity_procedures import db_Entity_procedures as db_conn_entity
from db_procs.db_EntityAddress_procedures import db_EntityAddress_procedures as db_conn_entityAddress
from db_procs.db_InvoiceStatus_procedures import db_InvoiceStatus_procedures as db_conn_invoiceStatus
from db_procs.db_InvoiceItem_procedures import db_InvoiceItem_procedures as db_conn_invoiceItem
from db_procs.db_Invoice_procedures import db_Invoice_procedures as db_conn_invoice
from db_procs.db_Product_procedures import db_Product_procedures as db_conn_product


from contextlib import closing
from sqlite3 import Error

#Connect to DB from command line use below from C:\Users\User\Desktop\GPF_Project\GPF\database\sqlite> directory
#sqlite3 c:\Users\User\Desktop\GPF_Project\GPF\database\sqlite\db\gpfdb.db

##C:\Users\dunju\Documents\GPF\database\sqlite
#sqlite3 C:\Users\dunju\Documents\GPF\database\sqlite\db\gpfdb.db

class GPFISCoordinator:

    def __init__(self):
        self.db_location = r"GPF\database\sqlite\db\gpfdb.db"
        self.db_location = r"C:\Users\dunju\Documents\GPF\database\sqlite\db\gpfdb.db"
        #print(self.db_location)

    def create_database_tables(self):
        #a = db_conn_address(self.db_location)
        #a.create_base_table()

        c = db_conn_country(self.db_location)
        c.create_base_table()

        e = db_conn_entity(self.db_location)
        e.create_base_table()

        #ea = db_conn_entityAddress(self.db_location)
        #ea.create_base_table()

        invS = db_conn_invoiceStatus(self.db_location)
        invS.create_base_table()

        ii = db_conn_invoiceItem(self.db_location)
        ii.create_base_table()

        i = db_conn_invoice(self.db_location)
        i.create_base_table()

        p = db_conn_product(self.db_location)
        p.create_base_table()

    def insert_country(self, country_code, country_name):
        c = db_conn_country(self.db_location)
        c.insert_country(country_code, country_name)

    def add_invoice(self, *, InvoiceObj=None):
        #Pre: Parameters an object of the Invoice class.
        #This method will need to handle adding all data that comes from the Invoice UI and insert it into invoice table.
        #Validation that data meets required insertion specifications based on the table should be done here too.
        try:
            if isinstance(InvoiceObj, InvObj):
                invoice_conn = db_conn_invoice(self.db_location)
                #Calculate totals should always be called before this object is ever passed in here but below is to make sure it happens.
                #InvoiceObj.calculate_invoice_subtotal()
                #InvoiceObj.calculate_invoice_total()

                invoice_conn.insert_invoice(InvoiceObj.asListForDBInsertion())
                print("The following InvoiceObj from GPFISCoordinator -> add_invoice() inserted into DB: ", InvoiceObj.asListForDBInsertion())

            else:
                print("InvoiceObj inside GPFISCoordinator.py -> add_invoice() is not an instance of InvObj!")
        except Error as e:
            print(e)
        finally:
            invoice_conn.close_connection()

    def insert_invoice_items(self, *, InvoiceObj=None):
        try:
            if isinstance(InvoiceObj, InvObj):
                invoice_item_conn = db_conn_invoiceItem(self.db_location)
                inv_item_list = InvoiceObj.getInvoiceItemList()

                for lines in inv_item_list:
                    #print(lines.asListForDBInsertion())
                    invoice_item_conn.insert_invoice_item(lines.asListForDBInsertion())
                    print("The following InvoiceItemObj from GPFISCoordinator -> insert_invoice_items() inserted into DB: ", lines.asListForDBInsertion())
            else:
                print("InvoiceObj inside GPFISCoordinator.py -> insert_invoice_items() is not an instance of InvObj!")
        except Error as e:
            print(e)
        finally:
            invoice_item_conn.close_connection()

    def get_next_invoice(self):
        invoice_conn = db_conn_invoice(self.db_location)
        next_inv_num = invoice_conn.next_invoice_number()
        next_inv_num = int(next_inv_num[0]) + 1
        return next_inv_num

    def view_invoice(self):
        print("todo")

    def modify_invoice(self):
        print("todo")

    def search_invoice_by_number(self):
        print("todo")

    def get_entities(self):
        entity_conn = db_conn_entity(self.db_location)
        entityObjList = []
        entityList = entity_conn.get_entities()
        print(entityList)
        for entity in entityList:
            eo = EntObj()
            eo.addEntityAsTuple(entity)
            entityObjList.append(eo)

        return entityObjList

    def insert_entity(self, * ,EntityObj=None):
        entity_conn = db_conn_entity(self.db_location)
        print("From inside insert entity ",EntityObj.asListForDBInsertion())
        if isinstance(EntityObj, EntObj):
            entity_conn.insert_entity_full(EntityObj.asListForDBInsertion())
        else:
            err_msg = "EntityObj inside GPFISCoordinator.py -> insert_entity() is not an instance of EntObj!"
            print(err_msg)

#*************************************************************
############################## Product #######################
#*************************************************************

    def insert_product(self, * ,ProductObj=None):
        product_conn = db_conn_product(self.db_location)
        print("From inside insert_product ",ProductObj.asListForDBInsertion())
        if isinstance(ProductObj, ProdObj):
            product_conn.insert_product(ProductObj.asListForDBInsertion())
            print("The following ProductObj from GPFISCoordinator -> insert_product() inserted into DB: ", repr(ProductObj))
        else:
            err_msg = "ProductObj inside GPFISCoordinator.py -> insert_product() is not an instance of ProdObj!"
            print(err_msg)

    def update_product(self, *, ProductObj=None):
        try:

            product_conn = db_conn_product(self.db_location)
            print("From inside update_product ",ProductObj.asListForDBUpdate())      
            if isinstance(ProductObj, ProdObj):
                product_conn.update_product(ProductObj.asListForDBUpdate())
                print("The following ProductObj from GPFISCoordinator -> update_product() updated in DB: ", repr(ProductObj))
            else:
                err_msg = "ProductObj inside GPFISCoordinator.py -> update_product() is not an instance of ProdObj!"
                print(err_msg)
        except Error as e:
            print(e)
        finally:
            product_conn.close_connection()

    def get_products(self):
        product_conn = db_conn_product(self.db_location)
        productObjList = []
        productList = product_conn.get_products()
        #print(productList)
        for product in productList:
            po = ProdObj(productList=product)
            #po.addProductAsList(productList=product)
            productObjList.append(po)

        return productObjList

    def get_product_by_id(self, product_id):
        try:
            product_conn = db_conn_product(self.db_location)
            product = product_conn.get_product_by_id(product_id)
            oProduct = ProdObj(productList= product)
            #print(product)
            return oProduct
        except Error as e:
            print(e)
        finally:
            product_conn.close_connection()

    def get_entity_id_by_name(self,current_customer):
        entity_conn = db_conn_entity(self.db_location)
        entityObjList = []
        entity = entity_conn.get_entity_by_name(current_customer)
        print(entity)
        return entity[0]

    def get_entities_simple(self):
        entity_conn = db_conn_entity(self.db_location)
        entityObjList = []
        entityList = entity_conn.get_all_entities_simple()
        print("FROM GPFISCoordinator:get_entities_simple()",entityList)

        for entities in entityList:
            entityObj = EntObj()
            entityObj.addEntityAsTuple(entities)
            entityObjList.append(entityObj)

        print(entityObjList)
        return entityObjList
            #entity_id = entities[0]
            #entity_name = entities[1]
            #entity_address = entities[2] + " " + entities[3] + " " + entities[4] + " " + entities[5] + " " + entities[6] + " " + entities[7]






#db1 = GPFISCoordinator()

#t = datetime.now()
# dd/mm/YY H:M:S
#dt_string = t.strftime("%Y-%m-%d %H:%M:%S")
#invObj = InvObj(creation_date= dt_string, delivery_date=dt_string, buyer_id=62, note='I am now created correctly')
#invObj.addInvoiceItem(4, 12, 24, 2.56)
#invObj.addInvoiceItem(4, 13, 25, 2.57)
#invObj.addInvoiceItem(4, 14, 26, 2.58)

#prodObj = ProdObj(23, 'Tokyo Negi 23', '23 Jumbo Tokyo Negi, packed 24 to a box.', 2.50, '24 per case 23')

#db1.insert_product(ProductObj=prodObj)
#prodsfromdb = db1.get_products()
#for prods in prodsfromdb:
#    print(prods.toString())

#db1.add_invoice()
#db1.create_database_tables()
#db1.insert_country("US", "United States of America")