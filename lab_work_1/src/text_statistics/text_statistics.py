def GetTextFromFile(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        text: str = file.read()
    return text


def GetCountSymbols(text: str) -> tuple[int, int]:
    symbols_with_spaces: int = len(text)
    symbols_without_spaces: int = len(text.replace(" ", "").replace("\n", ""))
    return symbols_with_spaces, symbols_without_spaces


def GetWordFormDict(text: str) -> dict[str, list[int]]:
    word_form_dict: dict[str, list[int]] = {}
    word: str = ''
    for symbol in text:
        symbol: str = symbol.lower()
        if symbol.isalpha():
            word += symbol
        else:
            if word != '':
                word_form_dict.setdefault(word, [0, len(word)])
                word_form_dict[word][0] += 1
                word = ''
    # обробатываем последнее слово если есть
    if word != '':
        word_form = word_form_dict.setdefault(word, [0, len(word)])
        word_form[word][0] += 1

    return word_form_dict


def GetTopCountWords(word_form_dict: dict[str, list[int]], top_count: int) -> list[tuple[str, list[int]]]:
    sorted_word_forms: list[tuple[str, list[int]]] = sorted(
        word_form_dict.items(),
        key=lambda item: item[1][0],
        reverse=True
    )
    return sorted_word_forms[:top_count]


def GetTopLengthWords(word_form_dict: dict[str, list[int]], top_count: int) -> list[tuple[str, list[int]]]:
    sorted_word_forms: list[tuple[str, list[int]]] = sorted(
        word_form_dict.items(),
        key=lambda item: item[1][1],
        reverse=True
    )
    return sorted_word_forms[:top_count]


def GetAverageWordLength(word_form_dict: dict[str, list[int]]) -> tuple[int, float]:
    total_length: int = sum(length * count for count, length in word_form_dict.values())
    total_count: int = sum(count for count, length in word_form_dict.values())
    if total_count == 0:
        return 0.0
    return total_count, total_length / total_count
