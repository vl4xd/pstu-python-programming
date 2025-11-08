from .engine import Engine

class Servo(Engine):

    def __init__(self, speed: int, rest_current: int, move_current: int) -> None:
        """_summary_

        :param int speed: _description_
        :param float hold_current: потребляемый ток в состоянии покоя (мА)
        :param float move_current: потребляемый ток в движении (мА)
        """
        super().__init__(speed)
        self.rest_current: int = rest_current
        self.move_current: int = move_current
        self.current_current: int = rest_current


    def __eq__(self, other) -> bool:
        if isinstance(other, Servo):
            result = self.speed == other.speed and \
                self.rest_current == other.rest_current and \
                self.move_current == other.move_current
            return result



    def __ne__(self, other) -> bool:
        if isinstance(other, Servo):
            result = self.speed != other.speed and \
                self.rest_current != other.rest_current and \
                self.move_current != other.move_current
            return result


    def __lt__(self, other) -> bool:
        if isinstance(other, Servo):
            result = self.speed < other.speed and \
                self.rest_current < other.rest_current and \
                self.move_current < other.move_current
            return result


    def __gt__(self, other) -> bool:
        if isinstance(other, Servo):
            result = self.speed > other.speed and \
                self.rest_current > other.rest_current and \
                self.move_current > other.move_current
            return result


    def __le__(self, other) -> bool:
        if isinstance(other, Servo):
            result = self.speed <= other.speed and \
                self.rest_current <= other.rest_current and \
                self.move_current <= other.move_current
            return result


    def __ge__(self, other) -> bool:
        if isinstance(other, Servo):
            result = self.speed >= other.speed and \
                self.rest_current >= other.rest_current and \
                self.move_current >= other.move_current
            return result
