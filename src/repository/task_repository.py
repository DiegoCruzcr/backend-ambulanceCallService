from src.domain.models.task import Task
from src.repository.mongo_client import MongoClient


class TaskRepository:
    def __init__(self, database: MongoClient):
        self.database = database

    def create_task(self, task: Task):
        task_id = self.database.create_task(task)

        return task_id

    def list_tasks(self):
        tasks = self.database.list_tasks()

        return list(tasks)

    def get_task(self, task_id: str):
        task = self.database.get_task(task_id)

        return task

    def update_task(self, task_id: str, task: Task):
        self.database.update_task(task_id, task)

    def delete_task(self, task_id: str):
        self.database.delete_task(task_id)

    def get_task_by_associated_user_id(self, user_id: str):
        task = self.database.get_task_by_associated_user_id(user_id)

        return task