from src.domain.models.task import Task
from src.repository.task_repository import TaskRepository


class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create_task(self, task: Task) -> dict:
        return task.to_dict()

    def list_tasks(self) -> dict:
        return self.task_repository.list_tasks()

    def get_task_by_id(self, task_id: str) -> dict:
        return self.task_repository.get_task(task_id)

    def update_task(self, task_id: str, task: Task) -> dict:
        return self.task_repository.update_task(task_id, task)

    def delete_task(self, task_id: str) -> dict:
        return self.task_repository.delete_task(task_id)