from abc import ABC, abstractmethod


class MsgCommon(ABC):

    @abstractmethod
    def IncorrentChoiсe(choiсe_input: str) -> str:
        string = f"""
Некорректный выбор ({choiсe_input})."""

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

:
"""
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

:"""
        return string