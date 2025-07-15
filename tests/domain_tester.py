from domain.game import Game

class DomainTester:

    @staticmethod
    def __testGetters():
        game = Game("joc",["rpg","shooter","mmo"],6,"ongoing")
        assert game.get_name() == "joc"
        assert game.get_type()[0] == "rpg"
        assert game.get_type()[1] == "shooter"
        assert game.get_type()[2] == "mmo"
        assert game.get_rating() == 6
        assert game.get_status() == "ongoing"

    @staticmethod
    def __testSetters():
        game = Game("a",["survival","coop"],9,"finished")
        game.set_name("Minecraft")
        game.set_type(game.get_type()+["rpg"])
        game.set_rating(game.get_rating()+1)
        game.set_status("ongoing")
        assert game.get_name() == "Minecraft"
        assert game.get_type()[0] == "survival"
        assert game.get_type()[1] == "coop"
        assert game.get_type()[2] == "rpg"
        assert game.get_rating() == 10
        assert game.get_status() == "ongoing"

    @staticmethod
    def testAllDomain():
        DomainTester.__testGetters()
        DomainTester.__testSetters()


