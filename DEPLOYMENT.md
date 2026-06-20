# Deployment Guide

## Overview

This document describes the deployment process used for the CI/CD Pipeline for a Python Application project.

The application is deployed as a Docker container on Render and is publicly accessible through a live URL.

---

# Deployment Platform

Platform:

Render

Deployment Method:

Docker-Based Deployment

---

# Deployment Architecture

```text
Developer
    ↓
Git Push
    ↓
GitHub Repository
    ↓
Render
    ↓
Docker Build
    ↓
Container Startup
    ↓
Live Application
```

---

# Deployment Files

The following files are used during deployment:

```text
Dockerfile
requirements.txt
app/main.py
.github/workflows/ci.yml
```

---

# Docker Configuration

Dockerfile Responsibilities:

* Define Python Runtime
* Install Dependencies
* Copy Project Files
* Expose Application Port
* Start FastAPI Application

Application Startup Command:

```dockerfile
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

# Pre-Deployment Verification

Before deployment, the following checks should pass:

## Automated Tests

```bash
pytest
```

## Code Quality

```bash
ruff check .
```

## Docker Build

```bash
docker build -t fastapi-task-manager .
```

## Docker Run

```bash
docker run -p 8000:8000 fastapi-task-manager
```

---

# Live Deployment Information

Application URL:

https://ci-cd-pipeline-for-a-python-application.onrender.com

Health Endpoint:

https://ci-cd-pipeline-for-a-python-application.onrender.com/health

Swagger Documentation:

https://ci-cd-pipeline-for-a-python-application.onrender.com/docs

---

# Deployment Verification

Successful deployment can be verified by:

### Root Endpoint

```text
/
```

### Health Endpoint

```text
/health
```

Expected Response:

```json
{
  "status": "active"
}
```

### API Documentation

```text
/docs
```

---

# Continuous Deployment Workflow

The deployment workflow follows:

```text
Code Changes
     ↓
Git Commit
     ↓
Git Push
     ↓
GitHub Repository Update
     ↓
Render Detects Changes
     ↓
Docker Image Build
     ↓
Application Deployment
```

---

# Known Limitation

The application currently uses in-memory storage.

Task data may not persist if the service restarts.

This limitation is planned to be addressed through future database integration.

---

# Deployment Status

Current Status:

Deployment Successful

Environment:

Production

Application Availability:

Online and Accessible

Deployment Platform:

Render
