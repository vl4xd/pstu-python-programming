from abc import abstractmethod

from .vehicle import Vehicle


class RoadVehicle(Vehicle):


    @classmethod
    @abstractmethod
    def get_engine_type(self):
        """Получить тип двигателя
        """
