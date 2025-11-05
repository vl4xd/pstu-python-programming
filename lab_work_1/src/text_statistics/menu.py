from text_statistics.messages import welcome, incoret_input, restart, analysis_result
from text_statistics.text_statistics import get_text_from_file, get_count_symbols, get_word_form_dict, get_top_count_words, get_top_length_words, get_average_word_length
from common.common import menu_choiсe


def get_text_statistics_main_menu() -> None:

    while True:

        user_text: str
        choice_start: int = menu_choiсe(0, 1, welcome())
        if choice_start == 0:
            break

        user_text = get_text_from_file('./text_statistics/text.txt')

        len_user_text = len(user_text)
        if len_user_text < 100:
            print(incoret_input(len_user_text))
            continue

        word_form_dict = get_word_form_dict(user_text)
        print(analysis_result(
            get_count_symbols(user_text),
            get_average_word_length(word_form_dict),
            get_top_count_words(word_form_dict, 5),
            get_top_length_words(word_form_dict, 5)
        ))

        choice_restart: int = menu_choiсe(0, 1, restart())
        if choice_restart == 0:
            break
