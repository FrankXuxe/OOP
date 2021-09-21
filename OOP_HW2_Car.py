class Car:
    def __init__(self, y, m, s):
        self.__year_model = y
        self.__make = m
        self.__speed = 0
        

    def set_year_model(self,y):
        self.__year_model = y

    def set_make(self,m):
        self.__make = m

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make