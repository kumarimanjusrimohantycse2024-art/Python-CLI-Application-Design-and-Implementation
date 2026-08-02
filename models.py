from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, Any

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: str = datetime.now().isoformat(timespec="seconds")
    due_date: str = ""          # e.g. "2025-12-10"
    priority: str = "Medium"    # "Low", "Medium", "High"
    category: str = "General"   # e.g. "Study", "Work", "Personal"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Task":
        return Task(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False),
            created_at=data.get("created_at", datetime.now().isoformat(timespec="seconds")),
            due_date=data.get("due_date", ""),
            priority=data.get("priority", "Medium"),
            category=data.get("category", "General"),
        )