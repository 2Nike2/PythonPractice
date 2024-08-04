from copy import deepcopy
from typing import Any

from tasks.models import Task

class InMemoryRepository:
    _store: dict[str, Any] = {}

    @classmethod
    def find_by_id(cls, id:str) -> Task:
        task = cls._store.get(id)
        if task is None:
            raise Exception(f"Task not found: {id}")
        
        return task
    
    @classmethod
    def find_all(cls) -> list[Task]:
        tasks = list(cls._store.values()) 
        return tasks
    
    @classmethod
    def save(cls, task: Task) -> None:
        cls._store[task.id] = deepcopy(task)

    @classmethod
    def delete(cls, task: Task) -> None:
        del cls._store[task.id]
        