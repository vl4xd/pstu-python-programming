from bulls_cows.bulls_cows import SumBullsCowsWrongs, GetRandomGoal, CountBullsAndCows, IsGameFinished
from bulls_cows.messages import MsgMainMenu, MsgDifficultyMenu, MsgCommon, MsgGame

def GetBullsCowsMainMenu() -> None:

    start = 0
    end = 3

    while True:
        choice: int = _MenuChoiсe(start, end, MsgMainMenu.Welcome())
        match choice:
            case 0:
                return
            case 1:
                _GetDifficultyMenu()
            case 2:
                _GetRulesMenu()
            case 3:
                pass


def _GetDifficultyMenu():

    start = 0
    end = 3

    while True:
        choice: int = _MenuChoiсe(start, end, MsgDifficultyMenu.SelectDifficulty())
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
            if not _GetGameMenu(difficalty):
                break


def _GetRulesMenu():

    start = 0
    end = 0

    while True:
        choice: int = _MenuChoiсe(start, end, MsgMainMenu.Rules())
        if choice == 0:
            return


def _GetGameMenu(length: int) -> bool:

    sum_bcw = SumBullsCowsWrongs()
    goal: int = GetRandomGoal(length)
    print(goal)
    while not IsGameFinished(sum_bcw):
        guess: int = _CheckUserGuess(length, MsgGame.GuessAtempt())
        if guess == 0:
            return False
        sum_bcw = CountBullsAndCows(length, guess, goal)
        if IsGameFinished(sum_bcw):
            continue
        print(MsgGame.StatAmongGuesses(sum_bcw.bulls, sum_bcw.cows, sum_bcw.wrongs))
    else:
        print(MsgGame.Congratulations(length, goal, 1))
        choice: int = _MenuChoiсe(0, 1, MsgGame.Restart())
        if choice == 1:
            return True
        return False


def _CheckUserGuess(length: int, msg: object) -> int:
    while True:
        guess_input: str = input(msg)
        try:
            guess_int = int(guess_input)
            if guess_int == 0:
                return guess_int
            if len(guess_input) != length or guess_int < 0:
                raise ValueError
            return guess_int
        except ValueError:
            print(MsgGame.IncorrectGuess(length))


def _MenuChoiсe(start: int, end: int, msg_menu: object) -> int:
    while True:
        choise_input: str = input(msg_menu)
        try:
            choise_int = int(choise_input)
            if choise_int < start or choise_int > end:
                raise ValueError
            return choise_int
        except ValueError:
            print(MsgCommon.IncorrectChoiсe(choise_input))