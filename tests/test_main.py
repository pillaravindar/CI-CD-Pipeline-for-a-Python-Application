from fastapi.testclient import TestClient
from app.main import app
client =TestClient(app)
def test_root_endpoint():
    response=client.get("/")
    assert response.status_code==200
    assert response.json()["message"]=="Hello, this is my Internship Project"

def test_health_endpoint():
    response=client.get("/health")
    assert response.status_code==200
    assert response.json()["status"]=="active"

def test_create_task():
    response=client.post(
        "/tasks",
        json={
            "title":"task1",
            "description":"task1 is important"
        }
    )
    assert response.status_code==200
    data = response.json()
    assert data["title"]=="task1"
    assert data["description"]=="task1 is important"
    assert data["completed"] is False
    assert "id" in data

def test_get_tasks():

    client.post(
        "/tasks",
        json={
            "title":"Task",
            "description":"Test"
        }
    )
    response=client.get("/tasks")
    assert response.status_code==200
    assert isinstance(
        response.json(),
        list
    )
    assert len(
        response.json()
    )>=1

def test_get_task_by_id():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Single task",
            "description": "Testing get by ID"
        }
    )

    created_task = create_response.json()
    task_id = created_task["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "Single task"
    assert data["description"] == "Testing get by ID"

def test_get_task_not_found():
    response = client.get("/tasks/999999")
    response.status_code==404
    response.json()["detail"]=="Task not found"