
import datetime
import os.path
from GPFISCoordinator import GPFISCoordinator
from webbrowser import open_new_tab

class GPFIS2HTML():

    document_location = r"C:\Users\dunju\Documents\GPF\GPFISHTMLObjects\Invoices"
    #css_path = 'GPFISHTMLObjects\css\gpf.css'
    css_path = "./css/gpf.css"
    logo_path = "./imgs/gpf_logo.png"

    def __init__(self, inv_num):
        self.entityObj = None
        self.invoiceObj = None
        self.coordinator = GPFISCoordinator()
        self.set_up_objects(inv_num)
        self.set_file_name()

    def set_up_objects(self, invoice_number):
        self.invoiceObj = self.coordinator.fetch_invoice_for_edit(invoice_number)
        self.fetch_entity(self.invoiceObj.get_buyer_id())

    def set_file_name(self):
        now = datetime.datetime.today().strftime("%Y%m%d-%H%M") 
        self.file_name = str(self.invoiceObj.get_inv_num()) + "_" + now + ".html"
        self.completeFileName = os.path.join(self.document_location, self.file_name)
        print(self.completeFileName)
        self.file_handle = open(self.completeFileName, 'w')

    def build_HTML_invoice(self):
        self.creater_header(self.invoiceObj.get_inv_num())
        self.create_GPF_logo_and_address()
        self.create_invoice_num(self.invoiceObj.get_inv_num())
        self.create_date(self.invoiceObj.get_creation_date())
        self.create_shipto(self.entityObj.getName(), self.entityObj.getStreetNumber(), self.entityObj.getStreetName(), self.entityObj.getCity(), self.entityObj.getState(), self.entityObj.getZip())
        self.create_static_item_table_info()

        for itemObjs in self.invoiceObj.invItemsObjList:
            self.create_line_item(itemObjs.asTupleForHTML())

        self.create_subtotal(self.invoiceObj.get_subtotal())
        self.create_discount(self.invoiceObj.get_discount_rate())
        self.create_total(self.invoiceObj.get_total())
        self.create_signature_line_and_close()
        self.file_handle.close()

        open_new_tab(self.completeFileName)

    def fetch_entity(self, entity_id):
        self.entityObj = self.coordinator.get_entity_by_id(entity_id)
        print("FROM GPFIS2HTML ENTITY", self.entityObj)

    def creater_header(self, inv_num):
        html_string = """<!DOCTYPE HTML>
        <html>
            <head>
                <title>Green Paradise Farms %s</title>
                <meta charset="utf-8" />
                <link rel="stylesheet" href="%s">
            </head>"""
        header = html_string % (inv_num, self.css_path)
        self.file_handle.write(header)
        
    def create_GPF_logo_and_address(self):
        html_string = """   <body>
        <div class = "wrapper">
            <div class = "logoandinfo">
                <img id="GPFLogo" src="%s">
                <p id="GPFAddressTitle">GREEN PARADISE FARM <br>2555 GUAJOME LAKE ROAD<br>VISTA, CALIFORNIA, 92084-1610<br>Tel: (760) 724-1123<br>Fax: (760) 724-5566</p>
            </div>"""
        logo_and_address = html_string % (self.logo_path)
        self.file_handle.write(logo_and_address)
        
    def create_invoice_num(self, inv_num):
        html_string = """<div class = "invoicenumber"><p>Invoice Number: </p> <p id="inv_num">%s</p></div>"""
        invoice_area = html_string % (inv_num)
        self.file_handle.write(invoice_area)

    def create_date(self, date):
        html_string = """<div class = "datefield"><p>Date: </p> <p id="datevalue">%s</p></div>"""
        date_area = html_string % (date)
        self.file_handle.write(date_area)

    def create_shipto(self, customer_name, street_num, street_name, city, state, zip):
        #customer name, address (street_num + street_name), city, state, zip
        html_string = """<div class = "shipto"><p>Ship to: </p> <p id = "storename" >%s<br> %s %s,<br> %s, %s, %s</p></div>"""
        shipto = html_string % (customer_name, street_num, street_name, city, state, zip)

        self.file_handle.write(shipto)

    def create_static_item_table_info(self):
        html_string = """<div class = "itemtable">
            <table id = "theitemtable">
                <tr id="headervalues">
                    <th>Qty (Lbs)</th>
                    <th>C/S</th>
                    <th>Item No.</th>
                    <th>Description</th>
                    <th>Note</th>
                    <th>Price</th>
                    <th>Total</th>
                </tr>"""
        self.file_handle.write(html_string)
        
    def create_line_item(self, lineItemTuple):
        #qty, cases, itemnum, description, note, price, total
        html_string = """<tr id="lineitem"><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>$%s</td><td>$%s</td></tr>"""
        line_item = html_string % lineItemTuple

        self.file_handle.write(line_item)

    def create_subtotal(self, subtotal):
        html_string = """<tr><td> </td> <td> </td> <td> </td> <td> </td> <td></td> <td>Subtotal: </td> <td>$%s</td></tr>"""
        subtotal = html_string % (subtotal)

        self.file_handle.write(subtotal)

    def create_discount(self, discount):
        html_string = """<tr><td> </td> <td> </td> <td> </td> <td> </td> <td></td> <td>Discount: </td> <td>$%s</td></tr>"""
        discount = html_string % (discount)

        self.file_handle.write(discount)

    def create_total(self, total):
        html_string = """<tr><td> </td> <td> </td> <td> </td> <td> </td> <td></td> <td>Total: </td> <td>$%s</td></tr></table></div>"""
        total = html_string % (total)

        self.file_handle.write(total)

    def create_signature_line_and_close(self):
        html_string = """<div class ="signatureline"><p>X___________________________________________________</p></div></div></body></html>"""

        self.file_handle.write(html_string)
