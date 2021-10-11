

class Item:

    def __int__(self, des, unit, pri):
        self.__description = des
        self.__unit_inventory = unit
        self.__price = pri

    def set_description(self, des):
        self.__description = des

    def set_unit(self, unit):
        self.__unit_inventory = unit
        
    def set_price(self,pri):
        self.__price = pri

    def get_description(self):
        return self.__description

    def get_unit(self):
        return self.__unit_inventory

    def get_price(self):
        return self.__price
