# Problem Statement

Small organizations often need a simple way to track employee records and payroll without the overhead of a full HR platform. Manually tracking names, departments, and salaries in spreadsheets is error-prone, has no access control, and offers no built-in way to summarize payroll costs. This project addresses that gap with a lightweight, role-based employee salary management system.

## Scope of the Project
This project covers the core lifecycle of employee record management:
- Registering new employees with auto-generated IDs
- Secure login with distinct roles (employee vs. admin)
- Viewing, updating, and deleting employee records, restricted by role
- Generating basic payroll reports (total and per-department)
- Persisting all data between program runs

It is scoped as a single-organization, command-line tool. It does not include a graphical interface, multi-organization support, or integration with external payroll/tax systems.

## Target Users
- **Employees** — can register, log in, view their own record, and update their own name, department, or password.
- **Admin** — has full access: can view all records, update any employee's salary, view payroll reports, and manage any employee's account.

## High-Level Features
1. **User Management** — registration and role-based login (employee/admin)
2. **Data Input & Processing** — auto-generated employee IDs, structured record storage
3. **CRUD Operations** — create (register), read (list/show), update, and delete employee records
4. **Reporting** — total payroll and department-wise salary breakdown (admin only)
5. **Persistence** — JSON-based storage so data survives across sessions
