import json

from domain.game import Game


class GamesRepository:
    def __init__(self, f):
        self.__file = f
        self.__game_data = {}
        self.__loadFromFile()

    def __exit__(self):
        self.__saveToFile()

    def __saveToFile(self):
        with open(self.__file, 'w') as f:
            for game in self.__game_data.values():
                line = str(game.get_name()) + "|" + str(game.get_type()) + "|" + str(game.get_rating()) + "|" + str(game.get_status()) + "\n"
                f.write(line)


    def __loadFromFile(self):
        with open(self.__file, 'r') as f:
            self.__game_data = {}
            for line in f:
                line = line.strip()
                name, typ, rating, status = line.split("|")
                name = name.strip()
                typ = typ.strip()
                rating = int(rating.strip())
                status = status.strip()
                self.__game_data[name] = Game(name, typ, rating, status)

    def addGame(self, game):
        if game.get_name() in self.__game_data:
            raise ValueError("Game with name [" + str(game.get_name()) + "] already exists")
        self.__game_data[game.get_name()] = game
        self.__saveToFile()

    def deleteGame(self, name):
        if name not in self.__game_data:
            raise ValueError("Game with name [" + str(name) + "] does not exist")
        self.__game_data.pop(name)
        self.__saveToFile()

    def modifyGame(self, name, new_game):
        if name not in self.__game_data:
            raise ValueError("Game with name [" + str(name) + "] does not exist")
        self.__game_data[name] = new_game
        self.__saveToFile()

    def getAllGames(self):
        return list(self.__game_data.values())

    def getGame(self, name):
        if name not in self.__game_data:
            raise ValueError("Game with name [" + str(name) + "] does not exist")
        return self.__game_data[name]