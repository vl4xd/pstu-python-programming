import re

from wordle.wordle import Wordle
from wordle.messages import MsgMainMenu, MsgGame
from common.common import MenuChoiсe


def GetWordleMainMenu() -> None:

    start = 0
    end = 2

    while True:
        choice: int = MenuChoiсe(start, end, MsgMainMenu.Welcome())
        match choice:
            case 0:
                return
            case 1:
                while True:
                    if not _GetGameMenu():
                        break
            case 2:
                _GetRulesMenu()


def _GetGameMenu() -> bool:

    worlde = Wordle()
    print(MsgGame.StartGame())
    print(f"*Подсказка - {worlde.goal}*")
    while not worlde.is_finished:

        guess: str = _CheckUserWord(worlde.length, MsgGame.GuessAttempt(worlde.count_attempts))

        try:
            guess = int(guess)
            if guess == 0:
                return False
        except ValueError:
            pass

        checked_guess = worlde.CheckWord(guess)
        print(MsgGame.StatAmongGuesses(checked_guess))
        if worlde.is_finished:
            continue
    else:
        if worlde.is_word_guessed:
            print(MsgGame.Congratulations(worlde.goal, worlde.count_attempts))
        else:
            print(MsgGame.Сondolence(worlde.goal, worlde.count_attempts))

        choice: int = MenuChoiсe(0, 1, MsgGame.Restart())
        if choice == 1:
            return True
        return False


def _GetRulesMenu():

    start = 0
    end = 0

    while True:
        choice: int = MenuChoiсe(start, end, MsgMainMenu.Rules())
        if choice == 0:
            return


def _CheckUserWord(length: int, msg: object) -> str:
    pattern = rf'^([а-яёА-ЯЁ]{{{length}}}|0)$'

    while True:
        guess_input: str = input(msg)
        try:
            if not re.match(pattern, guess_input):
                raise ValueError
            return guess_input
        except ValueError:
            print(MsgGame.IncorrectGuess(length))