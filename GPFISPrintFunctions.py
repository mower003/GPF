
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
        self.shiptoObj = None
        self.billtoObj = None
        self.invoiceObj = None
        self.coordinator = GPFISCoordinator()
        self.set_up_objects(inv_num)
        self.set_file_name()

    def set_up_objects(self, invoice_number):
        self.invoiceObj = self.coordinator.fetch_invoice_for_edit(invoice_number)
        self.billtoObj = self.fetch_entity(self.invoiceObj.get_buyer_id())
        self.shiptoObj = self.fetch_entity(self.invoiceObj.get_ship_to_id())

    def set_file_name(self):
        now = datetime.datetime.today().strftime("%Y%m%d_%H%M") 
        self.file_name = str(self.invoiceObj.get_inv_num()) + "_" + now + ".html"
        self.completeFileName = os.path.join(self.document_location, self.file_name)
        print(self.completeFileName)
        self.file_handle = open(self.completeFileName, 'w')

    def build_HTML_invoice(self):
        self.creater_header(self.invoiceObj.get_inv_num())
        self.create_GPF_logo_and_address()
        self.create_invoice_num(self.invoiceObj.get_inv_num())
        self.create_date(self.invoiceObj.get_invoice_date())
        self.create_subheader(self.invoiceObj.get_payment_terms(), self.invoiceObj.get_due_date(), self.invoiceObj.get_po_number(), self.invoiceObj.get_applied_credit_amount(), '', self.invoiceObj.get_note())
        self.create_billto(self.billtoObj.getName(), self.billtoObj.getStreetNumber(), self.billtoObj.getStreetName(), self.billtoObj.getCity(), self.billtoObj.getState(), self.billtoObj.getZip())
        self.create_shipto(self.shiptoObj.getName(), self.shiptoObj.getStreetNumber(), self.shiptoObj.getStreetName(), self.shiptoObj.getCity(), self.shiptoObj.getState(), self.shiptoObj.getZip())
        self.create_static_item_table_info()

        for itemObjs in self.invoiceObj.invItemsObjList:
            self.create_line_item(itemObjs.asTupleForHTML())

        self.create_subtotal(self.invoiceObj.no_calc_get_subtotal())
        self.create_discount(self.invoiceObj.get_discount_amount())
        self.create_total(self.invoiceObj.no_calc_get_total())
        self.create_signature_line_and_close()
        self.file_handle.close()

        open_new_tab(self.completeFileName)

    def fetch_entity(self, entity_id):
        entityObj = self.coordinator.get_entity_by_id(entity_id)
        print("FROM GPFIS2HTML ENTITY", entityObj)

        return entityObj

    def creater_header(self, inv_num):
        html_string = """<!DOCTYPE HTML>
        <html>
            <head>
                <title>Green Paradise Farms - %s</title>
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
                <p id="GPFAddressTitle">GREEN PARADISE FARM <br>2555 Guajome Lake Road<br>Vista, CA, 92084<br>Tel: (760) 724-1123<br>Fax: (760) 724-5566</p>
            </div>"""
        logo_and_address = html_string % (self.logo_path)
        self.file_handle.write(logo_and_address)
        
    def create_invoice_num(self, inv_num):
        html_string = """<div class = "invoicenumber"><p>Invoice Number: </p> <p id="inv_num">%s</p></div>"""
        invoice_area = html_string % (inv_num)
        self.file_handle.write(invoice_area)

    def create_date(self, date):
        html_string = """<div class = "datefield"><p>Invoice Date: </p> <p id="datevalue">%s</p></div>"""
        date_area = html_string % (date)
        self.file_handle.write(date_area)

    def create_shipto(self, customer_name, street_num, street_name, city, state, zip):
        #customer name, address (street_num + street_name), city, state, zip
        html_string = """<div class = "shipto"><p>Ship to: </p> <p id = "storename" >%s<br> %s %s,<br> %s, %s, %s</p></div>"""
        shipto = html_string % (customer_name, street_num, street_name, city, state, zip)

        self.file_handle.write(shipto)

    def create_billto(self, customer_name, street_num, street_name, city, state, zip):
        #customer name, address (street_num + street_name), city, state, zip
        html_string = """<div class = "billto"><p>Bill to: </p> <p id = "storename" >%s<br> %s %s,<br> %s, %s, %s</p></div>"""
        billto = html_string % (customer_name, street_num, street_name, city, state, zip)

        self.file_handle.write(billto)

    def create_subheader(self, terms, due_date, po, credit_amnt, credit_inv, notes):
        html_string = """
        <div class = "subheader">
            <table id = "subheader_table">
                <tr><th>Payment Terms</th><th>Due Date</th><th>Customer PO</th></tr>
                <tr><td>%s</td><td>%s</td><td>%s</td></tr>
                
                <tr><th>Credit Total</th><th>Credit Invoice Number</th><th>Notes</th></tr>
                <tr><td>$%s</td><td>%s</td><td>%s</td></tr>
            </table>
        </div>"""
        subheader = html_string % (terms, due_date, po, credit_amnt, credit_inv, notes)

        self.file_handle.write(subheader)

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


