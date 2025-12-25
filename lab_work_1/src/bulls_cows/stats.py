

def init_common_stats() -> dict[str:float | None]:
    """"""

    stats = {
        'Всего игр сыграно': 0,
        'Общий лучший результат': None,
        'Общий худший результат': None,
        'Общий средний результат': None,
        'Игр в режиме "Легко" (3 цифры)': 0,
        '"Легко" лучший результат': None,
        '"Легко" худший результат': None,
        '"Легко" средний результат': None,
        'Игр в режиме "Нормально" (4 цифры)': 0,
        '"Нормально" лучший результат': None,
        '"Нормально" худший результат': None,
        '"Нормально" средний результат': None,
        'Игр в режиме "Сложно" (5 цифр)': 0,
        '"Сложно" лучший результат': None,
        '"Сложно" худший результат': None,
        '"Сложно" средний результат': None,
    }

    return stats


def add_common_stats(common_stats: dict[str:float], count_attempt: int, length: int) -> None:

    if common_stats['Общий лучший результат'] is None or common_stats['Общий лучший результат'] > count_attempt:
        common_stats['Общий лучший результат'] = count_attempt

    if common_stats['Общий худший результат'] is None or common_stats['Общий худший результат'] < count_attempt:
        common_stats['Общий худший результат'] = count_attempt

    if common_stats['Общий средний результат'] is None:
        common_stats['Общий средний результат'] = count_attempt
    else:
        common_stats['Общий средний результат'] = (common_stats['Общий средний результат'] * \
                                                common_stats['Всего игр сыграно'] + count_attempt) / \
                                                    (common_stats['Всего игр сыграно'] + 1)

    common_stats['Всего игр сыграно'] += 1


    game_count_in = ''
    best_result_in = ''
    worst_result_in = ''
    average_result_in = ''
    match length:
        case 3:
            game_count_in = 'Игр в режиме "Легко" (3 цифры)'
            best_result_in = '"Легко" лучший результат'
            worst_result_in = '"Легко" худший результат'
            average_result_in = '"Легко" средний результат'
        case 4:
            game_count_in = 'Игр в режиме "Нормально" (4 цифры)'
            best_result_in = '"Нормально" лучший результат'
            worst_result_in = '"Нормально" худший результат'
            average_result_in = '"Нормально" средний результат'
        case 5:
            game_count_in = 'Игр в режиме "Сложно" (5 цифр)'
            best_result_in = '"Сложно" лучший результат'
            worst_result_in = '"Сложно" худший результат'
            average_result_in = '"Сложно" средний результат'

    if common_stats[best_result_in] is None or common_stats[best_result_in] > count_attempt:
        common_stats[best_result_in] = count_attempt

    if common_stats[worst_result_in] is None or common_stats[worst_result_in] < count_attempt:
        common_stats[worst_result_in] = count_attempt

    if common_stats[average_result_in] is None:
        common_stats[average_result_in] = count_attempt
    else:
        common_stats[average_result_in] = (common_stats[average_result_in] * \
                                                common_stats[game_count_in] + count_attempt) / \
                                                    (common_stats[game_count_in] + 1)

    common_stats[game_count_in] += 1


def get_common_stats_info(common_stats: dict[str:float | None]) -> str:
    string = ''

    for key, value in common_stats.items():
        string += f'{key}: {0 if value is None else value} \n'

    return string