# VitalLog - Patient Management System

A lightweight Django web application designed for efficient patient record management. This project serves as a foundation for a hospital information system, currently focusing on secure data entry and validation.

## 🚀 Features

### Current Functionality
- **Secure Authentication**: Built using Django's robust `contrib.auth` system:
    - **Register**: Secure user signup with password hashing (`UserCreationForm`).
    - **Login/Logout**: Session-based authentication (`AuthenticationForm`).
    - **Access Control**: value-protected views (Dashboard, Add Patient) accessible only to logged-in users.
- **Patient Dashboard**:
    - **View Records**: A centralized dashboard displaying a list of all registered patients (`/dashboard/`).
- **Patient Registration**: An intuitive form interface to add new patients.
- **Robust Data Validation**: Custom server-side validation rules ensuring data integrity:
    - **Email**: Enforces `@gmail.com` domain.
    - **Phone**: Validates digit-only input.
    - **Age**: Restricts input to 0-120 range.
    - **Name**: Minimum character length enforcement.

### 🔄 User Flow
`Login / Signup`  ➡️  `Dashboard (View Patients)`  ➡️  `Add New Patient`  ➡️  `Logout`

### 📂 Project Structure
```
VitalLog-Django/
├── hospital_project/       # Main Project Directory
│   ├── app/                # Core Application (Models, Forms, Views)
│   ├── templates/          # HTML Templates (Login, Dashboard, Form)
│   ├── manage.py           # Django Management Script
│   └── ...
└── README.md               # Documentation
```

### 🚧 Roadmap (Upcoming Features)
The project is actively being developed into a full CRUD application.
- **Update**: Interface to edit existing patient details.
- **Delete**: Functionality to remove discharged or erroneous records.
- **Search & Filter**: Ability to look up patients by ID, name, or medical condition.
- **Detailed View**: dedicated page for comprehensive patient history.

## 🛠️ Tech Stack
- **Backend**: Python 3.x, Django 5.x
- **Authentication**: Django Contrib Auth
- **Database**: SQLite (default)
- **Frontend**: HTML5, Django Templates

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/anugrahk21/VitalLog-Django.git
   cd VitalLog-Django
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Navigate to the project and run migrations**
   ```bash
   cd hospital_project
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Optional - for Admin Panel)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and visit: `http://127.0.0.1:8000/login/`

---
*Project under active development.*
