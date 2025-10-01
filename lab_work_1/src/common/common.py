from abc import ABC, abstractmethod

class MsgCommon(ABC):

    @abstractmethod
    def IncorrectChoiсe(choiсe_input: str) -> str:
        string = f"""
Некорректный выбор ({choiсe_input})! Введите цифру - пункт меню, отмеченный в [.]."""

        return string


def MenuChoiсe(start: int, end: int, msg_menu: object) -> int:
    while True:
        choise_input: str = input(msg_menu)
        try:
            choise_int = int(choise_input)
            if choise_int < start or choise_int > end:
                raise ValueError
            return choise_int
        except ValueError:
            print(MsgCommon.IncorrectChoiсe(choise_input))