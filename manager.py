from typing import List, Optional

from models import Task
from storage import TaskStorage


class TaskManager:
    def __init__(self, storage: TaskStorage) -> None:
        self._storage = storage
        self._tasks: List[Task] = self._storage.load_tasks()
        self._next_id = self._calculate_next_id()

    def _calculate_next_id(self) -> int:
        if not self._tasks:
            return 1
        return max(task.id for task in self._tasks) + 1

    def list_tasks(self) -> List[Task]:
        return list(self._tasks)

    def add_task(
        self,
        title: str,
        description: str = "",
        due_date: str = "",
        priority: str = "Medium",
        category: str = "General",
    ) -> Task:
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            category=category,
        )
        self._tasks.append(task)
        self._next_id += 1
        self._storage.save_tasks(self._tasks)
        return task

    def find_task(self, task_id: int) -> Optional[Task]:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id: int) -> bool:
        task = self.find_task(task_id)
        if task is None:
            return False
        task.completed = True
        self._storage.save_tasks(self._tasks)
        return True

    def remove_task(self, task_id: int) -> bool:
        task = self.find_task(task_id)
        if task is None:
            return False
        self._tasks.remove(task)
        self._storage.save_tasks(self._tasks)
        return True

    def edit_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[str] = None,
        priority: Optional[str] = None,
        category: Optional[str] = None,
    ) -> bool:
        """
        Edit an existing task.
        For each field, if you pass None, it will not be changed.
        Returns True if the task was found and updated, False otherwise.
        """
        task = self.find_task(task_id)
        if task is None:
            return False

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if due_date is not None:
            task.due_date = due_date
        if priority is not None:
            task.priority = priority
        if category is not None:
            task.category = category

        self._storage.save_tasks(self._tasks)
        return True

    def filter_tasks(self, status: str) -> List[Task]:
        """
        Filter tasks by status.
        status can be: "all", "pending", "completed"
        """
        if status == "pending":
            return [t for t in self._tasks if not t.completed]
        elif status == "completed":
            return [t for t in self._tasks if t.completed]
        else:  # "all"
            return list(self._tasks)

    def search_tasks(self, text: str) -> List[Task]:
        """
        Search tasks whose title contains the given text (case-insensitive).
        """
        text_lower = text.lower()
        return [t for t in self._tasks if text_lower in t.title.lower()]

    def get_stats(self) -> dict:
        """
        Return simple statistics:
        - total number of tasks
        - number of completed tasks
        - number of pending tasks
        """
        total = len(self._tasks)
        completed = sum(1 for t in self._tasks if t.completed)
        pending = total - completed
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
        }