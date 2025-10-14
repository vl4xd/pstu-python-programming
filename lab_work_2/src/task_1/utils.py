import os
import jsonpickle

from task import Task
from task_tracker import TaskTracker

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_JSON_PATH = os.path.join(SCRIPT_DIR, 'tasks.json')


def encode_to_json(task_tracker: TaskTracker, json_path: str) -> None:
        encoded_instance: str = jsonpickle.encode(task_tracker)
        with open(json_path, 'w+') as f:
            f.write(encoded_instance)


def decode_from_json(json_path: str) -> TaskTracker:
    with open(json_path, 'r+') as f:
        written_instance: str = f.read()
        if len(written_instance) == 0:
             return TaskTracker()
        decoded_instance: TaskTracker = jsonpickle.decode(written_instance)
    return decoded_instance

t = Task('fff', 'pstu')
t2 = Task('aefanelfk', 'school')
t3 = Task('aefkan', 'home')
t4 = Task('aefkan', 'pstu')

tt = TaskTracker()
tt.add_task(t)
tt.add_task(t2)
tt.add_task(t3)
tt.add_task(t4)
tt.complete_task(4)

print(tt.str_sorted_by_date())
print(tt.str_sorted_by_date(True))
print(tt.str_sorted_by_category())
print(tt.str_sorted_by_category(True, unfinished=True, finished=False))
print(tt.str_by_category('pstu'))
print(tt.str_by_category('pstu', finished=False))