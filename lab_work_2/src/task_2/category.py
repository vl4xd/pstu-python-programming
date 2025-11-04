from datetime import datetime

class Category:


    def __init__(self, name: str, limit: int = 0):
        self._name: int = name
        self._limit: int = limit
        self._created_at: datetime = datetime.now()


    def __eq__(self, other):
        if isinstance(other, Category):
            if self._name == other._name:
                return True
            return False
        if isinstance(other, str):
            if self._name == other:
                return True
            return False


    def __str__(self):
        return f"{self._name}"


    def __repr__(self):
        return f"Category(name={self._name}, limit={self._limit}, created_at={self._created_at})"