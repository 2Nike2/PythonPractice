from datetime import datetime
from typing import Optional

from tasks.models import Status, Task
from tasks.repositories import InMemoryRepository

class TaskService:
    def __init__(self, repo: type[InMemoryRepository]) -> None:
        self._repo = repo

    @property
    def repo(self) -> type[InMemoryRepository]:
        return self._repo
    
    def find(self, id: str) -> Task:
        return self._repo.find_by_id(id)
    
    def find_all(self) -> list[Task]:
        return self._repo.find_all()
    
    def create(self, *, title: str, description: Optional[str] = None) -> Task:
        task = Task(title=title, description=description)
        self._repo.save(task)
        return task
    
    def update(self, *, id:str, status: Status) -> Task:
        task = self._repo.find_by_id(id)
        task.status = status
        task.update_at = datetime.now()
        self._repo.save(task)

        return task
    
    def delete(self, name: str) -> None:
        task = self._repo.find_by_id(name)
        self._repo.delete(task)

        return task
        