def Welcome() -> str:
    string = """
'Статистика текста'

Введите текст для анализа в файл text.txt (не менее 100 символов).

[1] - Проанализировать текст из файла text.txt
[0] - Назад

: """
    return string


def AnalysisResult(count_symbols: tuple[int, int],
                   count_average_words: tuple[int,float],
                   top_count_words: list[tuple[str, list[int]]],
                   top_length_words: list[tuple[str, list[int]]]) -> str:
    string = f"""
Результаты анализа:

Общее количество символов: {count_symbols[0]} (без пробелов {count_symbols[1]})
Количество словоформ: {count_average_words[0]}
Средняя длина слова: {count_average_words[1]:.2f}

"""
    string += "Самые частые словоформы:\n"
    for word, form in top_count_words:
        string += f"- '{word}': {form[0]} раз(а)\n"

    string += "\nСамые длинные словоформы:\n"
    for word, form in top_length_words:
        string += f"- '{word}' ({form[1]} букв)\n"

    return string

def Restart() -> str:
    string = """
Хотите проанализировать текст еще?
[1] - Да
[0] - Нет

: """
    return string


def IncoretInput(lenght: int) -> str:
    string = f"""
Текст должен содежрать не менее 100 символов, у Вас сейчас {lenght} символов (для выхода введите - 0).
"""
    return string
