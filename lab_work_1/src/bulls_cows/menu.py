from bulls_cows.bulls_cows import SumBullsCowsWrongs, GetRandomGoal, CountBullsAndCows, IsGameFinished
from bulls_cows.messages import MsgMainMenu, MsgDifficultyMenu, MsgGame
from bulls_cows.stats import init_common_stats, add_common_stats
from common.common import MenuChoiсe

def GetBullsCowsMainMenu() -> None:

    start = 0
    end = 3

    common_stats = init_common_stats()

    while True:
        choice: int = MenuChoiсe(start, end, MsgMainMenu.Welcome())
        match choice:
            case 0:
                return
            case 1:
                _GetDifficultyMenu(common_stats)
            case 2:
                _GetRulesMenu()
            case 3:
                _GetStatsMenu(common_stats)



def _GetDifficultyMenu(common_stats: dict[str:float | None]):

    start = 0
    end = 3

    while True:
        choice: int = MenuChoiсe(start, end, MsgDifficultyMenu.SelectDifficulty())
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
            if not _GetGameMenu(difficalty, common_stats):
                break


def _GetRulesMenu():

    start = 0
    end = 0

    while True:
        choice: int = MenuChoiсe(start, end, MsgMainMenu.Rules())
        if choice == 0:
            return

def _GetStatsMenu(common_stats: dict[str:float | None]):

    start = 0
    end = 0

    while True:
        choice: int = MenuChoiсe(start, end, MsgMainMenu.Stats(common_stats))
        if choice == 0:
            return


def _GetGameMenu(length: int, common_stats: dict[str:float | None]) -> bool:

    sum_bcw = SumBullsCowsWrongs()
    goal: int = GetRandomGoal(length)

    count_attempt: int = 0

    print(f"*Подсказка - {goal}*")

    while not IsGameFinished(sum_bcw):
        guess: int = _CheckUserGuess(length, MsgGame.GuessAttempt())
        if guess == 0:
            return False
        sum_bcw = CountBullsAndCows(guess, goal)
        count_attempt += 1
        if IsGameFinished(sum_bcw):
            continue
        print(MsgGame.StatAmongGuesses(sum_bcw.bulls, sum_bcw.cows, sum_bcw.wrongs))
    else:
        print(MsgGame.Congratulations(length, goal, count_attempt))
        add_common_stats(common_stats, count_attempt, length)
        choice: int = MenuChoiсe(0, 1, MsgGame.Restart())
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
            if len(str(guess_int)) != length or guess_int < 0:
                raise ValueError
            return guess_int
        except ValueError:
            print(MsgGame.IncorrectGuess(length, guess_int))
