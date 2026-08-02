import json
from pathlib import Path
from typing import List

from models import Task

# This class handles saving and loading tasks to/from a JSON file.
class TaskStorage:
    def __init__(self, file_path: str = "tasks.json") -> None:
        # Path to the file where tasks are saved.
        self.file_path = Path(file_path)

    def load_tasks(self) -> List[Task]:
        """
        Load tasks from the JSON file.
        If the file doesn't exist or is broken, return an empty list.
        """
        if not self.file_path.exists():
            # No file yet => no tasks
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            # File is corrupted or can't be read
            return []

        tasks: List[Task] = []
        for item in data:
            try:
                tasks.append(Task.from_dict(item))
            except (KeyError, TypeError):
                # Skip any bad entries
                continue
        return tasks

    def save_tasks(self, tasks: List[Task]) -> None:
        """
        Save the list of tasks to the JSON file.
        """
        serializable = [task.to_dict() for task in tasks]
        try:
            with self.file_path.open("w", encoding="utf-8") as f:
                json.dump(serializable, f, indent=2)
        except OSError as e:
            # Simple error message if we can't save
            print(f"Warning: Could not save tasks to file: {e}")