from fastapi import FastAPI,HTTPException
from app.schemas import TaskCreate,TaskResponse

app = FastAPI(
    title="FASTAPI task manager",
    description="A simple task manager API build for DevOps project",
    version="1.0"
)
tasks=[]
task_id_counter=1

@app.get("/")
def root():
    return {"message": "Hello Internship Project"}

@app.get("/health")
def health_check():
    return{
        "status":"active",
        "message":"Application is running "
    }


@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):

    global task_id_counter

    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    tasks.append(new_task)

    task_id_counter += 1

    return new_task

@app.get("/tasks",response_model=list[TaskResponse])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}",response_model=TaskResponse)
def get_task(task_id:int):
    for task in tasks:
        if task["id"]==task_id:
            return task
        
    raise HTTPException(status_code=404,detail="Task not found")