from number_analyzer.number_analyzer import FindDivisors
from number_analyzer.messages import MsgMainMenu, MsgAnalyzer
from common.common import MenuChoiсe

def GetNumberAnalyzerMainMenu() -> None:

    start = 0
    end = 2

    while True:
        choice: int = MenuChoiсe(start, end, MsgMainMenu.Welcome())
        match choice:
            case 0:
                return
            case 1:
                _GetAnalyzerMenu()
            case 2:
                _GetAboutMenu()


def _GetAnalyzerMenu() -> None:

    while True:
        number: int = _CheckUserNumber(MsgAnalyzer.NumberAttempt())
        if number == 0:
            return
        divisors = FindDivisors(number)
        print(MsgAnalyzer.AnalyzedNumber(number, divisors))

        choice: int = MenuChoiсe(0, 1, MsgAnalyzer.Restart())
        if choice == 1:
            continue
        return


def _GetAboutMenu() -> None:
    start = 0
    end = 0

    while True:
        choice: int = MenuChoiсe(start, end, MsgMainMenu.About())
        if choice == 0:
            return


def _CheckUserNumber(msg: object) -> int:
    while True:
        number_input: str = input(msg)
        try:
            number_input = int(number_input)
            if number_input == 0:
                return number_input
            if number_input < 0:
                raise ValueError
            return number_input
        except ValueError:
            print(MsgAnalyzer.IncorrectNumber())
