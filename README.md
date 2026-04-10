# HR Management System — Odoo 18 Custom Module

A full-featured Human Resources Management module built for Odoo 18, covering the complete employee lifecycle from recruitment through offboarding.

---

## Features

### Core Employee Lifecycle
- Employee profiles with auto-generated IDs (`EMP0001`, `EMP0002`, ...)
- Age auto-computed from date of birth
- Employment detail tracking per employee (contract type, salary, probation dates)

### Organisational Structure
- Departments with parent/child hierarchy
- Designations linked to departments
- Work locations

### Time & Attendance
- Daily attendance records with check-in / check-out
- Leave types and leave policies
- Leave requests with approval workflow (Draft → Submitted → Approved/Rejected)

### Payroll
- Salary structures with allowances and deductions
- Auto-computed gross salary, total deductions, and net salary
- Pay slips with status workflow (Draft → Confirmed → Paid)

### Recruitment & Onboarding
- Job openings with vacancy tracking
- Candidate pipeline (New → Screening → Interview → Offered → Hired/Rejected)
- Offer letters linked to candidates and positions

### Performance
- Goal tracking with progress percentage
- Performance reviews with ratings (Poor → Excellent)

### Documents & Compliance
- Employee document storage (ID, passport, contracts, certificates)
- Disciplinary records with incident classification

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Odoo 18 ORM |
| Frontend | Odoo QWeb XML Views |
| Database | PostgreSQL |
| Messaging | Odoo mail.thread (chatter + activity tracking) |

---

## Installation

### Requirements
- Ubuntu 20.04+ or WSL2
- Python 3.10+
- PostgreSQL 14+
- Odoo 18 source

### Setup

1. Clone this repo into your custom addons folder:
```bash
git clone https://github.com/YOUR_USERNAME/hr_management.git ~/odoo18/custom_addons/hr_management
```

2. Activate your virtual environment:
```bash
source ~/odoo18/odoo-venv/bin/activate
```

3. Install the module:
```bash
cd ~/odoo18/odoo
./odoo-bin \
  --addons-path=/home/YOUR_USER/odoo18/odoo/addons,/home/YOUR_USER/odoo18/custom_addons \
  -d odoo18_db \
  -i hr_management \
  --stop-after-init
```

4. Start Odoo:
```bash
./odoo-bin \
  --addons-path=/home/YOUR_USER/odoo18/odoo/addons,/home/YOUR_USER/odoo18/custom_addons \
  -d odoo18_db
```

5. Open your browser at `http://localhost:8069`

---

## Module Structure
hr_management/
├── init.py
├── manifest.py
├── demo/
│   └── demo.xml
├── models/
│   ├── init.py
│   ├── attendance.py
│   ├── department.py
│   ├── designation.py
│   ├── document.py
│   ├── employee.py
│   ├── employment_detail.py
│   ├── leave.py
│   ├── payroll.py
│   ├── performance.py
│   ├── recruitment.py
│   └── work_location.py
├── security/
│   └── ir.model.access.csv
└── views/
├── attendance_views.xml
├── department_views.xml
├── designation_views.xml
├── document_views.xml
├── employee_views.xml
├── employment_detail_views.xml
├── leave_views.xml
├── menu.xml
├── payroll_views.xml
├── performance_views.xml
├── recruitment_views.xml
├── sequence.xml
└── work_location_views.xml
---

## Author

**Mutembei Nicholas**  
Odoo Developer  
Built with Odoo 18 | Python 3.12 | PostgreSQL
