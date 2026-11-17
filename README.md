# Employee Shift Scheduler

A lightweight Python command-line application for managing restaurant employee schedules, detecting shift conflicts, and persisting shift data in JSON format.

## Features

- **Chronological Weekly View**: Displays all scheduled shifts sorted automatically from Monday to Sunday.
- **Conflict Detection**: Prevents double-booking an employee on the same day (case-insensitive check).
- **Input Validation**: Validates days of the week before adding new entries.
- **JSON Persistence**: Automatically loads and saves schedule updates to `shifts.json`.
- **Automated Unit Tests**: Includes a `unittest` suite covering sorting, validation, and conflict logic.

## Project Structure

```text
employee-shift-scheduler/
├── scheduler.py        # Core scheduling logic and interactive CLI
├── shifts.json         # Initial dataset of restaurant employee shifts
├── test_scheduler.py   # Automated unit tests
├── .gitignore          # Standard Python ignore rules
└── README.md           # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.8 or higher (uses standard library modules only: `json`, `os`, `unittest`).

### Run the Application
```bash
python scheduler.py
```

### Run Unit Tests
```bash
python -m unittest test_scheduler.py
```
