from task import Task

class TaskTracker:

    def __init__(self):
        self._id: int = 1
        self._tasks: dict[int, Task] = {}


    def add_task(self, task: Task):
        self._tasks[self._id] = task
        self._id += 1


    def complete_task(self, id: int):

        try:
            self._tasks[id].complete()
        except KeyError:
            raise KeyError("the task ID does not exist")


    def get_categories_tasks(self) -> set[str]:

        categories: set[str] = set()

        for task in self._tasks.values():
            categories.add(task._categoty)

        return categories


    def _str_sort_tag(self, reverse: bool) -> str:

        if reverse:
            return "↓"

        return "↑"


    def str_sorted_by_date(self, reverse: bool = False, unfinished: bool = True, finished: bool = True) -> str:

        string_instance = f"Список задач (Время {self._str_sort_tag(reverse)}):\n"

        sorted_tasks = dict(sorted(self._tasks.items(), key=lambda item: item[0], reverse=reverse))

        for id, task in sorted_tasks.items():
            if not task._is_done and not unfinished:
                continue
            if task._is_done and not finished:
                continue
            string_instance += f"{id} - {task}\n"

        return string_instance


    def str_sorted_by_category(self, reverse: bool = False, unfinished: bool = True, finished: bool = True) -> str:

        string_instance = f"Список задач (Категория {self._str_sort_tag(reverse)}):\n"

        def select_category(tasks_item: tuple[int, Task]):
            return tasks_item[1]._category

        sorted_tasks = dict(sorted(self._tasks.items(), key=select_category, reverse=reverse))

        for id, task in sorted_tasks.items():
            if not task._is_done and not unfinished:
                continue
            if task._is_done and not finished:
                continue
            string_instance += f"{id} - {task}\n"

        return string_instance


    def str_by_category(self, category: str, unfinished: bool = True, finished: bool = True) -> str:

        string_instance = f"Список задач (#{category}):\n"

        for id, task in self._tasks.items():
            if not task._is_done and not unfinished:
                continue
            if task._is_done and not finished:
                continue
            if task._category == category:
                string_instance += f"{id} - {task}\n"

        return string_instance


    def __str__(self):
        return f"TaskTracker with {len(self._tasks)} tasks"


    def __repr__(self):
        return f"TaskTracker(id={self._id}, tasks={self._tasks})"
