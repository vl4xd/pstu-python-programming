import jsonpickle

from task_1.task_tracker import TaskTracker
from task_2.budget_tracker import BudgetTracker


def encode_to_json(json_path: str, instance: TaskTracker | BudgetTracker) -> None:
    """Encode TaskTracker instance to JSON file

    :param TaskTracker task_tracker: task_tracker instance to encode
    :param str json_path: path to JSON file
    :return None:
    """
    encoded_instance: str = jsonpickle.encode(instance)
    with open(json_path, 'w+') as f:
        f.write(encoded_instance)


def decode_from_json(json_path: str, instance_type: TaskTracker | BudgetTracker) -> TaskTracker | BudgetTracker:
    """Decode TaskTracker instance from JSON file

    :param str json_path: path to JSON file with encoded TaskTracker instance
    :return TaskTracker: decoded TaskTracker instance
    """
    with open(json_path, 'r+') as f:
        written_instance: str = f.read()
        if len(written_instance) == 0:
            return instance_type()
        decoded_instance: TaskTracker | BudgetTracker = jsonpickle.decode(written_instance)
    return decoded_instance