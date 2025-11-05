from abc import ABC, abstractmethod

class MsgMainMenu(ABC):

    @abstractmethod
    def welcome() -> str:
        string = """
'Wordle/5 букв'

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

Компьютер загадывает слово из 5 букв.
У Вас есть 6 попыток его угадать.
После каждой попытки программа дает обратную связь:

- Буква угадана и стоит на правильном месте — выделяется [X] .
- Буква есть в слове, но стоит на другом месте — выделяется (X) .
- Буквы нет в слове — она остается без изменений.

[0] - Назад

: """
        return string

class MsgGame(ABC):


    @abstractmethod
    def incorrect_guess(length: int) -> str:
        string = f"""
Некорретный ввод! Ваш вариант должнен быть знакомым нам словом с {length} буквами."""

        return string

    @abstractmethod
    def start_game() -> str:
        string = """
Закадано слово из 5 букв. У Вас 6 попыток."""

        return string

    @abstractmethod
    def guess_attempt(count_attempts: int) -> str:
        string = f"""
Попытка {count_attempts} (для выхода ввидете цифру 0): """

        return string

    @abstractmethod
    def stat_among_guesses(guess: str) -> str:
        string = f"""
Результат: {guess}"""

        return string

    @abstractmethod
    def congratulations(goal: str, count_attempts: int) -> str:

        string = f"""
Вы угадали слово '{goal}' за {count_attempts} попыток."""

        return string

    @abstractmethod
    def failure(goal: str, count_attempts: int) -> str:

        string = f"""
Вы НЕ угадали слово '{goal}' за {count_attempts} попыток."""

        return string

    @abstractmethod
    def restart() -> str:
        string = """
Хотите сыграть еще?
[1] - Да
[0] - Нет

: """
        return string
