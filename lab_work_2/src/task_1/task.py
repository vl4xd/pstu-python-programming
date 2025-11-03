from datetime import datetime

class Task:

    def __init__(self, description: str, category: str):
        """Task initialisation

        :param str description: task description
        :param str categoty: task category
        """

        self._description: str = description
        self._category: str = category
        self._is_done: bool = False
        self._created_at: datetime = datetime.now()
        self._finished_at: datetime = None

    @property
    def description(self) -> str:
        """Get a description

        :return str: task description
        """
        return self._description

    @property
    def categoty(self) -> str:
        """Get a category

        :return str: task category
        """
        return self._category

    @property
    def is_done(self) -> bool:
        """Get a completion status

        :return bool: task completion status
        """
        return self._is_done

    @property
    def created_at(self) -> datetime:
        """Get a creation datetime

        :return datetime: task creation datetime
        """
        return self._created_at

    @property
    def finished_at(self) -> datetime:
        """Get a completion datetime

        :return datetime: task completion datetime
        """
        return self._finished_at


    def complete(self) -> None:
        """Complete the task
        """
        self._is_done = True
        self._finished_at = datetime.now()


    def _str_done_tag(self, is_done: bool) -> str:
        """Display the task flag

        :param bool is_done: new completion status
        :return str: task flag
        """
        if is_done:
            return "[X]"
        return "[ ]"


    def __str__(self):
        return f"{self._str_done_tag(self._is_done)} {self._description} #{self._categoty}"