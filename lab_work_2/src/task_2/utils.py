from budget_tracker import BudgetTracker
from transaction import Transaction
from transaction_type import TransactionType
from category import Category

cat0 = Category('школа')
cat = Category('категория', 5000)
b = BudgetTracker(1000)
tr = Transaction('aefa', 2500, TransactionType.expense, 'категория')

print(tr)
print(repr(tr))
print(b._categories)
b.add_category(cat0)
b.add_category(cat)
print(b._categories)

b.add_transaction(tr)
print(b._transactions)
print(b.is_over_limit(tr))
b.add_transaction(tr)
print(b.is_over_limit(tr))
