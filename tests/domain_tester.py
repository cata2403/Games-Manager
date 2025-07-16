from domain.game import Game

class DomainTester:

    @staticmethod
    def __testGetters():
        game = Game("joc","rpg,shooter,mmo",6,"ongoing")
        assert game.get_name() == "joc"
        assert game.get_type() == "rpg,shooter,mmo"
        assert game.get_rating() == 6
        assert game.get_status() == "ongoing"

    @staticmethod
    def __testSetters():
        game = Game("a","survival,coop",9,"finished")
        game.set_name("Minecraft")
        game.set_type(game.get_type() + ",rpg")
        game.set_rating(game.get_rating() + 1)
        game.set_status("ongoing")
        assert game.get_name() == "Minecraft"
        assert game.get_type() == "survival,coop,rpg"
        assert game.get_rating() == 10
        assert game.get_status() == "ongoing"

    @staticmethod
    def testAllDomain():
        DomainTester.__testGetters()
        DomainTester.__testSetters()


