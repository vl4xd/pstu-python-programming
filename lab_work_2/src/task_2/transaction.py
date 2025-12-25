from datetime import datetime

from .transaction_type import TransactionType

class Transaction:


    def __init__(self, description: str, total: int, type: TransactionType, category: str) -> None:
        """Transaction initialisation

        :param str description: transaction description
        :param int total: transaction total in cents (e.g. 1050 = 10.50)
        :param TasnactionType type: transaction type
        :param str category: transaction category
        """
        self._description: str = description
        self._total: int = total
        self._type: TransactionType = type
        self._category: str = category
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


    def __str_total(self) -> str:
        return f"{self._total // 100} руб. {self._total % 100} коп."


    def __str_type_tag(self) -> str:
        match self._type:
            case TransactionType.income:
                return "▲"
            case TransactionType.expense:
                return "▼"


    def __radd__(self, other):
        if isinstance(other, int):
            return other + self._total


    def __str__(self) -> str:
        return f"{self.__str_type_tag()} Транзакция ({self._created_at}): {self._description} #{self.categoty} ({self.__str_total()})"


    def __repr__(self) -> str:
        return f"Transaction(description={self._description}, total={self._total}, type={self._type}, category={self._category}, created_at={self._created_at})"
