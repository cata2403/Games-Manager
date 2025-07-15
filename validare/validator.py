from domain.game import Game


class Validator:
    def __init__(self):
        self.__max_len = 3
        self.__max_r_len = 100

    def __validateName(self, name:str):
        if ',' in name or '.' in name:
            return False
        return True

    def __validateTypes(self, types:list):
        if len(types) == 0:
            return False
        if len(types) > self.__max_len:
            return False
        return True

    def __validateRating(self, rating:int):
        if rating < 0 or rating > self.__max_r_len:
            return False
        return True

    def validateGame(self, game:Game):
        if self.__validateName(game.get_name()) == False:
            raise ValueError("Name cannot contain comma (',') or point ('.')")
        if self.__validateRating(game.get_rating()) == False:
            raise ValueError("Rating must be between 0 and " + str(self.__max_r_len))
        if self.__validateTypes(game.get_type()) == False:
            raise ValueError("Min 1 type, max ", self.__max_r_len, " types")