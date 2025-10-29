from common.common import MenuChoiсe
from rock_paper_scissors.messages import MsgMainMenu, MsgWinRateMenu, MsgGame
from rock_paper_scissors.rock_paper_scissors import GetRandomGameUnit, IsLeftBeatsRight, GetListKeysGameUnits, GetGameUnitName, IsGameFinished

def GetRockPaperScissorsMainMenu() -> None:

    start = 0
    end = 2

    while True:
        choice: int = MenuChoiсe(start, end, MsgMainMenu.Welcome())
        match choice:
            case 0:
                return
            case 1:
                _GetWinRateMenu()
            case 2:
                _GetRulesMenu()


def _GetWinRateMenu():

    start = 0
    end = 10

    while True:
        choice: int = MenuChoiсe(start, end, MsgWinRateMenu.SelectWinRate())
        if choice == 0:
            return

        while True:
            if not _GetGameMenu(choice):
                break


def _GetRulesMenu():

    start = 0
    end = 0

    while True:
        choice: int = MenuChoiсe(start, end, MsgMainMenu.Rules())
        if choice == 0:
            return


def _GetGameMenu(win_rate: int) -> bool:

    computer_wins: int = 0
    player_wins: int = 0
    count_moves: int = 0

    while not IsGameFinished(win_rate, player_wins, computer_wins):
        count_moves += 1
        is_player_win: bool = False
        is_draw: bool = False

        computer_choice: int = GetRandomGameUnit()
        print(f"*Подсказка - {GetGameUnitName(computer_choice)}*")

        guess: int = _CheckUserGuess(MsgGame.GuessAttempt(count_moves))
        if guess == 0:
            return False

        if guess == computer_choice:
            player_wins += 1
            computer_wins += 1
            is_draw = True
        else:
            win_status, msg_status = IsLeftBeatsRight(guess, computer_choice)
            print(msg_status)
            if win_status:
                player_wins += 1
                is_player_win = True
            else:
                computer_wins += 1

        if IsGameFinished(win_rate, player_wins, computer_wins):
            continue

        print(MsgGame.StatAmongGuesses(player_wins, computer_wins, is_player_win, is_draw))
    else:
        print(MsgGame.Congratulations(player_wins, computer_wins))
        choice: int = MenuChoiсe(0, 1, MsgGame.Restart())
        if choice == 1:
            return True
        return False


def _CheckUserGuess(msg: object) -> int:
    while True:
        guess_input: str = input(msg)
        try:
            guess_int = int(guess_input)
            if guess_int == 0:
                return guess_int
            if guess_int not in GetListKeysGameUnits():
                raise ValueError
            return guess_int
        except ValueError:
            print(MsgGame.IncorrectGuess())