class GPFISStatment2HTML():

    document_location = r"C:\Users\dunju\Documents\GPF\GPFISHTMLObjects\Invoices"
    css_path = "./css/gpf_statement.css"
    logo_path = "./imgs/gpf_logo.png"

    def __init__(self, invoice_list, customer_name, begin_date, end_date, outstanding_balance, grand_total):
        self.coordinator = GPFISCoordinator()
        self.invoice_list = invoice_list
        self.customer_name = customer_name
        self.begin_date = begin_date
        self.end_date = end_date
        self.outstanding_balance = outstanding_balance
        self.grand_total = grand_total

    def build_HTML_statement(self):
        self.set_file_name()
        self.creater_header()
        self.create_GPF_logo_and_address()
        self.create_title(self.customer_name, self.begin_date, self.end_date)
        self.create_static_item_table_info()

        for invoice in self.invoice_list:
            self.create_line_item(invoice.asTupleForHTMLStatement())

        self.create_statement_total_line()

        self.close_html_doc()

        self.file_handle.close()

        open_new_tab(self.completeFileName)

    def create_statement_total_line(self):
        line_tuple = ("", "", "","Outstanding Balance", self.outstanding_balance, "Total", self.grand_total)
        self.create_line_item(line_tuple)

    def set_file_name(self):
        now = datetime.datetime.today().strftime("%Y%m%d_%H%M") 
        self.file_name = str(self.customer_name) + "_" + now + ".html"
        self.completeFileName = os.path.join(self.document_location, self.file_name)
        print(self.completeFileName)
        self.file_handle = open(self.completeFileName, 'w')

    def creater_header(self):
        html_string = """<!DOCTYPE HTML>
        <html>
            <head>
                <title>Green Paradise Farms</title>
                <meta charset="utf-8" />
                <link rel="stylesheet" href="%s">
            </head>"""
        header = html_string % (self.css_path)
        self.file_handle.write(header)
        
    def create_GPF_logo_and_address(self):
        html_string = """   <body>
        <div class = "wrapper">
            <div class = "logoandinfo">
                <img id="GPFLogo" src="%s">
                <p id="GPFAddressTitle">2555 Guajome Lake Road<br>Vista, California, 92084-1610<br>Tel: (760) 724-1123<br>Fax: (760) 724-5566</p>
            </div>"""
        logo_and_address = html_string % (self.logo_path)
        self.file_handle.write(logo_and_address)

    def create_title(self, customer_name, date_begin, date_end):
        html_string = """<div class = "title">
        <p id="statement_title">Statement for %s from %s to %s.</p>
        </div>"""
        title = html_string % (customer_name, date_begin, date_end)
        self.file_handle.write(title)

    def create_static_item_table_info(self):
        html_string = """<div class = "itemtable">
            <table id = "theitemtable">
                <tr id="headervalues">
                    <th>Invoice #</th>
                    <th>Bill To</th>
                    <th>Ship To</th>
                    <th>Invoice Date</th>
                    <th>Delivery Date</th>
                    <th>Payment Status</th>
                    <th>Invoice Total</th>
                </tr>"""

        self.file_handle.write(html_string)
        
    def create_line_item(self, lineItemTuple):
        #inv_num, bill to, ship tp, invoice date, delivery date, payment status, invoice total
        html_string = """<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>$%s</td></tr>"""
        line_item = html_string % lineItemTuple

        self.file_handle.write(line_item)

    def close_html_doc(self):
        html_string = """</div></body></html>"""

        self.file_handle.write(html_string)