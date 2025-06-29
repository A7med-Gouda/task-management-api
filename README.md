# 📋 Task Management API

A modern and lightweight Task Management API built with **FastAPI**, **SQLModel**, and **Pydantic**.  
This project supports task creation, updating, filtering, sorting, and more – ideal for learning and real-world use.

---

## 🚀 Features

- ✅ Full **CRUD** operations
- ✅ Advanced **data validation** with Pydantic
- ✅ **Filtering** by status and priority
- ✅ **Search** and **sorting**
- ✅ **Pagination**
- ✅ Auto-generated Swagger documentation
- ✅ **Error handling** with clear messages
- ✅ Docker support
- ✅ `.env` environment configuration
- ✅ Basic unit testing with pytest

---

## 🏗️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [SQLite](https://sqlite.org/)
- [Docker](https://www.docker.com/)
- [pytest](https://docs.pytest.org/)

---

## 📂 Project Structure

task-management-api/
├── app/
│ ├── main.py # Entry point
│ ├── models.py # Task model and enums
│ ├── schemas.py # Pydantic models
│ ├── crud.py # Business logic
│ ├── routes.py # API endpoints
│ └── database.py # DB session config
├── tests/ # Unit tests
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md

yaml
Copy
Edit



---

## 🧪 Run Locally

### 🔹 Prerequisites

- Python 3.9+
- [Docker](https://www.docker.com/products/docker-desktop) (optional)

### 🔹 Clone the Repository

```bash
git clone https://github.com/A7med-Gouda/task-management-api.git
cd task-management-api
