# ✅ To-Do List Manager (CLI)

A clean, modular, and production-style **command-line To-Do application** built in Python.  
Designed to demonstrate **strong fundamentals**: OOP, modular architecture, robust I/O, input validation, and clear documentation.

🙌**Try it now:**
```bash
git clone <your-repo-url>
cd todo_cli
python cli.py
```

---

## 📌 About This Project

This CLI app allows users to **add, list, edit, complete, delete, filter, and search tasks** — each with title, description, due date, priority, category, and status. All data is persisted in a JSON file (`tasks.json`), ensuring reliability across sessions.

Built with **only Python standard libraries**, this project emphasizes:
- Clean, readable, and maintainable code
- Modular architecture (separation of concerns)
- Defensive programming and graceful error handling
- Real-world design patterns suitable for production code

---

## ✨ Features

- ➕ **Add tasks** with title, description, due date, priority (Low/Medium/High), and category (Study/Work/Personal/General)
- 📋 **List all tasks** in a clean table with ID, title, status, priority, due date, category, and timestamp
- ✅ **Mark tasks as completed**
- ✏️ **Edit tasks** (title, description, due date, priority, category)
- 🗑️ **Remove tasks** with confirmation
- 🔍 **Search tasks** by title (case-insensitive)
- 🧭 **Filter tasks** by status: All / Pending / Completed
- 📊 **Show statistics**: total, completed, and pending tasks
- 💾 **Persistent storage** using `tasks.json`

---

## 🏗️ Architecture
This project follows a **modular, layered architecture** for clarity and scalability:

todo_cli/
├── models.py # Task dataclass (domain model)
├── storage.py # JSON file I/O (persistence layer)
├── manager.py # Business logic (service layer)
├── cli.py # User interface (presentation layer)
├── tasks.json # Auto-generated data file
├── test_input.py # Optional test script
└── README.md # This file


**Design principles applied:**
- **Separation of Concerns**: Data, logic, storage, and UI are cleanly separated
- **Single Responsibility**: Each module has one clear purpose
- **Defensive Programming**: Input validation and error handling throughout
- **Extensibility**: Easy to add new features (sorting, export, categories, etc.)

---

## 🛠️ Technologies Used

- **Language:** Python 3.8+
- **Standard Libraries:** `dataclasses`, `json`, `pathlib`, `datetime`
- **No external dependencies** — runs anywhere Python is installed

---

## 🌠 Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation
```bash
# Clone the repository
git clone <your-repo-url>

# Navigate to project folder
cd todo_cli
```

### Run the Application
```bash
python cli.py
```

Follow the on-screen menu (options 1–9) to interact with the app.

---

## 🧪 Sample Usage

```text
=== To-Do List Manager ===
1. Add task
2. List all tasks
3. Mark task as completed
4. Remove task
5. Edit task
6. Filter tasks
7. Search tasks
8. Show stats
9. Exit

Enter your choice (1-9): 1
Enter task title: Study Python
Enter task description (optional): CLI app practice
Enter due date (YYYY-MM-DD, optional): 2026-08-10
Choose priority:
1. Low
2. Medium
3. High
Enter priority choice (1-3, default=2): 3
Choose category:
1. Study
2. Work
3. Personal
4. General
Enter category choice (1-4, default=4): 1
Task added with ID 1.
```

---

## 📂 Project Structure

| File          | Purpose                                      |
|---------------|----------------------------------------------|
| `models.py`   | Task dataclass with serialization methods    |
| `storage.py`  | JSON file load/save with error handling      |
| `manager.py`  | Core business logic (CRUD + filter + search) |
| `cli.py`      | Menu-driven CLI with input validation        |
| `tasks.json`  | Persistent task data                         |
| `test_input.py` | Optional test script for input validation  |
| `README.md`   | Project documentation                        |

---

## 🎯 What This Project Demonstrates

✅ **Object-Oriented Design** – Clean class structure with clear responsibilities  
✅ **Modular Architecture** – Separation of data, logic, storage, and UI  
✅ **Robust Error Handling** – Graceful handling of invalid input and file errors  
✅ **Input Validation** – Safe, user-friendly prompts and guards  
✅ **Code Readability** – Clear naming, comments, and structure  
✅ **Production-Ready Mindset** – Designed for maintainability and extension  

---

## 📬 Contact

**[MANJUSRI MOHANTY]**  
📧 [kumarimanjusrimohantycse2024@gmail.com]  
🔗 [GITHUB : https://github.com/kumarimanjusrimohantycse2024-art] | [LINKEDIN : https://www.linkedin.com/in/m-pihu-mohanty-23200821z0?utm_source=share_via&utm_content=profile&utm_medium=member_android ]

---

## 📄 License

This project is open-source and available for educational and portfolio purposes.

---

> 💡 **Note for Recruiters:** This project was built from scratch to demonstrate strong Python fundamentals, clean architecture, and a production-ready mindset. I'm actively seeking opportunities to apply these skills in a professional environment.

This project follows a **modular, layered architecture** for clarity and scalability:

