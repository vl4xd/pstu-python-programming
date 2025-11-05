from abc import ABC, abstractmethod

from rock_paper_scissors.rock_paper_scissors import get_string_game_units

class MsgMainMenu(ABC):

    @abstractmethod
    def welcome() -> str:
        string = """
'Камень-Ножницы-Бумага-Ящерица-Спок'

Меню:
[1] - Начать игру
[2] - Парвила

[0] - Назад

: """
        return string

    @abstractmethod
    def rules() -> str:
        string = """
                Правила:

Расширенная версия игры "Камень-Ножницы-Бумага".
- Ножницы режут бумагу.
- Бумага накрывает камень.
- Камень давит ящерицу.
- Ящерица травит Спока.
- Спок ломает ножницы.
- Ножницы убивают ящерицу.
- Ящерица ест бумагу.
- Бумага подставляет Спока.
- Спок испаряет камень.
- Камень затупляет ножницы.
Выбор компьютера делается случайно.

[0] - Назад

: """
        return string


class MsgWinRateMenu(ABC):

    @abstractmethod
    def select_win_rate() -> str:
        string = """
Введите желаемое количество побед от [1] до [10]

[0] - Назад

: """
        return string


class MsgGame(ABC):


    @abstractmethod
    def incorrect_guess() -> str:
        string = """
Некорретный ввод! Выберите пункт, отмеченный в [.]"""

        return string


    @abstractmethod
    def stat_among_guesses(player_wins: int, computer_wins: int, is_plaer_win: bool, is_draw: bool) -> str:
        who_win: str
        if is_draw:
            who_win = "Ничья!"
        elif is_plaer_win:
            who_win = "Вы победили!"
        else:
            who_win = "Победил компьютер!"

        string = f"""
{who_win}
Счет: Вы - {player_wins}, Компьютер - {computer_wins}."""

        return string

    @abstractmethod
    def congratulations(player_wins: int, computer_wins: int) -> str:
        who_win: str
        if player_wins == computer_wins:
            who_win = "В этой игре ничья!"
        elif player_wins > computer_wins:
            who_win = "В этой игре победили Вы!"
        else:
            who_win = "В этой игре победил компьютер!"


        string = f"""
{who_win}
Общий счет: Вы - {player_wins}, Компьютер - {computer_wins}."""

        return string


    @abstractmethod
    def guess_attempt(count_moves: int) -> str:
        string = f"""
Ход №{count_moves}. Выберите один из вариантов:
{get_string_game_units()}
Ваш вариант (для выхода введите цифру 0): """

        return string

    @abstractmethod
    def restart() -> str:
        string = """
Хотите сыграть еще?
[1] - Да
[0] - Нет

: """
        return string