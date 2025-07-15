from domain.game import Game
from repository.repo_games import GamesRepository
from validare.validator import Validator


class GameService:
    def __init__(self, repo:GamesRepository, val:Validator):
        self.__repo = repo
        self.__val = val

    def addGame(self, name, type, rating, status):
        game = Game(name, type, rating, status)
        self.__val.validateGame(game)
        self.__repo.addGame(game)

    def deleteGame(self, name):
        self.__repo.deleteGame(name)

    def modifyGame(self, name, new_type, new_rating, new_status):
        game = Game(name, new_type, new_rating, new_status)
        self.__val.validateGame(game)
        self.__repo.modifyGame(name,game)

    def filterByName(self, mask):
        list = self.__repo.getAllGames()
        filtered = []
        for game in list:
            if mask in game.get_name():
                filtered.append(game)
        return filtered

    def getAllGames(self):
        return self.__repo.getAllGames()

    def getGame(self, name):
        return self.__repo.getGame(name)

