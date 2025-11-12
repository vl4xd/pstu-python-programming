import numpy as np

from .pair import Pair
from .axis_type import AxisType


class RotatingPair(Pair):
    def __init__(self, axis: AxisType, speed: int, rest_current, move_current, length, value: int):
        """_summary_

        :param _type_ axis: _description_
        :param _type_ speed: скорость вращения (град/с)
        :param _type_ rest_current: _description_
        :param _type_ move_current: _description_
        :param _type_ length: _description_
        :param int value: начальное значение пары (град)
        """
        super().__init__(axis, speed, rest_current, move_current, length, value)
        self.speed = np.radians(speed)


    def get_matrix(self, work_time: int) -> np.array:
        theta = self.speed * work_time
        match self.axis:
            case AxisType.X:
                return np.array([
                    [1, 0, 0, 0],
                    [0, np.cos(theta), -np.sin(theta), 0],
                    [0, np.sin(theta), np.cos(theta), 0],
                    [0, 0, 0, 1]
                ])
            case AxisType.Y:
                return np.array([
                    [np.cos(theta), 0, np.sin(theta), 0],
                    [0, 1, 0, 0],
                    [-np.sin(theta), 0, np.cos(theta), 0],
                    [0, 0, 0, 1]
                ])
            case AxisType.Z:
                return np.array([
                    [np.cos(theta), -np.sin(theta), 0, 0],
                    [np.sin(theta), np.cos(theta), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]
                ])


    def __mul__(self, other):
        return super().__mul__(other)


    def __rmul__(self, other):
        return super().__rmul__(other)


    def __eq__(self, other):
        return super().__eq__(other)


    def __ne__(self, other):
        return super().__ne__(other)


    def __lt__(self, other):
        return super().__lt__(other)


    def __gt__(self, other):
        return super().__gt__(other)


    def __le__(self, other):
        return super().__le__(other)


    def __ge__(self, other):
        return super().__ge__(other)


    def __str__(self) -> str:
        return "⭯" + super().__str__()