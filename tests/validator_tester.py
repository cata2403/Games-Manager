from domain.game import Game
from validare.validator import Validator


class ValidatorTester:

    @staticmethod
    def __testGameValidator():
        val = Validator()
        g1 = Game("a","a",0,"a")
        g2 = Game("b","",1,"b")
        g3 = Game("c","c,c,c,c",1,"c")
        g4 = Game("d.d","d,d,d",1,"d")
        g5 = Game("e,eee","e,e",1,"e")
        g6 = Game("f","f,f,f",-123,"f")
        g7 = Game("g","g,g,g",101,"g")
        try:
            val.validateGame(g1)
            assert True
        except ValueError:
            assert False
        try:
            val.validateGame(g2)
            assert False
        except ValueError:
            assert True
        try:
            val.validateGame(g3)
            assert True
        except ValueError:
            assert False
        try:
            val.validateGame(g4)
            assert True
        except ValueError:
            assert False
        try:
            val.validateGame(g5)
            assert True
        except ValueError:
            assert False
        try:
            val.validateGame(g6)
            assert False
        except ValueError:
            assert True
        try:
            val.validateGame(g7)
            assert False
        except ValueError:
            assert True

    @staticmethod
    def testAllValidator():
        ValidatorTester.__testGameValidator()