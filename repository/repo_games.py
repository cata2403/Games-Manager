from domain.game import Game


class GamesRepository:
    def __init__(self, f):
        self.__file = f
        self.__game_data = {}
        self.__loadFromFile()

    def __del__(self):
        self.__saveToFile()

    def __saveToFile(self):
        with open(self.__file, 'w') as f:
            for game in self.__game_data:
                line = str(game.get_name())
                line += ","
                for types in game.get_type():
                    line += str(types)
                    line += "."
                line += str(game.get_rating())
                line += str(game.get_status())
                line += "\n"
                f.write(line)


    def __loadFromFile(self):
        with open(self.__file, 'r') as f:
            for line in f:
                line = line.strip()
                name, type, rating, status = line.split(",")
                name = name.strip()
                type = type.strip()
                type = type.split(".")
                rating = int(rating.strip())
                status = status.strip()
                self.__game_data[name] = Game(name, type, rating, status)

    def addGame(self, game):
        if game.get_name() in self.__game_data:
            raise ValueError("Game with name [" + str(game.get_name()) + "] already exists")
        self.__game_data[game.get_name()] = game

    def deleteGame(self, name):
        if name not in self.__game_data:
            raise ValueError("Game with name [" + str(name) + "] does not exist")
        self.__game_data.pop(name)

    def modifyGame(self, name, new_game):
        if name not in self.__game_data:
            raise ValueError("Game with name [" + str(name) + "] does not exist")
        self.__game_data[name] = new_game

    def getAllGames(self):
        return list(self.__game_data.values())

    def getGame(self, name):
        return self.__game_data[name]