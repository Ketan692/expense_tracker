# 📦 Smart Expense Tracker API

A **production-ready Expense Tracking and Budget Management API** built using Django Rest Framework.
This project provides transaction management, financial analytics, and budget monitoring with secure JWT authentication.

---

## 🚀 Features

### 💰 Expense & Income Management

* Create and manage income and expense transactions
* Categorize transactions (Food, Rent, Travel, etc.)
* User-specific data isolation

---

### 📊 Analytics APIs

* Monthly summary (income, expense, savings)
* Category-wise expense breakdown
* Monthly spending trends

---

### 💸 Budget Management

* Set monthly budgets per category
* Prevent duplicate budgets per user/category/month
* Real-time **budget exceeded warning system**

---

### 🔐 Authentication

* JWT-based authentication
* Secure API access using access tokens

---

### 📄 API Documentation

* Swagger UI for testing and exploration

---

## 🧰 Tech Stack

* Python 3.x
* Django
* Django Rest Framework
* Simple JWT
* drf-spectacular (Swagger)
* SQLite / PostgreSQL

---

## 📂 Project Structure

```bash
expense-tracker-api/
│── analytics/
│── budget/
│── transactions/
│── expense_tracker/
│── manage.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Ketan692/expense_tracker.git
cd expense_tracker
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

---

### 5️⃣ Run Migrations

```bash
python manage.py migrate
```

---

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

### 7️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🔐 Authentication (JWT)

### Get Token

```
POST /api/token/
```

### Refresh Token

```
POST /api/token/refresh/
```

### Use Token

```
Authorization: Bearer <access_token>
```

---

## 📦 Core API Endpoints

### 🔹 Transactions

* `GET /api/transactions/`
* `POST /api/transactions/`

Filter examples:

```
/api/transactions/?type=EXPENSE
/api/transactions/?category=1
/api/transactions/?start_date=2026-01-01&end_date=2026-01-31
```

---

### 🔹 Categories

* `GET /api/categories/`
* `POST /api/categories/`

---

### 🔹 Budgets

* `GET /api/budgets/`
* `POST /api/budgets/`

---

## 📊 Analytics Endpoints

### 💰 Monthly Summary

```
GET /api/analytics/summary/?year=2026&month=3
```

---

### 📊 Category Breakdown

```
GET /api/analytics/category/
```

---

### 📈 Monthly Trends

```
GET /api/analytics/trends/
```

---

## ⚙️ Business Logic Highlights

* Category type must match transaction type
* Budget is unique per user, category, and month
* Transactions are NOT blocked when budget exceeds
* System returns warning:

```json
{
  "warning": "⚠️ Budget exceeded for this category."
}
```

---

## 📄 API Documentation

Swagger UI:

```
/api/docs/
```

Schema:

```
/api/schema/
```

---

## 🔒 Environment Variables

* `.env` file is excluded from Git
* Use `.env.example` for reference

---

## 🧠 Future Improvements

* Email alerts for budget exceed
* Frontend dashboard (React)
* Docker deployment

---

## 👨‍💻 Author

**Ketan**

GitHub: https://github.com/Ketan692

---

## 📜 License

MIT License
