import numpy as np

from .pair import Pair

class Manipulator:


    def __init__(self) -> None:
        self.pairs: list[Pair] = []
        self.pairs_values: list[list[int]] = [[]]


    def add_pair(self, pair: Pair) -> None:
        self.pairs.append(pair)
        self.pairs_values[0].append(pair.value)


    def clear_pairs(self) -> None:
        self.pairs.clear()
        self.pairs_values.clear()
        self.pairs_values.append([])


    def get_translation_matrix(self, lenght: int) -> np.array:
        """Матрица длины звена (всегда вдоль оси X)

        :return np.array: _description_
        """
        return np.array([
                [1, 0, 0, lenght],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])



    def forward_kinematics(self, work_time_set: list[int]) -> None:
        """_summary_

        :param list[int] work_time_set: время работы каждой пары (сек)
        """
        if len(work_time_set) != len(self.pairs):
            raise ValueError("Длина work_time_set должна быть равна количеству пар манипулятора.")

        # Начальная точка (база)
        T = np.eye(4)  # Единичная матрица
        points = [T @ np.array([0, 0, 0, 1])]  # База

        for i, pair in enumerate(self.pairs):
            T = T @ pair.get_matrix(work_time_set[i])

            if pair.length != 0:
                T = T @ self.get_translation_matrix(pair.length)

            points.append(T @ np.array([0, 0, 0, 1]))

        return points


    def __str__(self):
        string = "Manipulator:\n|-"
        for pair in self.pairs:
            string += str(pair)
        string += "C"

        return string
