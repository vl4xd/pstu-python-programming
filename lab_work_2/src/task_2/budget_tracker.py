from datetime import datetime

from .transaction import Transaction
from .transaction_type import TransactionType
from .category import Category

class BudgetTracker:


    def __init__(self, balance: int = 0) -> None:
        """BudgetTracker initialisation

        :param int balance: balance in cents (e.g. 1050 = 10.50)
        """
        self._balance: int = balance
        self._categories: list[Category] = []
        self._transactions: list[Transaction] = []


    @property
    def balance(self) -> int:
        return self._balance


    @balance.setter
    def balance(self, new_balance) -> None:
        self._balance = new_balance


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


    def __get_transactions_in_cur_month_by_category(self, category: str) -> list[Transaction]:
        cur_date = datetime.today()
        first_month_datetime = cur_date.replace(day=1)

        return [tr for tr in self._transactions if first_month_datetime <= tr._created_at and tr._category == category]


    def __get_transactions_in_cur_month_by_category_type(self, category: str, type: TransactionType) -> list[Transaction]:
        cur_date = datetime.today()
        first_month_datetime = cur_date.replace(day=1)

        return [tr for tr in self._transactions if first_month_datetime <= tr._created_at and tr._category == category and tr._type == type]


    def __sum_transactions_in_cur_month(self, category: str, type: TransactionType) -> int:
        return sum(self.__get_transactions_in_cur_month_by_category_type(category, type))


    def is_over_limit(self, transaction: Transaction) -> bool:
        if transaction._category not in self._categories:
            return False

        if transaction._type == TransactionType.income:
            return False

        past_transactions_totals = self.__sum_transactions_in_cur_month(transaction._category, transaction._type)
        category_index = self._categories.index(transaction._category)

        if self._categories[category_index]._limit != 0 and self._categories[category_index]._limit < past_transactions_totals + transaction._total:
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


    def str_sorted_by_category(self, income: bool = True, expense: bool = True) -> str:
        string = f"Трекер бюджета (текущий баланс: {self._balance // 100} руб. {self._balance % 100} коп.):\n"
        for cat in self._categories:
            sum_income_in_month = self.__sum_transactions_in_cur_month(cat._name, TransactionType.income)
            sum_expense_in_month = self.__sum_transactions_in_cur_month(cat._name, TransactionType.expense)
            tr_in_month = self.__get_transactions_in_cur_month_by_category(cat._name)
            count_tr_in_month = len(tr_in_month)
            string += f"    #{cat} Сумма в месяц: ▲ {sum_income_in_month // 100} руб. {sum_income_in_month % 100} коп. | ▼ {sum_expense_in_month // 100} руб. {sum_expense_in_month % 100} коп. (всего транзакций за месяц: {count_tr_in_month}):\n"
            for tr in tr_in_month:
                if tr._type is TransactionType.income and not income:
                    continue
                if tr._type is TransactionType.expense and not expense:
                    continue
                string += f"        {tr}\n"
        return string


    def __str__(self):
        return f"Трекер бюджета: категорий - {len(self._categories_limit)}; транзакций - {len(self._transactions)}"


    def __repr__(self):
        return f"BudgetTracker(categories_balance={self._categories_limit}, transactions={self._transactions})"