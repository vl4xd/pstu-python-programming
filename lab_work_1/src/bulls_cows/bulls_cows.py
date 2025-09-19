import random


class SumBullsCowsWrongs:

    def __init__(self, bulls: int = -1, cows: int = -1, wrongs: int = -1):
        self.bulls: int = bulls
        self.cows: int = cows
        self.wrongs: int = wrongs

    def __str__(self):
        return f"Bulls = {self.bulls}; Cows = {self.cows}; Wrongs = {self.wrongs}"


def GetRandomGoal(length: int) -> int:
    """Generates a random number with digits of specified length."""
    try:
        length = int(length)
    except ValueError:
        raise ValueError("Length must be an integer.")

    digits = '0123456789'
    match length:
        case 3 | 4 | 5:
            goal = int("".join(random.choices(digits, k=length)))
        case _:
            raise ValueError("Length must be 3, 4, or 5.")

    return goal


def CountBullsAndCows(length: int, guess: int, goal: int) -> SumBullsCowsWrongs:
    """Count the number of bulls and cows in a guess compared to the goal."""

    try:
        guess = int(guess)
        goal = int(goal)
    except ValueError:
        raise ValueError("Guess and goal must be integers.")

    guess_str = AddPrefixZero(length, guess)
    goal_str = AddPrefixZero(length, goal)

    len_guess = len(guess_str)
    len_goal = len(goal_str)

    if len_guess != len_goal:
        raise ValueError(f"Guess len({len_guess}) and goal ({len_goal}) must have the same number of digits.")

    cows_sum = 0
    goal_intersection_str = ""
    guess_intersection_str = ""
    for guess_digit, goal_digit in zip(guess_str, goal_str):
        if int(guess_digit) == int(goal_digit):
            cows_sum += 1
        else:
            guess_intersection_str += guess_digit
            goal_intersection_str += goal_digit

    bulls_sum = len(set(guess_intersection_str) & set(goal_intersection_str))

    wrongs_sum = len_goal - bulls_sum - cows_sum

    return SumBullsCowsWrongs(bulls_sum, cows_sum, wrongs_sum)


def IsGameFinished(sum_bulls_cows_wrons: SumBullsCowsWrongs) -> bool:

    if sum_bulls_cows_wrons.bulls == 0 and sum_bulls_cows_wrons.wrongs == 0:
        return True
    return False


def AddPrefixZero(length: int, number: int) -> str:
    return str(number).zfill(length)