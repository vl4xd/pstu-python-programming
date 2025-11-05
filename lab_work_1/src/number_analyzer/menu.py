from number_analyzer.number_analyzer import find_divisors
from number_analyzer.messages import MsgMainMenu, MsgAnalyzer
from common.common import menu_choiсe


def get_number_analyzer_main_menu() -> None:

    start = 0
    end = 2

    while True:
        choice: int = menu_choiсe(start, end, MsgMainMenu.welcome())
        match choice:
            case 0:
                return
            case 1:
                _get_analyzer_menu()
            case 2:
                _get_about_menu()


def _get_analyzer_menu() -> None:

    while True:
        number: int = _check_user_number(MsgAnalyzer.number_attempt())
        if number == 0:
            return
        divisors = find_divisors(number)
        print(MsgAnalyzer.analyzed_number(number, divisors))

        choice: int = menu_choiсe(0, 1, MsgAnalyzer.restart())
        if choice == 1:
            continue
        return


def _get_about_menu() -> None:
    start = 0
    end = 0

    while True:
        choice: int = menu_choiсe(start, end, MsgMainMenu.about())
        if choice == 0:
            return


def _check_user_number(msg: object) -> int:
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
            print(MsgAnalyzer.incorrect_number())
