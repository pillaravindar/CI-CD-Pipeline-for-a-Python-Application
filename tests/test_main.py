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

def test_update_task():
    create_response=client.post(
        "/tasks",
        json={
            "title":"old title",
            "description":"old description"
        }
    )
    create_task=create_response.json()
    create_task_id=create_task["id"]
    update_response = client.put(
        f"/tasks/{create_task_id}",
        json={
            "title":"new title",
            "description":"new description",
            "completed" : True
        }
    )
    assert update_response.status_code==200
    assert update_response.json()["id"]==create_task_id
    assert update_response.json()["title"]=="new title"
    assert update_response.json()["description"]=="new description"
    assert update_response.json()["completed"] is True

def test_update_task_not_found():
    response=client.put(
        "/tasks/9999999",
        json={
            "title":"Missing Task",
            "description":"Missing description",
            "completed":True
        }
    )
    assert response.status_code==404
    assert response.json()["detail"]=="Task not found"

def test_delete_task():
    create_response=client.post(
        "/tasks",
        json={
            "title":"task to delete",
            "description":"task is being deleted"
        }
    )
    create_task=create_response.json()
    create_task_id=create_task["id"]
    delete_task=client.delete(f"/tasks/{create_task_id}")
    assert delete_task.status_code==200
    assert delete_task.json()["message"]=="Task deleted successfully"
    get_task=client.get(f"/tasks/{create_task_id}")
    assert get_task.status_code==404
    assert get_task.json()["detail"]=="Task not found"

def test_delete_task_not_found():
    response=client.delete("/tasks/9999999")
    assert response.status_code==404
    assert response.json()["detail"]=="Task not found"