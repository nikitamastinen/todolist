from enum import Enum


class Status(Enum):
    INCOMPLETED = 'incompleted'
    COMPLETED = 'completed'
    ALL = 'all'


class Task:
    def __init__(self, status, name):
        self.status = status
        self.name = name

    def __eq__(self, other):
        return self.status == other.status and self.name == other.name


class TodoList:
    def __init__(self):
        self.tasks = []
        self.status = Status.INCOMPLETED.value

    def add_task(self, name):
        if name is not None and len(name) > 0:
            self.tasks.append(Task(Status.INCOMPLETED.value, name))

    def complete_task(self, position):
        if position is not None and int(position) < len(self.tasks):
            self.tasks[int(position)].status = Status.COMPLETED.value

    def change_status(self, status):
        if status not in [v.value for v in Status.__members__.values()]:
            return
        if status is not None:
            self.status = status
