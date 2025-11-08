
class Engine:


    def __init__(self, speed: int) -> None:
        self.speed: int = speed


    def __eq__(self, other) -> bool:
        if isinstance(other, Engine):
            return self.speed == other.speed
        if isinstance(other, int):
            return self.speed == other


    def __ne__(self, other) -> bool:
        if isinstance(other, Engine):
            return self.speed != other.speed
        if isinstance(other, int):
            return self.speed != other


    def __lt__(self, other) -> bool:
        if isinstance(other, Engine):
            return self.speed < other.speed
        if isinstance(other, int):
            return self.speed < other


    def __gt__(self, other) -> bool:
        if isinstance(other, Engine):
            return self.speed > other.speed
        if isinstance(other, int):
            return self.speed > other


    def __le__(self, other) -> bool:
        if isinstance(other, Engine):
            return self.speed <= other.speed
        if isinstance(other, int):
            return self.speed <= other


    def __ge__(self, other) -> bool:
        if isinstance(other, Engine):
            return self.speed >= other.speed
        if isinstance(other, int):
            return self.speed >= other
