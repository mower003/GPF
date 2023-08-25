import locale
import re
from enum import Enum

class InvoiceItemEnum(Enum):
    LINE_ID = 0
    INVOICE_ID = 1
    PRODUCT_ID = 2
    CASE_QUANTITY = 3
    QUANTITY = 4
    UNIT_PRICE = 5
    LINE_NOTE = 6
    TAX_RATE = 7
    #DESCRIPTION = 5 (NOT USED)

class InvoiceItemObj:
    locale.setlocale(locale.LC_ALL, 'en_US')

    def __init__(self, line_id = -999, invoice_id = -1, product_id = -1, case_quantity = '', quantity = -1, unit_price = 0.00, tax_rate = 0, line_note='', *, invItemList=None):
        if invItemList is None:
            self.unit_price = locale.currency(float(unit_price), False, False, False)
            self.line_id = line_id
            self.invoice_id = invoice_id
            self.product_id = product_id
            self.case_quantity = case_quantity
            self.quantity = int(quantity)
            self.tax_rate = tax_rate
            self.line_note = line_note

            #These are not part of DB definition of invoice_item, must be set after the fact.
            self.line_total = 0.00
            self.product_description = ''
        else:
            self.line_id = invItemList[InvoiceItemEnum.LINE_ID.value]
            self.unit_price = locale.currency(float(invItemList[InvoiceItemEnum.UNIT_PRICE.value]), False, False, False)
            self.invoice_id = invItemList[InvoiceItemEnum.INVOICE_ID.value]
            self.product_id = invItemList[InvoiceItemEnum.PRODUCT_ID.value]
            self.case_quantity = invItemList[InvoiceItemEnum.CASE_QUANTITY.value]
            self.quantity = int(invItemList[InvoiceItemEnum.QUANTITY.value])
            self.tax_rate = invItemList[InvoiceItemEnum.TAX_RATE.value]
            self.line_note = invItemList[InvoiceItemEnum.LINE_NOTE.value]

            #These are not part of DB definition of invoice_item, must be set after the fact.
            self.line_total = 0.00
            self.product_description = ''

        #print("InvoiceItemObj __init__ called with params: %s, %s, %s, %s, %s, %s, %s, %s. %s." % (self.line_id, self.invoice_id, self.product_id, self.case_quantity, self.quantity, self.unit_price, self.line_note, self.tax_rate, self.tax_amount))

    def __str__(self):
        the_string = str(self.line_id) + " " + str(self.invoice_id) + " " + str(self.product_id) + " " + str(self.case_quantity) + " " + str(self.quantity) + " " + str(self.unit_price)
        return the_string
    
    def __repr__(self):
        invoice_item_representation = "Line ID: " + str(self.line_id) + " " + "Unit Price: " + str(self.unit_price) + " " + "Invoice Number: " + str(self.invoice_id) + " " + "Product ID: " + str(self.product_id) + " " + "Product Description: " + str(self.product_description) + " " + "Case Quantity: " + str(self.case_quantity) + " " + "Quantity: " + str(self.quantity) + " " + "Tax Rate: " + str(self.tax_rate) + " " + "Line Note: " + str(self.line_note) + " " + "Line Total: " + str(self.line_total) + '\n'
        
        return invoice_item_representation
    
    def addInvoiceItemAsList(self, invoiceItemList=None):
        print("Inside InvoiceItem:addInvoiceItemAsList()",invoiceItemList)
        if invoiceItemList is None:
            print("InvoiceItemObj:addInvoiceItemAsList() -> No invoiceItemList!")
        else:
            self.invoice_id = invoiceItemList[InvoiceItemEnum.INVOICE_ID.value]
            self.line_id = invoiceItemList[InvoiceItemEnum.LINE_ID.value]
            self.product_id = invoiceItemList[InvoiceItemEnum.PRODUCT_ID.value]
            self.case_quantity = invoiceItemList[InvoiceItemEnum.CASE_QUANTITY.value]
            self.quantity = invoiceItemList[InvoiceItemEnum.QUANTITY.value]
            self.unit_price = locale.currency(round(float(invoiceItemList[InvoiceItemEnum.UNIT_PRICE.value]),2), False, False, False)
            self.line_note = re.sub(r"[\n\t]*", "", invoiceItemList[InvoiceItemEnum.LINE_NOTE.value])
            self.tax_rate = invoiceItemList[InvoiceItemEnum.TAX_RATE.value]

    def toList(self):
        list = [self.line_id, self.invoice_id, self.product_id, self.case_quantity, self.quantity, self.unit_price, self.tax_rate, self.line_note]
        return list
    
    def asListForDBInsertion(self):
        list = [self.line_id, self.invoice_id, self.product_id, self.case_quantity, self.quantity, self.unit_price, self.line_note]
        return list
    
    def asUpdateList(self):
        list = [self.line_id, self.quantity, self.case_quantity, self.product_id, self.product_description,  self.line_note, self.unit_price, self.line_total]
        return list
    
    def asTupleForHTML(self):
        return (self.quantity, self.case_quantity, self.product_id, self.product_description, self.line_note, self.unit_price, locale.currency(round(float(self.line_total),2), True, True, False))

    def toString(self):
        the_string = str(self.line_id) + " " + str(self.invoice_id) + " " + str(self.product_id) + " " + str(self.case_quantity) + " " + str(self.quantity) + " " + str(self.unit_price)
        return the_string

    def calculateLineTotal(self):
        self.line_total = int(self.quantity) * float(self.unit_price)
        print("Line Total Calculation -> ", locale.currency(float(self.line_total), False, False, False))
        self.line_total = round(float(self.line_total), 2)
        return self.line_total
    
    def setDescription(self, product_description):
        self.product_description = product_description

    def getDescription(self):
        return self.product_description
    
    def getProductID(self):
        return self.product_id
        