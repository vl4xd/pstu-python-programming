from datetime import datetime

class Task:


    def __init__(self, description: str, categoty: str):
        self._description: str = description
        self._categoty: str = categoty
        self._is_done: bool = False
        self._created_at: datetime = datetime.now()
        self._finished_at: datetime = None

    @property
    def description(self):
        return self._description

    @property
    def categoty(self):
        return self._categoty

    @property
    def is_done(self):
        return self._is_done

    @property
    def created_at(self):
        return self._created_at

    @property
    def finished_at(self):
        return self._finished_at


    def complete(self):
        self._is_done = True
        self._finished_at = datetime.now()


    def _str_done_tag(self, is_done: bool):
        if is_done:
            return "[X]"
        return "[ ]"


    def __str__(self):
        return f"{self._str_done_tag(self._is_done)} {self._description} #{self._categoty}"