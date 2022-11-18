import locale
from enum import Enum

class EntityObjEnum(Enum):
    ENTITY_ID = 0
    ENTITY_NAME = 1
    IS_ACTIVE = 2
    STREET_NUMBER = 3
    STREET_NAME = 4
    CITY = 5
    STATE = 6
    ZIP = 7
    COUNTRY = 8

class EntityObj:
    locale.setlocale(locale.LC_ALL, 'en_US')

    def __init__(self, *, id=-1, name='', street_number='', street_name='', city='', state='', zip='', country='', is_active=1) -> None:
        self.id = id
        self.name = name
        self.street_name = street_name
        self.street_number = street_number
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.is_active = is_active

        print("EntityObj __init__ called with params: %i, %s, %s, %s, %s, %s, %s, %s, %i." % (self.id, self.name, self.street_number, self.street_name, self.city, self.state, self.zip, self.country, self.is_active))

    def toList(self):
        list = []
        list.append(self.id)
        list.append(self.name)
        list.append(self.is_active)
        list.append(self.street_number)
        list.append(self.street_name)
        list.append(self.city)
        list.append(self.state)
        list.append(self.zip)
        list.append(self.country)
        return list

    def asListForDBInsertion(self):
        list = []
        list.append(self.id)
        list.append(self.name)
        list.append(self.is_active)
        list.append(self.street_number)
        list.append(self.street_name)
        list.append(self.city)
        list.append(self.state)
        list.append(self.zip)
        list.append(self.country)

        return list

    def toString(self):
        return_str = str(self.id) + " " + self.name + " " + self.street_number + " " + self.street_name + " " + self.city + " " + self.state + " " + self.zip + " " + self.country
        return return_str

    def getAsAddressString(self):
        return_str = self.street_number + " " + self.street_name + " " + self.city + " " + self.state + " " + self.zip + " " + self.country
        return return_str

    def addEntityAsTuple(self, EntityTuple=None):
        if EntityTuple is None:
            print("Entity tuple is None")
        else:
            self.id = EntityTuple[EntityObjEnum.ENTITY_ID.value]
            self.name = EntityTuple[EntityObjEnum.ENTITY_NAME.value]
            self.street_name = EntityTuple[EntityObjEnum.STREET_NAME.value]
            self.street_number = EntityTuple[EntityObjEnum.STREET_NUMBER.value]
            self.city = EntityTuple[EntityObjEnum.CITY.value]
            self.state = EntityTuple[EntityObjEnum.STATE.value]
            self.zip = EntityTuple[EntityObjEnum.ZIP.value]
            self.country = EntityTuple[EntityObjEnum.COUNTRY.value]
            self.is_active = EntityTuple[EntityObjEnum.IS_ACTIVE.value]

