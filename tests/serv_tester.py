from repository.repo_games import GamesRepository
from service.serv import GameService
from validare.validator import Validator


class ServTester:

    @staticmethod
    def __testAddDel():
        val = Validator()
        repo = GamesRepository("date_teste.txt")
        serv = GameService(repo,val)
        assert len(serv.getAllGames()) == 4
        serv.addGame("v",["v","v"],78,"v")
        assert len(serv.getAllGames()) == 5
        assert serv.getGame("v").get_type() == ["v","v"]
        serv.deleteGame("v")
        assert len(serv.getAllGames()) == 4

    @staticmethod
    def __testMod():
        val = Validator()
        repo = GamesRepository("date_teste.txt")
        serv = GameService(repo, val)
        serv.modifyGame("d",["A"],0,"D")
        assert serv.getGame("d").get_type() == ["A"]
        assert serv.getGame("d").get_rating() == 0
        assert serv.getGame("d").get_status() == "D"
        serv.modifyGame("d",["A","D","C"],90,"d")

    @staticmethod
    def __testGetters():
        val = Validator()
        repo = GamesRepository("date_teste.txt")
        serv = GameService(repo, val)
        assert serv.getGame("d").get_rating() == 90
        assert serv.getGame("b").get_type() == ["A","B"]
        lst = serv.getAllGames()
        assert len(lst) == 4
        assert lst[0].get_name() == "a"
        assert lst[2].get_status() == "c"

    @staticmethod
    def __testFilter():
        val = Validator()
        repo = GamesRepository("date_teste.txt")
        serv = GameService(repo, val)
        lst = serv.filterByName("a")
        assert len(lst) == 1
        assert lst[0].get_type() == ["A"]
        serv.addGame("bbb",["F"],23,"b")
        lst = serv.filterByName("b")
        assert len(lst) == 2
        assert lst[0].get_name() == "b"
        assert lst[1].get_type() == ["F"]
        serv.deleteGame("bbb")

    @staticmethod
    def testAllServ():
        ServTester.__testGetters()
        ServTester.__testAddDel()
        ServTester.__testMod()
        ServTester.__testFilter()