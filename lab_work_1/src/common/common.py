from abc import ABC, abstractmethod

class MsgCommon(ABC):

    @abstractmethod
    def incorrect_choiсe(choiсe_input: str) -> str:
        string = f"""
Некорректный выбор ({choiсe_input})! Введите цифру - пункт меню, отмеченный в [.]."""

        return string


def menu_choiсe(start: int, end: int, msg_menu: object) -> int:
    while True:
        choise_input: str = input(msg_menu)
        try:
            choise_int = int(choise_input)
            if choise_int < start or choise_int > end:
                raise ValueError
            return choise_int
        except ValueError:
            print(MsgCommon.incorrect_choiсe(choise_input))