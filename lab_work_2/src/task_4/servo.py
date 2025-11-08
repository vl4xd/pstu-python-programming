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