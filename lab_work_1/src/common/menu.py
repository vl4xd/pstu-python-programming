from common.common import menu_choiсe
from common.messages import MsgMainMenu
from bulls_cows.menu import get_bulls_cows_main_menu
from number_analyzer.menu import get_number_analyzer_main_menu
from wordle.menu import get_wordle_main_menu
from rock_paper_scissors.menu import get_rock_paper_scissors_main_menu
from text_statistics.menu import get_text_statistics_main_menu

def get_main_menu() -> None:
    start = 0
    end = 5

    while True:
        choice: int = menu_choiсe(start, end, MsgMainMenu.welcome())
        match choice:
            case 0:
                return
            case 1:
                get_bulls_cows_main_menu()
            case 2:
                get_number_analyzer_main_menu()
            case 3:
                get_wordle_main_menu()
            case 4:
                get_rock_paper_scissors_main_menu()
            case 5:
                get_text_statistics_main_menu()