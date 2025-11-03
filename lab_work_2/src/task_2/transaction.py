from datetime import datetime

from transaction_type import TasnactionType

class Transaction:


    def __init__(self, description: str, total: int, type: TasnactionType, category: str):
        """Transaction initialisation

        :param str description: transaction description
        :param int total: transaction total in 
        :param TasnactionType type: _description_
        :param str category: _description_
        """
        self._description = description
        self._total = total
        self._type = type
        self._category = category
        self._created_at: datetime = datetime.now()

    
    @property
    def description(self) -> str:
        """Get a description

        :return str: transaction description
        """
        return self._description
    

    @property
    def total(self) -> int:
        """Get a total

        :return str: transaction total
        """
        return self._description


    @property
    def categoty(self) -> str:
        """Get a category

        :return str: transaction category
        """
        return self._category
    

    @property
    def created_at(self) -> datetime:
        """Get a creation datetime

        :return datetime: transaction creation datetime
        """
        return self._created_at