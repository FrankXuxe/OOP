class Project:
    def __init__(self, id, desc, cons, date):
        self.__projID = id
        self.__projDesc = desc
        self.__consultants = cons
        self.__dueDate = date

    def get_projID(self):
        return self.__projID

    def get_projDesc(self):
        return self.__projDesc

    def get_consultants(self):
        return self.__consultants

    def get_duedate(self):
        return self.__dueDate
