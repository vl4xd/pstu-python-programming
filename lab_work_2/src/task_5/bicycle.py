from .road_vehicle import RoadVehicle
from .engine_type import BicycleEngineType
from .vehicle_type import VehicleType


class Bicycle(RoadVehicle):


    def __init__(self, max_speed: int, engine_type: BicycleEngineType):
        if not isinstance(engine_type, BicycleEngineType):
            raise ValueError("Значение 'engine_type' должно быть выбрано из перечисления 'BicycleEngineType'")
        self._max_speed = max_speed
        self._engine_type = engine_type
        self._vegicle_type = VehicleType.bicycle


    def get_max_speed(self) -> int:
        return self._max_speed


    def get_vehicle_type(self) -> str:
        return self._vegicle_type.value


    def get_engine_type(self) -> str:
        return self._engine_type.value
