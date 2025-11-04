from datetime import datetime

from transaction import Transaction
from transaction_type import TransactionType
from category import Category

class BudgetTracker:


    def __init__(self, balance: int) -> None:
        """BudgetTracker initialisation

        :param int balance: balance in cents (e.g. 1050 = 10.50)
        """
        self._balance: int = balance
        self._categories: list[Category] = []
        self._transactions: list[Transaction] = []


    def add_category(self, category: Category) -> None:
        """Add new category

        :param str category: category name
        :param int limit: limit in cents (e.g. 1050 = 10.50), defaults to 0 (unlimited)
        """

        if category not in self._categories:
            self._categories.append(category)
        return


    def __change_balance(self, transaction: Transaction) -> None:
        """Change balance according to transaction

        :param Transaction transaction: transaction instance
        """
        match transaction._type:
            case TransactionType.income:
                self._balance += transaction._total
            case TransactionType.expense:
                self._balance -= transaction._total
        return


    def __get_transactions_in_cur_month(self, category: str, type: TransactionType) -> list[Transaction]:
        cur_date = datetime.today()
        first_month_datetime = cur_date.replace(day=1)

        return [tr for tr in self._transactions if first_month_datetime <= tr._created_at and tr._category == category and tr._type == type]


    def is_over_limit(self, transaction: Transaction) -> bool:
        if transaction._category not in self._categories:
            return False

        if transaction._type == TransactionType.income:
            return False

        past_transactions_totals = sum(self.__get_transactions_in_cur_month(transaction._category, transaction._type))
        category_index = self._categories.index(transaction._category)

        if self._categories[category_index]._limit < past_transactions_totals + transaction._total:
            return True

        return False


    def add_transaction(self, transaction: Transaction) -> None:
        """Add new transaction

        :param Transaction transaction: transaction instance
        """
        if transaction._category not in self._categories:
            new_category = Category(transaction._category)
            self.add_category(new_category)

        self._transactions.append(transaction)
        self.__change_balance(transaction)


    def __str__(self):
        return f"Трекер бюджета: категорий - {len(self._categories_limit)}; транзакций - {len(self._transactions)}"


    def __repr__(self):
        return f"BudgetTracker(categories_balance={self._categories_limit}, transactions={self._transactions})"