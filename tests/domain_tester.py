from domain.game import Game

class DomainTester:

    def __testGetters(self):
        self.game = Game("joc",["rpg","shooter","mmo"],6,"ongoing")
        assert self.game.get_name() == "joc"
        assert self.game.get_type()[0] == "rpg"
        assert self.game.get_type()[1] == "shooter"
        assert self.game.get_type()[2] == "mmo"
        assert self.game.get_rating() == 6
        assert self.game.get_status() == "ongoing"

    def __testSetters(self):
        self.game = Game("a",["survival","coop"],9,"finished")
        self.game.set_name("Minecraft")
        self.game.set_type(self.game.get_type()+["rpg"])
        self.game.set_rating(self.game.get_rating()+1)
        self.game.set_status("ongoing")
        assert self.game.get_name() == "Minecraft"
        assert self.game.get_type()[0] == "survival"
        assert self.game.get_type()[1] == "coop"
        assert self.game.get_type()[2] == "rpg"
        assert self.game.get_rating() == 10
        assert self.game.get_status() == "ongoing"

    def testAllDomain(self):
        self.__testGetters()
        self.__testSetters()


