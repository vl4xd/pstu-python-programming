from bulls_cows.bulls_cows import SumBullsCowsWrongs, get_random_goal, count_bulls_and_cows, is_game_finished
from bulls_cows.messages import MsgMainMenu, MsgDifficultyMenu, MsgGame
from bulls_cows.stats import init_common_stats, add_common_stats
from common.common import menu_choiсe


def get_bulls_cows_main_menu() -> None:

    start = 0
    end = 3

    common_stats = init_common_stats()

    while True:
        choice: int = menu_choiсe(start, end, MsgMainMenu.welcome())
        match choice:
            case 0:
                return
            case 1:
                _get_difficulty_menu(common_stats)
            case 2:
                _get_rules_menu()
            case 3:
                _get_stats_menu(common_stats)


def _get_difficulty_menu(common_stats: dict[str:float | None]):

    start = 0
    end = 3

    while True:
        choice: int = menu_choiсe(start, end, MsgDifficultyMenu.select_difficulty())
        difficalty: int
        match choice:
            case 0:
                return
            case 1:
                difficalty = 3
            case 2:
                difficalty = 4
            case 3:
                difficalty = 5

        while True:
            if not _get_game_menu(difficalty, common_stats):
                break


def _get_rules_menu():

    start = 0
    end = 0

    while True:
        choice: int = menu_choiсe(start, end, MsgMainMenu.rules())
        if choice == 0:
            return

def _get_stats_menu(common_stats: dict[str:float | None]):

    start = 0
    end = 0

    while True:
        choice: int = menu_choiсe(start, end, MsgMainMenu.stats(common_stats))
        if choice == 0:
            return


def _get_game_menu(length: int, common_stats: dict[str:float | None]) -> bool:

    sum_bcw = SumBullsCowsWrongs()
    goal: int = get_random_goal(length)

    count_attempt: int = 0

    print(f"*Подсказка - {goal}*")

    while not is_game_finished(sum_bcw):
        guess: int = _check_user_guess(length, MsgGame.guess_attempt())
        if guess == 0:
            return False
        sum_bcw = count_bulls_and_cows(guess, goal)
        count_attempt += 1
        if is_game_finished(sum_bcw):
            continue
        print(MsgGame.stat_among_guesses(sum_bcw.bulls, sum_bcw.cows, sum_bcw.wrongs))
    else:
        print(MsgGame.congratulations(length, goal, count_attempt))
        add_common_stats(common_stats, count_attempt, length)
        choice: int = menu_choiсe(0, 1, MsgGame.restart())
        if choice == 1:
            return True
        return False


def _check_user_guess(length: int, msg: object) -> int:
    while True:
        guess_input: str = input(msg)
        try:
            guess_int = int(guess_input)
            if guess_int == 0:
                return guess_int
            if len(str(guess_int)) != length or guess_int < 0:
                raise ValueError
            return guess_int
        except ValueError:
            print(MsgGame.incorrect_guess(length, guess_int))
