# CI/CD Pipeline for a Python Application

## Project Overview

This project demonstrates the development, testing, containerization, automation, and deployment of a Python-based REST API using FastAPI and modern DevOps practices.

The application is a Task Management API that supports Create, Read, Update, and Delete (CRUD) operations while showcasing Continuous Integration (CI), automated testing, code quality checks, Docker containerization, and cloud deployment.

The objective of the project is to implement a complete software development lifecycle workflow from development to deployment using industry-standard tools and practices.

---

# Features

## Application Features

* Task Creation
* Task Retrieval
* Individual Task Lookup
* Task Update
* Task Deletion
* Health Check Endpoint
* Request Validation
* Error Handling
* Interactive API Documentation

## DevOps Features

* Git Version Control
* GitHub Repository Management
* Automated Testing using Pytest
* Code Quality Checks using Ruff
* Continuous Integration using GitHub Actions
* Docker Containerization
* Docker Build Verification
* Cloud Deployment using Render

---

# Technology Stack

| Category             | Technology     |
| -------------------- | -------------- |
| Programming Language | Python 3.12    |
| Framework            | FastAPI        |
| Validation           | Pydantic       |
| Testing              | Pytest         |
| Linting              | Ruff           |
| Version Control      | Git            |
| Repository Hosting   | GitHub         |
| CI/CD                | GitHub Actions |
| Containerization     | Docker         |
| Deployment Platform  | Render         |

---

# Project Structure

```text
CI-CD-Pipeline-for-a-Python-Application/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── tests/
│   └── test_main.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── .dockerignore
├── pytest.ini
├── requirements.txt
├── README.md
├── DEPLOYMENT.md
├── FINAL_REPORT.md
└── .gitignore
```

---

# API Endpoints

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| GET    | /                | Root Endpoint       |
| GET    | /health          | Health Check        |
| POST   | /tasks           | Create Task         |
| GET    | /tasks           | Retrieve All Tasks  |
| GET    | /tasks/{task_id} | Retrieve Task by ID |
| PUT    | /tasks/{task_id} | Update Task         |
| DELETE | /tasks/{task_id} | Delete Task         |

---

# Running the Application Locally

## Clone Repository

```bash
git clone <repository-url>
cd CI-CD-Pipeline-for-a-Python-Application
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

### Windows

```powershell
.\venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Testing

Run automated tests:

```bash
pytest
```

Current Status:

```text
14 Tests Passed
```

Testing includes:

* Endpoint Testing
* CRUD Operation Testing
* Validation Testing
* Error Handling Testing

---

# Code Quality

Run Ruff checks:

```bash
ruff check .
```

Purpose:

* Code consistency
* Error detection
* Style enforcement
* Maintainability

---

# Continuous Integration

GitHub Actions workflow automatically performs:

* Repository Checkout
* Python Setup
* Dependency Installation
* Ruff Linting
* Pytest Execution
* Docker Image Build Verification

Workflow File:

```text
.github/workflows/ci.yml
```

---

# Docker Usage

Build Image:

```bash
docker build -t fastapi-task-manager .
```

Run Container:

```bash
docker run -p 8000:8000 fastapi-task-manager
```

---

# Live Deployment

Deployment Platform:

Render

Application URL:

https://ci-cd-pipeline-for-a-python-application.onrender.com

Health Endpoint:

https://ci-cd-pipeline-for-a-python-application.onrender.com/health

Swagger Documentation:

https://ci-cd-pipeline-for-a-python-application.onrender.com/docs

---

# Current Limitations

The application currently uses in-memory storage.

Data may be reset if the application service restarts.

---

# Future Improvements

* SQLite Database Integration
* SQLAlchemy ORM
* PostgreSQL Migration
* User Authentication
* JWT Authorization
* Role-Based Access Control
* Logging
* Monitoring
* Automated Deployment
* Cloud Infrastructure Expansion

---

# Author

Pilla Ravindar

Internship Project: CI/CD Pipeline for a Python Application

This project demonstrates software development and DevOps practices including API development, automated testing, CI/CD implementation, containerization, and cloud deployment.
