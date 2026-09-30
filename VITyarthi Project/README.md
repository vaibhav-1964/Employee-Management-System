# Employee Salary Management System

## Overview
A command-line Python application for registering employees, managing logins with role-based permissions (employee vs. admin), updating and deleting records, and generating basic payroll reports. Employee data persists between sessions using JSON file storage.

## Features
- **Employee registration** — auto-generates a unique employee ID from the employee's name and department
- **Login system** — separate access for employees and an admin account
- **Role-based permissions** — employees can only view/update/delete their own record; only admin can change salary or view reports
- **View records** — list all employees, or view a single employee's own details
- **Update records** — change name, department, or password (salary is admin-only)
- **Delete records** — remove an employee's account (self or admin only)
- **Reports (admin only)** — total payroll and totals broken down by department
- **Persistent storage** — all data is saved to `employees.json` and reloaded automatically on the next run

## Technologies / Tools Used
- Python 3
- Built-in modules: `json` (data persistence), `os` (file existence checks)

## Project Structure
```
project/
├── data.py                 # Shared data: employees dict, salary/bonus constants, admin password
├── employee_functions.py   # All core functions: register, login, update, delete, reports, save/load
├── main.py                 # Entry point — menu loop that ties everything together
├── employees.json          # Auto-generated data file (created on first run)
└── README.md
```

## How to Install & Run
1. Make sure Python 3 is installed on your machine.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:
   ```
   python main.py
   ```
5. Follow the on-screen menu to register, log in, and manage employee records.

## Testing Instructions
Manually test the following flows:
1. **Register** a new employee and confirm a unique ID is generated.
2. **Restart the program** and confirm the employee is still there (tests persistence).
3. **Log in** as that employee and view your own details.
4. **Update** your name, department, and password — confirm each change is saved.
5. **Attempt to update another employee's record** — should be blocked.
6. **Log in as admin** and view payroll reports.
7. **Delete** an employee and confirm they no longer appear in the employee list.

## Future Enhancements
- Input validation with `try/except` for non-numeric input
- Fix duplicate-ID risk after deleting and re-registering employees
- Password hashing instead of plain-text storage
- Export reports to a file
