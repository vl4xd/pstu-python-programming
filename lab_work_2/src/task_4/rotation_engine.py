from engine import Engine

class RotationEngine(Engine):


    def __init__(self, power, speed, acceleration, angle):
        super().__init__(power, speed, acceleration)
        self.angle = angle