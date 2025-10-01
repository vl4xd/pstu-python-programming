import random

class Wordle:

    def __init__(self):
        self.wordl_list_5: list[str] = [
            "берег",
            "ветер",
            "город",
            "дождь",
            "жизнь",
            "звено",
            "игрок",
            "октан",
            "капля",
            "лучши",
            "номер",
            "остро",
            "товар",
            "ягода",
            "лотос",
            "столп",
            "комод",
            "наган",
            "мадам",
        ]
        self.length = 5
        self.goal: str = random.choice(self.wordl_list_5).lower()
        self.max_attempts: int = 6
        self.count_attempts: int = 1
        self.is_finished: bool = False


    def _AddAttempt(self) -> None:
            self.count_attempts += 1


    def CheckWord(self, guess: str) -> str:
        len_guess: int = len(guess)
        len_goal: int = len(self.goal)
        if len_guess!= len_goal:
            raise ValueError(f"Guess len({len_guess}) and goal ({len_goal}) must have the same number of digits.")

        guess = guess.lower()

        if guess == self.goal or self.max_attempts <= self.count_attempts:
            self.is_finished = True
        else:
            self._AddAttempt()

        goal_letters_list: list[str] = list(self.goal)
        guess_letters_list: list[str] = list(guess)
        guess_check_list: list[bool] = [False for _ in range(len(guess))]

        for i, guess_letter in enumerate(guess):
            if guess_letter == self.goal[i]:
                guess_letters_list[i] = f"[{guess_letters_list[i]}]"
                goal_letters_list[i] = "boom"
                guess_check_list[i] = True

        for i in range(len(guess)):
            if guess_check_list[i]:
                continue
            if guess[i] in goal_letters_list:
                goal_letter_index = goal_letters_list.index(guess[i])
                goal_letters_list[goal_letter_index] = "boom"
                guess_letters_list[i] = f"({guess_letters_list[i]})"
            guess_check_list[i] = True

        return " ".join(guess_letters_list)


    def __str__(self):
        pass
