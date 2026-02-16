# VitalLog - Patient Management System

A lightweight Django web application designed for efficient patient record management. This project serves as a foundation for a hospital information system, currently focusing on secure data entry and validation.

## 🚀 Features

### Current Functionality
- **Patient Registration**: An intuitive form interface to add new patients to the system.
- **Robust Data Validation**: Custom server-side validation rules in `forms.py` ensure data integrity:
    - **Email**: Enforces specific domain usage (e.g., `@example.com`).
    - **Phone**: Validates that only digits are entered.
    - **Age**: Restricts input to a realistic range (0-120).
    - **Name**: Enforces minimum character length.
- **Error Handling**: Graceful error management and debug logging for form submissions.

### 🚧 Roadmap (Upcoming Features)
The project is actively being developed into a full CRUD (Create, Read, Update, Delete) application.
- **Read**: Dashboard to view a list of all registered patients.
- **Update**: Interface to edit patient details (e.g., address changes, medical history updates).
- **Delete**: functionality to remove discharged or erroneous records.
- **Search**: Ability to look up patients by ID or name.

## 🛠️ Tech Stack
- **Backend**: Python 3.x, Django 5.x
- **Database**: SQLite (default)
- **Frontend**: HTML5, Standard Django Templates

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
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and visit: `http://127.0.0.1:8000/add_patient/`

---
*Project under active development.*
