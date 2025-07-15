from domain.game import Game
from repository.repo_games import GamesRepository


class RepoTester:

    @staticmethod
    def __testAddDelete():
        repo = GamesRepository("date_teste.txt")
        assert len(repo.getAllGames()) == 4
        repo.addGame(Game("g",["g","gg"],80,"g"))
        assert len(repo.getAllGames()) == 5
        try:
            repo.addGame(Game("a",["aaa"],89,"aaa"))
            assert False
        except ValueError:
            assert len(repo.getAllGames()) == 5
        repo.deleteGame("g")
        assert len(repo.getAllGames()) == 4
        try:
            repo.deleteGame("g")
            assert False
        except ValueError:
            assert len(repo.getAllGames()) == 4

    @staticmethod
    def __testModify():
        repo = GamesRepository("date_teste.txt")
        repo.modifyGame("c",Game("c",["A","B"],100,"C"))
        assert repo.getGame("c").get_name() == "c"
        assert repo.getGame("c").get_type() == ["A","B"]
        assert repo.getGame("c").get_rating() == 100
        assert repo.getGame("c").get_status() == "C"
        repo.modifyGame("c",Game("c",["A","B","C"],8,"c"))
        try:
            repo.modifyGame("ccccc",Game("ccccc",["A","B"],8,"c"))
            assert False
        except ValueError:
            assert True

    @staticmethod
    def __testGetters():
        repo = GamesRepository("date_teste.txt")
        game = repo.getGame("a")
        assert game.get_type() == ["A"]
        assert game.get_rating() == 1
        assert game.get_status() == "a"
        lst = repo.getAllGames()
        assert len(lst) == 4
        assert lst[2].get_type() == ["A","B","C"]
        assert lst[3].get_rating() == 90

    @staticmethod
    def testAllRepo():
        RepoTester.__testGetters()
        RepoTester.__testAddDelete()
        RepoTester.__testModify()