from InvoiceItem import InvoiceItemObj as invItemObj
import locale

class InvoiceObj:
    locale.setlocale(locale.LC_ALL, 'en_US')

    def __init__(self, invoice_number=-37, creation_date=None, delivery_date=None, note='', issuer_id=37, buyer_id=-37, status=0, discount_rate=0, tax_amount=0, subtotal=0.00, total=0, credit_inv_num=0, lineItems=[]) -> None:
        self.invoice_number = invoice_number
        self.creation_date = creation_date
        self.delivery_date = delivery_date
        self.note = note
        self.issuer_id = issuer_id
        self.issuer_name = ''
        self.buyer_id = buyer_id
        self.buyer_name = ''
        self.status = status
        self.discount_rate = discount_rate
        self.total = locale.currency(total, False, False, False)
        self.subtotal = locale.currency(subtotal, False, False, False)
        self.tax_amount = locale.currency(tax_amount, False, False, False)
        self.credit_inv_num = credit_inv_num
        self.invItemsObjList = []

        print("InvoiceObj __init__ called with params: %i, %s, %s, %s, %i, %i, %i, %d, %f, %f, %f, %i." % (self.invoice_number, self.creation_date, self.delivery_date, self.note, self.issuer_id, self.buyer_id, self.status, self.discount_rate, float(self.tax_amount), float(self.subtotal), float(self.total), self.credit_inv_num))

    def calculate_invoice_total(self):
        self.total = float(self.subtotal) * (1 - float(self.discount_rate)) + float(self.tax_amount)
        self.total = round(self.total, 2)
        return float(self.total)

    def calculate_invoice_subtotal(self):
        for items in self.invItemsObjList:
            #print(items.calculateLineTotal())
            self.subtotal = round(float(self.subtotal) + float(items.calculateLineTotal()),2)
        return float(self.subtotal)

    def toList(self):
        list = []
        list.append(self.invoice_number)
        list.append(self.creation_date)
        list.append(self.delivery_date)
        list.append(self.note)
        list.append(self.issuer_id)
        list.append(self.issuer_name)
        list.append(self.buyer_id)
        list.append(self.buyer_name)
        list.append(self.status)
        list.append(self.discount_rate)
        list.append(self.tax_amount)
        list.append(self.subtotal)
        list.append(self.total)
        list.append(self.invItemsObjList)
        return list

    def asListForDBInsertion(self):
        list = []
        list.append(self.creation_date)
        list.append(self.delivery_date)
        list.append(self.note)
        list.append(self.issuer_id)
        list.append(self.buyer_id)
        list.append(self.status)
        list.append(self.discount_rate)
        list.append(self.subtotal)
        list.append(self.tax_amount)
        list.append(self.credit_inv_num)
        return list

    def getInvoiceItemList(self):
        return self.invItemsObjList

    def addInvoiceItem(self, line_id = -999, invoice_id=-1, product_id=-1, case_quantity='', quantity=-1, unit_price=-1, line_note='', *, invItemAsList=None):

        if invItemAsList is None:
            iio = invItemObj(invoice_id, product_id, case_quantity, quantity, unit_price, line_note)
            self.invItemsObjList.append(iio)
        else:
            iio = invItemObj()
            print("from addinvoiceitem",invItemAsList)
            iio.addInvoiceItemAsList(invItemAsList)
            self.invItemsObjList.append(iio)

    #Setters/Getters below here 
    def set_inv_num(self, num):
        self.invoice_number = num
        print(self.invoice_number)

    def set_creation_date(self, date):
        self.creation_date = date
        print(self.creation_date)

    def set_delivery_date(self, date):
        self.delivery_date = date
        print(self.delivery_date)

    def set_note(self, note):
        self.note = note
        print(self.note)

    def set_issuer_id(self, issuer_id):
        self.issuer_id = issuer_id
        print(self.issuer_id)

    def set_buyer_id(self, buyer_id):
        self.buyer_id = buyer_id
        print(self.buyer_id)

    def set_status(self, status):
        self.status = status
        print(self.status)

    def set_discount_rate(self, rate=0):
        if rate >= 1 or rate < 0:
            rate = 0
        else:
            self.discount_rate = rate
        print(self.discount_rate)

    def set_tax_amount(self, amount):
        self.tax_amount = amount
        print(self.tax_amount)

    def set_subtotal(self, subtotal):
        self.subtotal = subtotal
        print(self.subtotal)

    def set_total(self, total):
        self.total = total
        print(self.total)

    # Basic Getters
    def get_inv_num(self):
        return self.invoice_number

    def get_creation_date(self):
        return self.creation_date

    def get_delivery_date(self):
        return self.delivery_date

    def get_note(self, note):
        return self.note

    def get_issuer_id(self):
        return self.issuer_id

    def get_buyer_id(self):
        return self.buyer_id

    def get_status(self):
        return self.status

    def get_discount_rate(self):
        return self.discount_rate

    def get_tax_amount(self):
        return self.tax_amount

    def get_subtotal(self):
        return self.subtotal 

    def get_total(self):
        return self.total


#i = InvoiceObj()
#i.addInvoiceItem(1, 77, 12, 2.00)
#i.addInvoiceItem(2, 78, 13, 2.53)
#print(i.calculate_invoice_subtotal())
#i.invoiceItemsAsList()
#i.set_discount_rate()
#i.set_discount_rate(-1)
#i.set_discount_rate(0)
#i.set_discount_rate(1)
#i.set_discount_rate(2)
#i.set_discount_rate(.5)