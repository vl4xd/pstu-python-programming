from abc import ABC, abstractmethod

class MsgMainMenu(ABC):

    @abstractmethod
    def Welcome() -> str:
        string = """
'Лабораторная работа №1'

Меню:
[1] - Быки и коровы
[2] - Анализатор чисел
[3] - Wordle/5 букв
[4] - Камень-Ножницы-Бумага-Ящерица-Спок
[5] - Статистика текста

[0] - Выход

: """
        return string
