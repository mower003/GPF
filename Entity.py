import locale
from enum import Enum

class EntityObjEnum(Enum):
    ENTITY_ID = 0
    ENTITY_NAME = 1
    STREET_NUMBER = 2
    STREET_NAME = 3
    CITY = 4
    STATE = 5
    ZIP = 6
    COUNTRY = 7
    IS_ACTIVE = 8

class EntityObj:
    locale.setlocale(locale.LC_ALL, 'en_US')

    def __init__(self, id=-1, name='', street_number='', street_name='', city='', state='', zip='', country='', is_active=1, *, entityList=None):
        if entityList is None:
            self.id = id
            self.name = name
            self.street_name = street_name
            self.street_number = street_number
            self.city = city
            self.state = state
            self.zip = zip
            self.country = country
            self.is_active = is_active
        else:
            self.id = entityList[EntityObjEnum.ENTITY_ID.value]
            self.name = entityList[EntityObjEnum.ENTITY_NAME.value]
            self.street_number = entityList[EntityObjEnum.STREET_NUMBER.value]
            self.street_name = entityList[EntityObjEnum.STREET_NAME.value]
            self.city = entityList[EntityObjEnum.CITY.value]
            self.state = entityList[EntityObjEnum.STATE.value]
            self.zip = entityList[EntityObjEnum.ZIP.value]
            self.country = entityList[EntityObjEnum.COUNTRY.value]
            self.is_active = entityList[EntityObjEnum.IS_ACTIVE.value]

        print("######################Entity Object created######################"+'\n'+self.__repr__())

    def __repr__(self) -> str:
        entity_representation = '\n' + "Entity ID: " + str(self.id) + '\n' + "Name: " + str(self.name) + '\n' + "Street Number: " + str(self.street_number) + '\n' + "Street Name: " + str(self.street_name) + '\n' + "City: " + str(self.city) + '\n' + "State: " + str(self.state) + '\n' + "Zip Code: " + str(self.zip) + '\n' + "Country: " + str(self.country) + '\n' + "Is Active: " + str(self.is_active)
    
        return entity_representation

    def asList(self):
        list = []
        list.insert(EntityObjEnum.ENTITY_ID.value, self.id)
        list.insert(EntityObjEnum.ENTITY_NAME.value, self.name)
        list.insert(EntityObjEnum.STREET_NUMBER.value, self.street_number)
        list.insert(EntityObjEnum.STREET_NAME.value, self.street_name)
        list.insert(EntityObjEnum.CITY.value, self.city)
        list.insert(EntityObjEnum.STATE.value, self.state)
        list.insert(EntityObjEnum.ZIP.value, self.zip)
        list.insert(EntityObjEnum.COUNTRY.value, self.country)
        list.insert(EntityObjEnum.IS_ACTIVE.value, self.is_active)
        return list

    def asListForDBInsertion(self):
        list = []
        list.insert(EntityObjEnum.ENTITY_ID.value, self.id)
        list.insert(EntityObjEnum.ENTITY_NAME.value, self.name)
        list.insert(EntityObjEnum.STREET_NUMBER.value, self.street_number)
        list.insert(EntityObjEnum.STREET_NAME.value, self.street_name)
        list.insert(EntityObjEnum.CITY.value, self.city)
        list.insert(EntityObjEnum.STATE.value, self.state)
        list.insert(EntityObjEnum.ZIP.value, self.zip)
        list.insert(EntityObjEnum.COUNTRY.value, self.country)
        list.insert(EntityObjEnum.IS_ACTIVE.value, self.is_active)
        return list
    
    def asListForDBUpdate(self):
        list = []
        list.append(self.name)
        list.append(self.street_number)
        list.append(self.street_name)
        list.append(self.city)
        list.append(self.state)
        list.append(self.zip)
        list.append(self.country)
        list.append(self.is_active)
        list.append(self.id)
        return list

    def toString(self):
        return_str = str(self.id) + " " + self.name + " " + self.street_number + " " + self.street_name + " " + self.city + " " + self.state + " " + self.zip + " " + self.country
        return return_str

    def getAsAddressString(self):
        #print(str(self.street_number) + " " + str(self.street_name) + " " + str(self.city) + " " + str(self.state) + " " + str(self.zip) + " " + str(self.country))
        return_str = str(self.street_number) + " " + self.street_name + " " + self.city + ", " + self.state + " " + str(self.zip) + " " + self.country
        return return_str

    def getAsCustomerWidgetDisplay(self):
        return_str = self.name + "\n" + str(self.street_number) + " " + self.street_name + " " + self.city + " " + self.state + " " + str(self.zip) + " " + self.country
        return return_str

    def addEntityAsTuple(self, EntityTuple=None):
        if EntityTuple is None:
            print("Entity tuple is None")
        else:
            self.id = EntityTuple[EntityObjEnum.ENTITY_ID.value]
            self.name = EntityTuple[EntityObjEnum.ENTITY_NAME.value]
            self.street_number = EntityTuple[EntityObjEnum.STREET_NUMBER.value]
            self.street_name = EntityTuple[EntityObjEnum.STREET_NAME.value]
            self.city = EntityTuple[EntityObjEnum.CITY.value]
            self.state = EntityTuple[EntityObjEnum.STATE.value]
            self.zip = EntityTuple[EntityObjEnum.ZIP.value]
            self.country = EntityTuple[EntityObjEnum.COUNTRY.value]
            self.is_active = EntityTuple[EntityObjEnum.IS_ACTIVE.value]

    def getName(self):
        return str(self.name)

    def getID(self):
        return self.id

    def getStreetName(self):
        return self.street_name

    def getStreetNumber(self):
        return self.street_number

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getIsActive(self):
        return self.is_active

    def getCountry(self):
        return self.country

    def getZip(self):
        return self.zip
