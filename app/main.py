from fastapi import FastAPI

app = FastAPI(
    title="FASTAPI task manager",
    description="A simple task manager API build for DevOps project",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "Hello Internship Project"}

@app.get("/health")
def health_check():
    return{
        "status":"active",
        "message":"Application is running "
    }