import locale
from enum import Enum

class InvoiceItemEnum(Enum):
    INVOICE_ID = 0
    PRODUCT_ID = 1
    QUANTITY = 2
    CASE_QUANTITY = 3
    UNIT_PRICE = 4
    TAX_RATE = 5
    TAX_AMOUNT = 6
    LINE_NOTE = 7

class InvoiceItemObj:
    locale.setlocale(locale.LC_ALL, 'en_US')

    def __init__(self, invoice_id = -1, product_id = -1, case_quantity = '', quantity = -1, unit_price = 0.00, tax_rate = 0, tax_amount = 0.00, line_note=''):
        self.unit_price = locale.currency(unit_price, False, False, False)
        self.invoice_id = invoice_id
        self.product_id = product_id
        self.case_quantity = case_quantity
        self.quantity = quantity
        self.tax_rate = tax_rate
        self.tax_amount = tax_amount
        self.line_note = line_note

    def addInvoiceItemAsList(self, invoiceItemList=None):
        if invoiceItemList is None:
            print("InvoiceItemObj:addInvoiceItemAsList() -> No invoiceItemList!")
        else:
            self.invoice_id = invoiceItemList[InvoiceItemEnum.INVOICE_ID.value]
            self.product_id = invoiceItemList[InvoiceItemEnum.PRODUCT_ID.value]
            self.case_quantity = invoiceItemList[InvoiceItemEnum.CASE_QUANTITY.value]
            self.quantity = invoiceItemList[InvoiceItemEnum.QUANTITY.value]
            self.unit_price = locale.currency(invoiceItemList[InvoiceItemEnum.UNIT_PRICE.value], False, False, False)
            self.line_note = invoiceItemList[InvoiceItemEnum.LINE_NOTE.value]
            #self.tax_rate = invoiceItemList[InvoiceItemEnum.TAX_RATE.value]
            #self.tax_amount = invoiceItemList[InvoiceItemEnum.TAX_AMOUNT.value]

    def toList(self):
        list = [self.invoice_id, self.product_id, self.case_quantity, self.quantity, self.unit_price, self.tax_rate, self.tax_amount, self.line_note]
        return list

    def asListForDBInsertion(self):
        list = [self.invoice_id, self.product_id, self.case_quantity, self.quantity, self.unit_price, self.line_note]
        return list

    def toString(self):
        the_string = str(self.invoice_id) + " " + str(self.product_id) + " " + str(self.case_quantity) + " " + str(self.quantity) + " " + str(self.unit_price)
        return the_string

    def calculateLineTotal(self):
        line_total = int(self.quantity) * float(self.unit_price)
        return line_total
        