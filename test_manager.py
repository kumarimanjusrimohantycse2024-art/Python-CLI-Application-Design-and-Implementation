import tempfile
import unittest
from pathlib import Path

from manager import TaskManager
from storage import TaskStorage


class TaskManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.tasks_file = Path(self.temp_dir.name) / "tasks.json"
        self.manager = TaskManager(TaskStorage(str(self.tasks_file)))

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_add_task_persists_to_storage(self) -> None:
        task = self.manager.add_task("Study Python", category="Study", priority="High")
        self.assertEqual(task.id, 1)

        reloaded = TaskManager(TaskStorage(str(self.tasks_file)))
        tasks = reloaded.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Study Python")
        self.assertEqual(tasks[0].category, "Study")
        self.assertEqual(tasks[0].priority, "High")

    def test_complete_and_remove_task(self) -> None:
        task = self.manager.add_task("Write tests")
        self.assertTrue(self.manager.complete_task(task.id))
        self.assertEqual(self.manager.get_stats()["completed"], 1)

        self.assertTrue(self.manager.remove_task(task.id))
        self.assertEqual(self.manager.get_stats()["total"], 0)

    def test_filter_and_search_tasks(self) -> None:
        first = self.manager.add_task("Study algebra")
        second = self.manager.add_task("Buy groceries")
        self.manager.complete_task(second.id)

        pending = self.manager.filter_tasks("pending")
        completed = self.manager.filter_tasks("completed")
        search = self.manager.search_tasks("study")

        self.assertEqual([task.id for task in pending], [first.id])
        self.assertEqual([task.id for task in completed], [second.id])
        self.assertEqual([task.id for task in search], [first.id])


if __name__ == "__main__":
    unittest.main()
