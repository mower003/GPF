import locale
from enum import Enum

class ProductObjEnum(Enum):
    PRODUCT_ID = 0
    PRODUCT_NAME = 1
    DESCRIPTION = 2
    UNIT_PRICE = 3
    CASE_STYLE = 4
    NOTE = 5


class ProductObj:
    locale.setlocale(locale.LC_ALL, 'en_US')

    def __init__(self, id=-1, name='', description='', unit_price=0.00, note='', case_style='', *, productList = None):
        if productList is None:
            self.id = int(id)
            self.name = name
            self.description = description
            self.unit_price = locale.currency(unit_price, False, False, False)
            self.case_style = case_style
            self.note = note
        else:
            self.id = productList[ProductObjEnum.PRODUCT_ID.value]
            self.name = productList[ProductObjEnum.PRODUCT_NAME.value]
            self.description = productList[ProductObjEnum.DESCRIPTION.value]
            self.unit_price = locale.currency((float(productList[ProductObjEnum.UNIT_PRICE.value])), False, False, False)
            self.case_style = productList[ProductObjEnum.CASE_STYLE.value]
            self.note = productList[ProductObjEnum.NOTE.value]

        product_representation = "######################Product Object created######################"+'\n'+"Product ID: " + str(self.id) + '\n' + "Name: " + str(self.name) + '\n' + "Description: " + str(self.description) + '\n' + "Unit Price: " + str(self.unit_price) + '\n' + "Note: " + str(self.note) + '\n' + "Case Style: " + str(self.case_style)
        print("######################Product Object created######################"+'\n'+self.__repr__())
        #print("ProductObj __init__ called with params: %i, %s, %s, %f, %s, %s." % (self.id, self.name, self.description, float(self.unit_price),  self.note, self.case_style))


    def __repr__(self) -> str:
        product_representation = '\n'+"Product ID: " + str(self.id) + '\n' + "Name: " + str(self.name) + '\n' + "Description: " + str(self.description) + '\n' + "Unit Price: " + str(self.unit_price) + '\n' + "Note: " + str(self.note) + '\n' + "Case Style: " + str(self.case_style)

        return product_representation

    def asList(self):
        list = []
        list.insert(ProductObjEnum.PRODUCT_ID.value, self.id)
        list.insert(ProductObjEnum.PRODUCT_NAME.value, self.name)
        list.insert(ProductObjEnum.DESCRIPTION.value, self.description)
        list.insert(ProductObjEnum.UNIT_PRICE.value, self.unit_price)
        list.insert(ProductObjEnum.CASE_STYLE.value, self.case_style)
        list.insert(ProductObjEnum.NOTE.value, self.note)

        return list

    def asListForDBInsertion(self):
        list = []
        list.insert(ProductObjEnum.PRODUCT_ID.value, self.id)
        list.insert(ProductObjEnum.PRODUCT_NAME.value, self.name)
        list.insert(ProductObjEnum.DESCRIPTION.value, self.description)
        list.insert(ProductObjEnum.UNIT_PRICE.value, self.unit_price)
        list.insert(ProductObjEnum.CASE_STYLE.value, self.case_style)
        list.insert(ProductObjEnum.NOTE.value, self.note)
        return list

    #Special case where list has to be static since list order matters for db update function
    def asListForDBUpdate(self):
        list = []
        list.append(self.name)
        list.append(self.description)
        list.append(self.unit_price)
        list.append(self.case_style)
        list.append(self.note)
        list.append(self.id)

        return list

    def addProductAsList(self, productList=None):
        if productList is None:
            print("From Product.py -> addProductAsList() param productList is None")
        else:
            print("From Product.py addProductAsList() : productList param = ", productList)
            self.id = int(productList[ProductObjEnum.PRODUCT_ID.value])
            self.name = productList[ProductObjEnum.PRODUCT_NAME.value]
            self.description = productList[ProductObjEnum.DESCRIPTION.value]
            self.unit_price = locale.currency((float(productList[ProductObjEnum.UNIT_PRICE.value])), False, False, False)
            self.note = productList[ProductObjEnum.NOTE.value]
            self.case_style = productList[ProductObjEnum.CASE_STYLE.value]

    def toString(self):
        the_str = str(self.id) + " " + str(self.name) + " " + str(self.description) + " " + str(self.unit_price) + " " + str(self.case_style) + " " + str(self.note)
        return the_str

    def setID(self, id):
        self.id = id
    
    def setName(self, name):
        self.name = name

    def setDescription(self, desc):
        self.description = desc

    def setUnitPrice(self, up):
        self.unit_price = up

    def setCaseStyle(self, cs):
        self.case_style = cs

    def setNote(self, note):
        self.note = note

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getUnitPrice(self):
        return self.unit_price

    def getCaseStyle(self):
        return self.case_style

    def getNote(self):
        return self.note