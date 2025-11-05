from abc import ABC, abstractmethod

from bulls_cows.stats import get_common_stats_info

class MsgMainMenu(ABC):

    @abstractmethod
    def welcome() -> str:
        string = """
'Быки и Коровы'

Меню:
[1] - Начать игру
[2] - Правила
[3] - Статистика

[0] - Назад

: """
        return string

    @abstractmethod
    def rules() -> str:
        string = """
                Правила:

Компьютер загадывает число из n уникальных цифр.
Вы пытаетесь его угадать, предлагая свои варианты.

- Корова — цифра угадана и стоит на правильной позиции.
- Бык — цифра угадана, но стоит на неправильной позиции.

[0] - Назад

: """
        return string

    @abstractmethod
    def stats(common_stats: dict[str:float]) -> str:
        string = f"""
                Статистика за сессию:

{get_common_stats_info(common_stats)}
[0] - Назад

: """
        return string


class MsgDifficultyMenu(ABC):

    @abstractmethod
    def select_difficulty() -> str:
        string = """
Выберите сложность:
[1] - Легко (3 цифры)
[2] - Нормально (4 цифры)
[3] - Сложно (5 цифр)

[0] - Назад

: """
        return string


class MsgGame(ABC):


    @abstractmethod
    def incorrect_guess(length: int, guess: int) -> str:
        string = f"""
Некорректный ввод! Ваш вариант должен быть ЦЕЛЫМ ПОЛОЖИТЕЛЬНЫМ числом с {length} знаками (Ваш вариант: {guess})."""

        return string

    @abstractmethod
    def guess_attempt() -> str:
        string = """
Ваш вариант (для выхода ввидете цифру 0): """

        return string

    @abstractmethod
    def stat_among_guesses(bulls: int, cows: int, wrongs: int) -> str:
        string = f"""
Найдено {bulls} быков, {cows} коров и {wrongs} цифр(ы) нет в числе."""

        return string

    @abstractmethod
    def congratulations(length: int, goal: int, count_guesses) -> str:

        goal_str = str(goal)
        string = f"""
Вы угадали число {goal_str} за {count_guesses} попыток."""

        return string

    @abstractmethod
    def restart() -> str:
        string = """
Хотите сыграть еще?
[1] - Да
[0] - Нет

: """
        return string