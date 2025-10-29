import random


GAME_UNITS: dict[int:str] = {
    1: 'Ножницы',
    2: 'Бумага',
    3: 'Камень',
    4: 'Ящерица',
    5: 'Спок'
}

def IsLeftBeatsRight(left: int, right: int) -> tuple[bool, str]:
    win_status: bool
    msg: str
    match (left, right):
        case (1, 2) | (1, 4):
            win_status = True
        case (2, 3) | (2, 5):
            win_status = True
        case (3, 1) | (3, 4):
            win_status = True
        case (4, 2) | (4, 5):
            win_status = True
        case (5, 1) | (5, 3):
            win_status = True
        case _:
            win_status = False

    if win_status:
        msg = f'{GAME_UNITS[left]} бьет(ют) {GAME_UNITS[right]}'
    else:
        msg = f'{GAME_UNITS[right]} бьет(ют) {GAME_UNITS[left]}'

    return win_status, msg

def IsGameFinished(win_rate: int, player_wins: int, computer_wins: int) -> bool:
    win_condition: int = (win_rate // 2) + 1
    if player_wins >= win_condition or computer_wins >= win_condition:
        return True
    return False


def GetRandomGameUnit() -> int:
    random_unit: int = random.randint(1, 5)
    return random_unit


def GetGameUnitName(unit_key: int) -> str:
    return GAME_UNITS[unit_key]


def GetListKeysGameUnits() -> list[int]:
    return list(GAME_UNITS.keys())


def GetStringGameUnits() -> str:
    string = ''
    for key, value in GAME_UNITS.items():
        string += f'[{key}] - {value}\n'

    return string