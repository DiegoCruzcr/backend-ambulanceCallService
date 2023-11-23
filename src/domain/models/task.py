from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid

@dataclass
class Task:
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    task_name: str = None
    task_description: str = None
    task_status: str = 'PENDING'
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    associated_users: list = field(default_factory=lambda: [])

    def to_dict(self):
        """Return a dictionary representation of the object"""
        return {
            'task_id': self.task_id,
            'task_name': self.task_name,
            'task_description': self.task_description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'associated_users': self.associated_users
        }

    @staticmethod
    def from_dict(task: dict):
        """Return an AmbulanceCall object from a dictionary"""
        return Task(
            task_id=task.get('task_id', str(uuid.uuid4())),
            task_name=task.get('task_name'),
            task_description=task.get('task_description'),
            created_at=task.get('created_at'),
            updated_at=task.get('updated_at'),
            associated_users=task.get('associated_users', [])
        )