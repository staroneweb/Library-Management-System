📚 Library Management System (Django + DRF)

A REST-based Library Management System built using **Django**, **Django REST Framework**, and **PostgreSQL**.
This project was developed as part of a backend technical assessment to demonstrate real-world API design, authentication, authorization, and database modeling.

The system allows users to browse and borrow books, while admins can manage books, users, and loan records.

### ***Features***

### 👤 User Roles

* **Anonymous Users**

  * Browse and view books
* **Registered Users**

  * Borrow available books
  * Return borrowed books
  * View their loan history
* **Admin Users**

  * Full CRUD on books
  * Manage users
  * View and manage loan records

### 🔐 Authentication & Authorization

* User registration & login APIs
* JWT authentication (Access & Refresh tokens)
* Role-based permissions:

  * Admin vs normal user vs anonymous

### 📖 Book Management

* Add, update, delete books (Admin only)
* Book fields:

  * Title, Author, ISBN
  * Page count
  * Genre, Description (optional)
  * Availability status
  * Created & updated timestamps

🔄 Borrow & Return System

* Users can borrow only available books
* Users can return borrowed books
* Loan history is tracked with timestamps

---

### 🧾 Loan Tracking

Each loan stores:

* User
* Book
* Borrow date
* Return date

### 🛠 Tech Stack

* **Backend:** Django 6.0, Django REST Framework
* **Database:** PostgreSQL
* **Authentication:** JWT (SimpleJWT)
* **Documentation:** Swagger (drf-yasg)
* **Environment Management:** python-dotenv
* **Deployment Ready:** Docker + PostgreSQL


### ⚙️ Project Setup

1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Create `.env` File

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key
DEBUG=True

POSTGRES_DB=lms
POSTGRES_USER=postgres
POSTGRES_PASSWORD=****************
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

ACCESS_TOKEN_LIFETIME_MINUTES=60
REFRESH_TOKEN_LIFETIME_DAYS=7

ALLOWED_HOSTS=127.0.0.1,localhost
```

5️⃣ Configure PostgreSQL

* Create a database named: `lms`
* Make sure PostgreSQL is running
* Update `.env` with correct credentials

6️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
7️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

8️⃣ Run the Server

```bash
python manage.py runserver
```

### 📑 API Documentation (Swagger)

Swagger UI is available at:

```
http://127.0.0.1:8000/swagger/
```

### From Swagger you can:

* Register users
* Login users
* Manage books
* Borrow & return books
* View loan history

### 🔑 JWT Authentication Flow

1. Register → `/api/auth/register/`
2. Login → `/api/auth/login/`
3. Use **ACCESS token** for secured APIs
4. Refresh access token → `/api/auth/refresh/`
5. Logout (optional)

### 📬 API Endpoints Summary

Auth

* `POST /api/auth/register/`
* `POST /api/auth/login/`
* `POST /api/auth/refresh/`

Books

* `GET /api/books/`
* `GET /api/books/<id>/`
* `POST /api/books/` (Admin only)
* `PUT /api/books/<id>/` (Admin only)
* `DELETE /api/books/<id>/` (Admin only)

Loans

* `POST /api/loans/borrow/`
* `POST /api/loans/return/`
* `GET /api/loans/`

### 🧪 Testing (Planned)

* Unit tests for:

  * Models
  * Serializers
  * Views
* Integration tests:

  * Borrow flow
  * Return flow
  * JWT authentication
* Coverage report using `coverage`

### Test Coverage

This project uses **pytest + pytest-django + coverage** for automated testing.

Current test coverage:

- **Overall Coverage: 94%**
- Auth, Books, and Loans modules are fully tested
- Unit + integration tests are included

To run tests with coverage:

```bash
coverage run -m pytest
coverage report
coverage html



🐳 Docker Support (Planned)

* Dockerfile for Django app
* Docker-compose for Django + PostgreSQL
* Single-command setup using:

  ```bash
  docker-compose up --build
  ```
