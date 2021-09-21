class RetailItem:

    def __init__(self, des, unit, price):
        self.__description = des
        self.__units = unit
        self.__price = price

    def get_description(self):
        return self.__description

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price


