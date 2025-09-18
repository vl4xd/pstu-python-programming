from bulls_cows.messages import MsgMainMenu, MsgDifficultyMenu, MsgCommon

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
                pass
            case 3:
                pass


def _GetDifficultyMenu():

    start = 0
    end = 3

    while True:
        choice: int = _MenuChoiсe(start, end, MsgDifficultyMenu.SelectDifficulty())

        match choice:
            case 0:
                return
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass


def _GetGameMenu() -> int:
    pass

def _MenuChoiсe(start: int, end: int, msg_menu: object) -> int:
    while True:
        choise_input: str = input(msg_menu)
        try:
            choise_int = int(choise_input)
            if choise_int < start or choise_int > end:
                raise ValueError
            return choise_int
        except ValueError:
            print(MsgCommon.IncorrentChoiсe(choise_input))