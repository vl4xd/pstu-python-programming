from text_statistics.messages import Welcome, IncoretInput, Restart, AnalysisResult
from text_statistics.text_statistics import GetTextFromFile, GetCountSymbols, GetWordFormDict, GetTopCountWords, GetTopLengthWords, GetAverageWordLength
from common.common import MenuChoiсe


def GetTextStatisticsMainMenu() -> None:

    while True:

        user_text: str
        choice_start: int = MenuChoiсe(0, 1, Welcome())
        if choice_start == 0:
            break

        user_text = GetTextFromFile('./text_statistics/text.txt')

        word_form_dict = GetWordFormDict(user_text)
        print(AnalysisResult(
            GetCountSymbols(user_text),
            GetAverageWordLength(word_form_dict),
            GetTopCountWords(word_form_dict, 5),
            GetTopLengthWords(word_form_dict, 5)
        ))

        choice_restart: int = MenuChoiсe(0, 1, Restart())
        if choice_restart == 0:
            break


def _CheckUserInput(msg: object) -> str:
    length: int = 100
    while True:
        user_input: str = input(msg)
        try:
            if user_input == '0':
                return user_input
            if len(user_input) < length:
                raise ValueError
            return user_input
        except ValueError:
            print(IncoretInput(length))