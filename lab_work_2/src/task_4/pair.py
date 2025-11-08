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


    def __str__(self) -> str:
        return f"({self.axis.name})--{self.length}(мм)--"


    def __repr__(self):
        pass