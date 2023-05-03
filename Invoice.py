from InvoiceItem import InvoiceItemObj as invItemObj
from Entity import EntityObj
import locale
from enum import Enum


#Invoice data object needs to have
"""
Invoice number
Invoice Date
Ship Date
Due Date
Issuer ID,
Buyer ID
ShipTo ID
Status,
Sales Tax,
Subtotal
Discount Amount
Customer Purchase Order #
Payment Terms
Applied Credit Amount
Credit Invoice Number

"""

class InvoiceObjEnum(Enum):
    INVOICE_NUMBER = 0
    INVOICE_DATE = 1
    SHIP_DATE = 2
    DUE_DATE = 3
    ISSUER_ID = 4
    BUYER_ID = 5
    SHIP_TO_ID = 6
    STATUS = 7
    SALES_TAX = 8
    SUBTOTAL = 9
    DISCOUNT_AMOUNT = 10
    TOTAL = 11 #NOT IN INVOICE DB
    CUSTOMER_PO_NUM = 12
    PAYMENT_TERMS = 13
    APPLIED_CREDIT_AMOUNT = 14
    CREDIT_INVOICE_NUMBER = 15
    NOTE = 16

class InvoiceObj:
    locale.setlocale(locale.LC_ALL, 'en_US')

    def __init__(self, inv_num = -999, inv_date = '01-01-0001', ship_date='01-01-0001', due_date='01-01-0001', issuer_id=37, buyer_id=-1, shiptoid=-1, status=-1, sales_tax=-1, subtotal=-1, discount=-1, total=-1, customerpo='', paymentterms='', creditamnt=-1, creditnum=-1, note ='', *, invList=None):

        if invList is None:
            self.invoice_number = inv_num
            self.invoice_date = inv_date
            self.ship_date = ship_date
            self.due_date = due_date
            self.issuer_id = issuer_id
            self.buyer_id = buyer_id
            self.ship_to_id = shiptoid
            self.status = status
            self.sales_tax = sales_tax
            self.subtotal = subtotal
            self.discount_amount = discount
            self.total = total
            self.customer_po_number = customerpo
            self.payment_terms = paymentterms
            self.applied_credit_amount = creditamnt
            self.credit_inv_num = creditnum
            self.note = note
        else:
            self.invoice_number = invList[InvoiceObjEnum.INVOICE_NUMBER.value]
            self.invoice_date = invList[InvoiceObjEnum.INVOICE_DATE.value]
            self.ship_date = invList[InvoiceObjEnum.SHIP_DATE.value]
            self.due_date = invList[InvoiceObjEnum.DUE_DATE.value]
            self.issuer_id = invList[InvoiceObjEnum.ISSUER_ID.value]
            self.buyer_id = invList[InvoiceObjEnum.BUYER_ID.value]
            self.ship_to_id = invList[InvoiceObjEnum.SHIP_TO_ID.value]
            self.status = invList[InvoiceObjEnum.STATUS.value]
            self.sales_tax = invList[InvoiceObjEnum.SALES_TAX.value]
            self.subtotal = locale.currency(float(invList[InvoiceObjEnum.SUBTOTAL.value]), False, False, False)
            self.discount_amount = locale.currency(float(invList[InvoiceObjEnum.DISCOUNT_AMOUNT.value]), False, False, False)
            self.total = locale.currency(0.0, False, False, False)
            self.customer_po_number = invList[InvoiceObjEnum.CUSTOMER_PO_NUM.value]
            self.payment_terms = invList[InvoiceObjEnum.PAYMENT_TERMS.value]
            self.applied_credit_amount = locale.currency(float(invList[InvoiceObjEnum.APPLIED_CREDIT_AMOUNT.value]), False, False, False)
            self.credit_inv_num = invList[InvoiceObjEnum.CREDIT_INVOICE_NUMBER.value]
            self.note = invList[InvoiceObjEnum.NOTE.value]
        
        self.invItemsObjList = []

        self.issuer = EntityObj()
        self.buyer = EntityObj()
        self.shipto = EntityObj()

        self.calculate_invoice_total()
        print("######################Invoice Object created######################"+'\n'+self.__repr__())

    def __repr__(self) -> str:
        invoice_representation = '\n' \
        + "Invoice Number: " + str(self.invoice_number) + '\n' \
        + "Invoice Date: " + str(self.invoice_date) + '\n' \
        + "Ship Date: " + str(self.ship_date) + '\n' \
        + "Due Date: " + str(self.due_date) + '\n' \
        + "Issuer ID: " + str(self.issuer.getID()) + '\n' \
        + "Issuer Name: " + str(self.issuer.getName()) + '\n' \
        + "Issuer Address: " + str(self.issuer.getAsAddressString()) + '\n' \
        + "Buyer ID: " + str(self.buyer.getID()) + '\n' \
        + "Buyer Name: " + str(self.buyer.getName()) + '\n' \
        + "Buyer Address: " + str(self.buyer.getAsAddressString()) + '\n' \
        + "Ship To ID: " + str(self.shipto.getID()) + '\n' \
        + "Ship To Name: " + str(self.shipto.getName()) + '\n' \
        + "Ship To Address: " + str(self.shipto.getAsAddressString()) + '\n' \
        + "Status: " + str(self.status) + '\n' \
        + "Sales Tax Amount: " + str(self.sales_tax) + '\n' \
        + "Subtotal: " + str(self.subtotal) + '\n' \
        + "Discount Amount: " + str(self.discount_amount) + '\n' \
        + "Total: " + str(self.total) + '\n' \
        + "Customer PO Number: " + str(self.customer_po_number) + '\n' \
        + "Payment Terms: " + str(self.payment_terms) + '\n' \
        + "Applied Credit Amount: " + str(self.applied_credit_amount) + '\n' \
        + "Credit Invoice Number: " + str(self.credit_inv_num) + '\n' \
        + "Note: " + str(self.note)  + '\n' \
        + "Invoice Line Items: " + str(self.getInvoiceItemList())

        return invoice_representation
    
    def calculate_invoice_total(self):
        try:
            self.total = float(self.subtotal) - float(self.discount_amount) + float(self.sales_tax)
            self.total = locale.currency(self.total, False, False, False)
            return self.total
        except ValueError as e:
            print(e)

    def calculate_invoice_subtotal(self):
        if self.invItemsObjList.__len__ == 0:
            print("No items in Invoice Items Object List")
            return 0
        else:
            for items in self.invItemsObjList:
                #print(items.calculateLineTotal())
                self.subtotal = round(float(self.subtotal) + float(items.calculateLineTotal()),2)
                self.subtotal = locale.currency(self.subtotal, False, False, False)
            return self.subtotal

    def toList(self):
        list = []
        list.append(self.invoice_number)
        list.append(self.invoice_date)
        list.append(self.ship_date)
        list.append(self.due_date)
        list.append(self.get_issuer_id())
        list.append(self.get_issuer_name())
        list.append(self.get_issuer_address())
        list.append(self.get_buyer_id())
        list.append(self.get_buyer_name())
        list.append(self.get_buyer_address())
        list.append(self.get_ship_to_id())
        list.append(self.get_ship_to_name())
        list.append(self.get_ship_to_address())
        list.append(self.status)
        list.append(self.sales_tax)
        list.append(self.subtotal)
        list.append(self.discount_amount) 
        list.append(self.total)
        list.append(self.customer_po_number)
        list.append(self.payment_terms)
        list.append(self.applied_credit_amount)
        list.append(self.credit_inv_num)
        list.append(self.note)
        return list

    def asListForDBInsertion(self):
        list = []
        list.append(self.invoice_date)
        list.append(self.ship_date)
        list.append(self.due_date)
        list.append(self.get_issuer_id())
        list.append(self.get_buyer_id())
        list.append(self.get_ship_to_id())
        list.append(self.status)
        list.append(self.sales_tax)
        list.append(self.subtotal)
        list.append(self.discount_amount) 
        list.append(self.customer_po_number)
        list.append(self.payment_terms)
        list.append(self.applied_credit_amount)
        list.append(self.credit_inv_num)
        list.append(self.note)
        return list
    
    def asListForDBUpdate(self):
        list = []
        list.append(self.invoice_date)
        list.append(self.ship_date)
        list.append(self.due_date)
        list.append(self.get_issuer_id())
        list.append(self.get_buyer_id())
        list.append(self.get_ship_to_id())
        list.append(self.sales_tax)
        list.append(self.subtotal)
        list.append(self.discount_amount) 
        list.append(self.customer_po_number)
        list.append(self.payment_terms)
        list.append(self.applied_credit_amount)
        list.append(self.credit_inv_num)
        list.append(self.note)
        list.append(self.invoice_number)
        return list

    def getInvoiceItemList(self):
        return self.invItemsObjList

    def addInvoiceItem(self, line_id = -999, invoice_id=-1, product_id=-1, case_quantity='', quantity=-1, unit_price=-1, line_note='', *, invItemAsList=None):

        if invItemAsList is None:
            iio = invItemObj(line_id, self.invoice_number, product_id, case_quantity, quantity, unit_price, line_note)
            self.invItemsObjList.append(iio)
        else:
            iio = invItemObj()
            invItemAsList.insert(1, self.invoice_number)
            print("from addinvoiceitem",invItemAsList)
            iio.addInvoiceItemAsList(invItemAsList)
            self.invItemsObjList.append(iio)

    #Setters/Getters below here 
    def set_inv_num(self, num):
        self.invoice_number = num
        print(self.invoice_number)

    def set_invoice_date(self, date):
        self.invoice_date = str(date)
        print(self.invoice_date)

    def set_ship_date(self, date):
        self.ship_date = str(date)
        print(self.ship_date)

    def set_due_date(self, date):
        self.due_date = str(date)
        print(self.due_date)

    def set_note(self, note):
        self.note = note
        print(self.note)

    def set_issuer(self, issuer_object):
        self.issuer = issuer_object

    def set_issuer_id(self, issuer_id):
        self.issuer_id = issuer_id
        print(self.issuer_id)

    def set_issuer_name(self, issuer_name):
        self.issuer_name = issuer_name
        print(self.issuer_name)

    def set_issuer_address(self, issuer_address):
        self.issuer_address = issuer_address
        print(self.issuer_address)

    def set_buyer(self, buyer_object):
        self.buyer = buyer_object

    def set_buyer_id(self, buyer_id):
        self.buyer_id = buyer_id
        print(self.buyer_id)

    def set_buyer_name(self, buyer_name):
        self.buyer_name = buyer_name
        print(buyer_name)

    def set_buyer_address(self, buyer_address):
        self.buyer_address = buyer_address
        print(self.buyer_address)

    def set_shipto(self, shipto_object):
        self.shipto = shipto_object

    def set_ship_to_id(self, shipto_id):
        self.ship_to_id = shipto_id
        print(self.ship_to_id)

    def set_ship_to_name(self, ship_to_name):
        self.ship_to_name = ship_to_name
        print(self.ship_to_name)

    def set_ship_to_address(self, ship_to_addr):
        self.ship_to_address = ship_to_addr
        print(self.ship_to_address)

    def set_status(self, status):
        self.status = status
        print(self.status)

    def set_po_number(self, po_num):
        self.customer_po_number = po_num
        print(self.customer_po_number)

    def set_applied_credit_amount(self, credit_amnt):
        self.applied_credit_amount = round(float(credit_amnt),2)
        print(self.applied_credit_amount)

    def set_payment_terms(self, payment_terms):
        self.payment_terms = payment_terms
        print(payment_terms)

    def set_discount_amount(self, amount=0):
        self.discount_amount = locale.currency(float(amount), False, False, False)
        print(self.discount_amount)

    def set_sales_tax(self, amount):
        self.sales_tax = locale.currency(float(amount), False, False, False)
        print(self.sales_tax)

    def set_subtotal(self, subtotal):
        self.subtotal = locale.currency(float(subtotal), False, False, False)
        print(self.subtotal)

    def set_total(self, total):
        self.total = locale.currency(float(total), False, False, False)
        print(self.total)

    def set_note(self, note):
        self.note = note
        print(self.note)

    def set_credit_invoice_number(self, credit_inv_num):
        self.credit_inv_num = credit_inv_num
        print(self.credit_inv_num)

    # Basic Getters
    def get_inv_num(self):
        return self.invoice_number

    def get_creation_date(self):
        return self.invoice_date

    def get_delivery_date(self):
        return self.ship_date
    
    def get_due_date(self):
        return self.due_date

    def get_note(self, note):
        return self.note

    def get_issuer_id(self):
        return self.issuer.getID()
    
    def get_issuer_name(self):
        return self.issuer.getName()
    
    def get_issuer_address(self):
        return self.issuer.getAsAddressString()

    def get_buyer_id(self):
        return self.buyer.getID()
    
    def get_buyer_name(self):
        return self.buyer.getName()
    
    def get_buyer_address(self):
        return self.buyer.getAsAddressString()
    
    def get_ship_to_id(self):
        return self.shipto.getID()
    
    def get_ship_to_name(self):
        return self.shipto.getName()
    
    def get_ship_to_address(self):
        return self.shipto.getAsAddressString()

    def get_status(self):
        return self.status
    
    def get_po_number(self):
        return self.customer_po_number

    def get_applied_credit_amount(self):
        return self.applied_credit_amount

    def get_payment_terms(self):
        return self.payment_terms

    def get_discount_amount(self):
        return self.discount_amount

    def get_sales_tax(self):
        return self.sales_tax

    def get_subtotal(self):
        return self.subtotal 

    def get_total(self):
        return self.total
    
    def get_note(self):
        return self.note
    
    def get_credit_inv_num(self):
        return self.credit_inv_num