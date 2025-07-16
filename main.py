from repository.repo_games import GamesRepository
from service.serv import GameService
from tests.domain_tester import DomainTester
from tests.repo_tester import RepoTester
from tests.serv_tester import ServTester
from tests.validator_tester import ValidatorTester
from validare.validator import Validator
from gui.gui import mainwindow


def runAllTests():
    DomainTester.testAllDomain()
    RepoTester.testAllRepo()
    ValidatorTester.testAllValidator()
    ServTester.testAllServ()

runAllTests()
repo = GamesRepository("game_data.csv")
val = Validator()
serv = GameService(repo,val)
mainwindow(serv)

