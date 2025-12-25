from common.common import menu_choiсe
from rock_paper_scissors.messages import MsgMainMenu, MsgWinRateMenu, MsgGame
from rock_paper_scissors.rock_paper_scissors import get_random_game_unit, is_left_beats_right, get_list_keys_game_units, get_game_unit_name, is_game_finished

def get_rock_paper_scissors_main_menu() -> None:

    start = 0
    end = 2

    while True:
        choice: int = menu_choiсe(start, end, MsgMainMenu.welcome())
        match choice:
            case 0:
                return
            case 1:
                _get_win_rate_menu()
            case 2:
                _get_rules_menu()


def _get_win_rate_menu():

    start = 0
    end = 10

    while True:
        choice: int = menu_choiсe(start, end, MsgWinRateMenu.select_win_rate())
        if choice == 0:
            return

        while True:
            if not _get_game_menu(choice):
                break


def _get_rules_menu():

    start = 0
    end = 0

    while True:
        choice: int = menu_choiсe(start, end, MsgMainMenu.rules())
        if choice == 0:
            return


def _get_game_menu(win_rate: int) -> bool:

    computer_wins: int = 0
    player_wins: int = 0
    count_moves: int = 0

    while not is_game_finished(win_rate, player_wins, computer_wins):
        count_moves += 1
        is_player_win: bool = False
        is_draw: bool = False

        computer_choice: int = get_random_game_unit()
        print(f"*Подсказка - {get_game_unit_name(computer_choice)}*")

        guess: int = _check_user_guess(MsgGame.guess_attempt(count_moves))
        if guess == 0:
            return False

        if guess == computer_choice:
            player_wins += 1
            computer_wins += 1
            is_draw = True
        else:
            win_status, msg_status = is_left_beats_right(guess, computer_choice)
            print(msg_status)
            if win_status:
                player_wins += 1
                is_player_win = True
            else:
                computer_wins += 1

        if is_game_finished(win_rate, player_wins, computer_wins):
            continue

        print(MsgGame.stat_among_guesses(player_wins, computer_wins, is_player_win, is_draw))
    else:
        print(MsgGame.congratulations(player_wins, computer_wins))
        choice: int = menu_choiсe(0, 1, MsgGame.restart())
        if choice == 1:
            return True
        return False


def _check_user_guess(msg: object) -> int:
    while True:
        guess_input: str = input(msg)
        try:
            guess_int = int(guess_input)
            if guess_int == 0:
                return guess_int
            if guess_int not in get_list_keys_game_units():
                raise ValueError
            return guess_int
        except ValueError:
            print(MsgGame.incorrect_guess())