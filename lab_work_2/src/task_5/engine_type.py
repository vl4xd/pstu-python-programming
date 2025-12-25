from enum import Enum


class CarEngineType(Enum):
    electric = 'электрический'
    petrol = 'бензиновый'
    gas = 'газовый'
    diesel = 'дизельный'


class BicycleEngineType(Enum):
    electric = 'электрический'
    muscular = 'мускульная сила'