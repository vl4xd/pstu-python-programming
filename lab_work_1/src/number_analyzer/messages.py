from abc import ABC, abstractmethod

from number_analyzer.number_analyzer import IsNumberSimple, IsNumberPerfect, GetStringSumDivisors

class MsgMainMenu(ABC):

    @abstractmethod
    def Welcome() -> str:
        string = """
'Анализатор чисел'

Меню:
[1] - Анализировать число
[2] - Об анализаторе

[0] - Назад

: """
        return string

    @abstractmethod
    def About() -> str:
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
    def IncorrectNumber() -> str:
        string = """
Некорретный ввод! Число должно быть ЦЕЛЫМ ПОЛОЖИТЕЛЬНЫМ."""

        return string

    @abstractmethod
    def NumberAttempt() -> str:
        string = """
Ваше число (для выхода ввидете цифру 0): """

        return string

    @abstractmethod
    def AnalyzedNumber(number: int, divisors: list[int]) -> str:
        string = """
"""
        string += f"Делители числа {number}: {divisors}\n"

        if IsNumberSimple(divisors):
            string += f"Число {number} является ПРОСТЫМ\n"
        else:
            string += f"Число {number} НЕ является ПРОСТЫМ\n"

        if IsNumberPerfect(number, divisors):
            string += f"Число {number} является СОВЕРШЕННЫМ: ({GetStringSumDivisors(divisors)})"
        else:
            string += f"Число {number} НЕ является СОВЕРШЕННЫМ: ({GetStringSumDivisors(divisors)})"

        return string

    @abstractmethod
    def Restart() -> str:
        string = """
Хотите проанализировать еще число?
[1] - Да
[0] - Нет

: """
        return string