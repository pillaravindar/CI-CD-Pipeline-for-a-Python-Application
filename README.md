# CI/CD Pipeline for a Python Application

## Project Overview

This project demonstrates the development of a production-style Python application using **FastAPI** along with modern **DevOps practices** including automated testing, code quality checks, continuous integration, and Docker containerization.

The application is a Task Management REST API that allows users to create, retrieve, update, and delete tasks while showcasing a complete CI/CD workflow.

---

# Features

## Application Features

* Create Tasks
* Retrieve All Tasks
* Retrieve Individual Tasks
* Update Existing Tasks
* Delete Tasks
* Health Check Endpoint
* Input Validation using Pydantic
* Error Handling
* Automatic API Documentation

## DevOps Features

* Git Version Control
* GitHub Repository Management
* Automated Testing with Pytest
* Code Quality Checks with Ruff
* Continuous Integration using GitHub Actions
* Docker Containerization
* Docker Image Build Verification
* Deployment Preparation

---

# Technology Stack

| Component          | Technology     |
| ------------------ | -------------- |
| Backend Framework  | FastAPI        |
| Language           | Python 3.12    |
| Validation         | Pydantic       |
| Testing            | Pytest         |
| Code Quality       | Ruff           |
| Version Control    | Git            |
| Repository Hosting | GitHub         |
| CI/CD              | GitHub Actions |
| Containerization   | Docker         |

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
└── .gitignore
```

---

# API Endpoints

## Root Endpoint

Returns a welcome message.

```http
GET /
```

### Example Response

```json
{
  "message": "Hello, this is my Internship Project"
}
```

---

## Health Check Endpoint

Checks whether the application is running.

```http
GET /health
```

### Example Response

```json
{
  "status": "active"
}
```

---

## Create Task

Creates a new task.

```http
POST /tasks
```

### Request Body

```json
{
  "title": "Learn FastAPI",
  "description": "Complete FastAPI CRUD project"
}
```

### Response

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Complete FastAPI CRUD project",
  "completed": false
}
```

---

## Get All Tasks

Returns all available tasks.

```http
GET /tasks
```

---

## Get Task by ID

Returns a specific task.

```http
GET /tasks/{task_id}
```

---

## Update Task

Updates an existing task.

```http
PUT /tasks/{task_id}
```

### Request Body

```json
{
  "title": "Updated Task",
  "description": "Updated Description",
  "completed": true
}
```

---

## Delete Task

Deletes a task.

```http
DELETE /tasks/{task_id}
```

---

# Input Validation

The project uses **Pydantic** for request validation.

Validation includes:

* Required title field
* Required description field
* Empty value prevention
* Type validation
* Request structure validation

Benefits:

* Prevents invalid requests
* Improves application reliability
* Reduces runtime errors

---

# Error Handling

The API handles common errors gracefully.

Examples:

### Task Not Found

```json
{
  "detail": "Task not found"
}
```

### Validation Error

```json
{
  "detail": "Validation error"
}
```

---

# Running the Application Locally

## Clone Repository

```bash
git clone <repository-url>
cd CI-CD-Pipeline-for-a-Python-Application
```

---

## Create Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate:

```powershell
.\venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

---

## Swagger Documentation

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# Automated Testing

The project uses **Pytest** for automated testing.

Current test coverage includes:

* Root endpoint testing
* Health endpoint testing
* Task creation testing
* Task retrieval testing
* Task update testing
* Task deletion testing
* Validation testing
* Error handling testing

## Run Tests

```bash
pytest
```

Expected output:

```text
14 passed
```

---

# Code Quality Checks

The project uses **Ruff** for linting and code quality validation.

## Run Ruff

```bash
ruff check .
```

Benefits:

* Cleaner code
* Consistent style
* Early error detection
* Better maintainability

---

# Continuous Integration Pipeline

GitHub Actions is configured to automatically validate the project.

Workflow file:

```text
.github/workflows/ci.yml
```

Pipeline stages:

1. Repository Checkout
2. Python Environment Setup
3. Dependency Installation
4. Ruff Code Quality Checks
5. Pytest Execution
6. Docker Image Build Verification

If any stage fails, the workflow stops automatically.

---

# Docker Support

The application is containerized using Docker.

## Build Docker Image

```bash
docker build -t fastapi-task-manager .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 fastapi-task-manager
```

Application will be available at:

```text
http://127.0.0.1:8000
```

---

# Docker Configuration Files

## Dockerfile

Responsible for:

* Base image selection
* Dependency installation
* Application startup

## .dockerignore

Excludes unnecessary files:

```text
venv/
__pycache__/
.pytest_cache/
.git/
.env
```

---

# Deployment Preparation

The project has been prepared for deployment using Docker.

Recommended deployment platforms:

* Render
* Railway
* AWS
* Azure
* GCP

Deployment documentation will be maintained separately.

---

# Project Objectives Achieved

* FastAPI Application Development
* REST API Design
* CRUD Operations
* Input Validation
* Exception Handling
* Automated Testing
* Code Quality Automation
* Continuous Integration
* Docker Containerization
* Docker Build Verification
* Deployment Preparation

---

# Future Improvements

Potential enhancements include:

* Database Integration
* User Authentication
* Role-Based Access Control
* Logging Framework
* Monitoring
* Caching
* Background Tasks
* Automated Deployment
* Cloud Infrastructure Integration

---

Internship Project: CI/CD Pipeline for a Python Application

Built to demonstrate both Software Development and DevOps practices using modern Python tooling.
