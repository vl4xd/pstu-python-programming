from abc import ABC, abstractmethod


class Vehicle(ABC):


    @classmethod
    @abstractmethod
    def get_max_speed(self):
        """Получить максимальную скорость
        """

    @classmethod
    @abstractmethod
    def get_vehicle_type(self):
        """Получить тип транспортного средства
        """