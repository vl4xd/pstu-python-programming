from abc import ABC, abstractmethod

from bulls_cows.bulls_cows import AddPrefixZero


class MsgCommon(ABC):

    @abstractmethod
    def IncorrectChoiсe(choiсe_input: str) -> str:
        string = f"""
Некорректный выбор ({choiсe_input})! Введите цифру - пункт меню, отмеченный в [.]."""

        return string


class MsgMainMenu(ABC):

    @abstractmethod
    def Welcome() -> str:
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
    def Rules() -> str:
        string = """
                Правила:

Компьютер загадывает число из n уникальных цифр.
Вы пытаетесь его угадать, предлагая свои варианты.

- Корова — цифра угадана и стоит на правильной позиции.
- Бык — цифра угадана, но стоит на неправильной позиции.

[0] - Назад

: """
        return string


class MsgDifficultyMenu(ABC):

    @abstractmethod
    def SelectDifficulty() -> str:
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
    def IncorrectGuess(length: int) -> str:
        string = f"""
Некорретный ввод! Ваш вариант должна быть ЦЕЛЫМ ПОЛОЖИТЕЛЬНЫМ числом с {length} знаками."""

        return string

    @abstractmethod
    def GuessAtempt() -> str:
        string = """
Ваш вариант (Для выхода ввидете цифру 0): """

        return string

    @abstractmethod
    def StatAmongGuesses(bulls: int, cows: int, wrongs: int) -> str:
        string = f"""
Найдено {bulls} быков, {cows} коров и {wrongs} цифр нет в числе."""

        return string

    @abstractmethod
    def Congratulations(length: int, goal: int, count_guesses) -> str:

        goal_str = AddPrefixZero(length, goal)
        string = f"""
Вы угадали число {goal_str} за {count_guesses} попыток."""

        return string

    @abstractmethod
    def Restart() -> str:
        string = """
Хотите сыграть еще?
[1] - Да
[0] - Нет

: """
        return string