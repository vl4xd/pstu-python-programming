from datetime import datetime

class Task:

    def __init__(self, description: str, category: str) -> None:
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


    def __str_done_tag(self) -> str:
        """Display the task flag

        :param bool is_done: new completion status
        :return str: task flag
        """
        if self._is_done:
            return "[X]"
        return "[ ]"


    def __str__(self) -> str:
        return f"{self.__str_done_tag()} {self._description} #{self._category}"


    def __repr__(self) -> None:
        return f"Task(description={self._description}, category={self._category}, is_done={self._is_done}, created_at={self._created_at}, finished_at={self._finished_at})"