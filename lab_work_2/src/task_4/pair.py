import numpy as np

from .servo import Servo
from .axis_type import AxisType

class Pair(Servo):
    def __init__(self, axis: AxisType, speed: int, rest_current: int, move_current: int, length: int, value: int) -> None:
        """_summary_

        :param AxisType axis: _description_
        :param int speed: _description_
        :param int rest_current: _description_
        :param int move_current: _description_
        :param int length: _description_
        :param int value: начальное значение пары
        """
        super().__init__(speed, rest_current, move_current)
        self.axis: AxisType = axis
        self.length: int = length
        self.value: int = value


    def get_matrix(self, work_time: int) -> np.array:
        """_summary_

        :param int work_time: время работы в секундах
        """
        pass


    def __mul__(self, other):
        """Использовать для умножение на время работы в секундах

        :param _type_ other: _description_
        """
        if isinstance(other, (int, float)):
            if other == 0:
                return self.rest_current
            # Берем модуль если, поскольку может быть отрицательное значене, показывающее движение в обратную сторону
            abs_other = abs(other)
            return abs_other * self.move_current


    def __rmul__(self, other):
        return self.__mul__(other)



    def __eq__(self, other) -> bool:
        if isinstance(other, Pair):
            result = self.axis == other.axis and \
                self.speed == other.speed and \
                self.rest_current == other.rest_current and \
                self.move_current == other.move_current and \
                self.length == other.length and \
                self.value == other.value
            return result



    def __ne__(self, other) -> bool:
        if isinstance(other, Pair):
            result = self.axis != other.axis and \
                self.speed != other.speed and \
                self.rest_current != other.rest_current and \
                self.move_current != other.move_current and \
                self.length != other.length and \
                self.value != other.value
            return result


    def __lt__(self, other) -> bool:
        if isinstance(other, Pair):
            result = self.axis < other.axis and \
                self.speed < other.speed and \
                self.rest_current < other.rest_current and \
                self.move_current < other.move_current and \
                self.length < other.length and \
                self.value < other.value
            return result


    def __gt__(self, other) -> bool:
        if isinstance(other, Pair):
            result = self.axis > other.axis and \
                self.speed > other.speed and \
                self.rest_current > other.rest_current and \
                self.move_current > other.move_current and \
                self.length > other.length and \
                self.value > other.value
            return result


    def __le__(self, other) -> bool:
        if isinstance(other, Pair):
            result = self.axis <= other.axis and \
                self.speed <= other.speed and \
                self.rest_current <= other.rest_current and \
                self.move_current <= other.move_current and \
                self.length <= other.length and \
                self.value <= other.value
            return result


    def __ge__(self, other) -> bool:
        if isinstance(other, Pair):
            result = self.axis >= other.axis and \
                self.speed >= other.speed and \
                self.rest_current >= other.rest_current and \
                self.move_current >= other.move_current and \
                self.length >= other.length and \
                self.value >= other.value
            return result


    def __str__(self) -> str:
        return f"({self.axis.name})--{self.length}(мм)--"


    def __repr__(self):
        pass