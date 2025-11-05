from abc import ABC, abstractmethod

from number_analyzer.number_analyzer import is_number_simple, is_number_perfect, get_string_sum_divisors

class MsgMainMenu(ABC):

    @abstractmethod
    def welcome() -> str:
        string = """
'Анализатор чисел'

Меню:
[1] - Анализировать число
[2] - Об анализаторе

[0] - Назад

: """
        return string

    @abstractmethod
    def about() -> str:
        string = """
                Об анализаторе:

Данная программма анализирует введенное число по следующим критериям:

- Проверка числа на простоту (делиться только на 1 и на себя)
- Проверка на совершенность (равно сумме всех своих делителей, кроме себя самого)

[0] - Назад

: """
        return string


class MsgAnalyzer(ABC):


    @abstractmethod
    def incorrect_number() -> str:
        string = """
Некорретный ввод! Число должно быть ЦЕЛЫМ ПОЛОЖИТЕЛЬНЫМ."""

        return string

    @abstractmethod
    def number_attempt() -> str:
        string = """
Ваше число (для выхода ввидете цифру 0): """

        return string

    @abstractmethod
    def analyzed_number(number: int, divisors: list[int]) -> str:
        string = """
"""
        string += f"Делители числа {number}: {divisors}\n"

        if is_number_simple(divisors):
            string += f"Число {number} является ПРОСТЫМ\n"
        else:
            string += f"Число {number} НЕ является ПРОСТЫМ\n"

        if is_number_perfect(number, divisors):
            string += f"Число {number} является СОВЕРШЕННЫМ: ({get_string_sum_divisors(divisors)})"
        else:
            string += f"Число {number} НЕ является СОВЕРШЕННЫМ: ({get_string_sum_divisors(divisors)})"

        return string

    @abstractmethod
    def restart() -> str:
        string = """
Хотите проанализировать еще число?
[1] - Да
[0] - Нет

: """
        return string