import re

from wordle.wordle import Wordle
from wordle.messages import MsgMainMenu, MsgGame
from common.common import menu_choiсe


def get_wordle_main_menu() -> None:

    start = 0
    end = 2

    while True:
        choice: int = menu_choiсe(start, end, MsgMainMenu.welcome())
        match choice:
            case 0:
                return
            case 1:
                while True:
                    if not _get_game_menu():
                        break
            case 2:
                _get_rules_menu()


def _get_game_menu() -> bool:

    worlde = Wordle()
    print(MsgGame.start_game())
    print(f"*Подсказка - {worlde.goal}*")
    while not worlde.is_finished:

        guess: str = _check_user_word(worlde.length, MsgGame.guess_attempt(worlde.count_attempts))

        try:
            guess = int(guess)
            if guess == 0:
                return False
        except ValueError:
            pass

        checked_guess = worlde.check_word(guess)
        print(MsgGame.stat_among_guesses(checked_guess))
        if worlde.is_finished:
            continue
    else:
        if worlde.is_word_guessed:
            print(MsgGame.congratulations(worlde.goal, worlde.count_attempts))
        else:
            print(MsgGame.failure(worlde.goal, worlde.count_attempts))

        choice: int = menu_choiсe(0, 1, MsgGame.restart())
        if choice == 1:
            return True
        return False


def _get_rules_menu():

    start = 0
    end = 0

    while True:
        choice: int = menu_choiсe(start, end, MsgMainMenu.rules())
        if choice == 0:
            return


def _check_user_word(length: int, msg: object) -> str:
    pattern = rf'^([а-яёА-ЯЁ]{{{length}}}|0)$'

    while True:
        guess_input: str = input(msg)
        try:
            if not re.match(pattern, guess_input):
                raise ValueError
            return guess_input
        except ValueError:
            print(MsgGame.incorrect_guess(length))