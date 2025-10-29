from common.common import MenuChoiсe
from common.messages import MsgMainMenu
from bulls_cows.menu import GetBullsCowsMainMenu
from number_analyzer.menu import GetNumberAnalyzerMainMenu
from wordle.menu import GetWordleMainMenu
from rock_paper_scissors.menu import GetRockPaperScissorsMainMenu
from text_statistics.menu import GetTextStatisticsMainMenu

def GetMainMenu() -> None:
    start = 0
    end = 5

    while True:
        choice: int = MenuChoiсe(start, end, MsgMainMenu.Welcome())
        match choice:
            case 0:
                return
            case 1:
                GetBullsCowsMainMenu()
            case 2:
                GetNumberAnalyzerMainMenu()
            case 3:
                GetWordleMainMenu()
            case 4:
                GetRockPaperScissorsMainMenu()
            case 5:
                GetTextStatisticsMainMenu()