class Game:
    def __init__(self, name, type, rating, status):
        self.__name = name
        self.__type = type
        self.__rating = rating
        self.__status = status

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_rating(self):
        return self.__rating

    def get_status(self):
        return self.__status

    def set_name(self, name):
        self.__name = name

    def set_type(self, type):
        self.__type = type

    def set_rating(self, rating):
        self.__rating = rating

    def set_status(self, status):
        self.__status = status