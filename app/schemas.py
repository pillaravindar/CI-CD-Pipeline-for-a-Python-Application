from pydantic import BaseModel,Field,field_validator

class TaskCreate(BaseModel):
    title:str=Field(...,min_length=1,max_length=100)
    description : str | None = None
    @field_validator("title")
    @classmethod
    def validate_title(cls,value:str)->str:
        if not value.strip():
            raise ValueError("Title cannot be empty")
        return value

class TaskUpdate(BaseModel):
    title:str=Field(...,min_length=1,max_length=100)
    description:str|None=None
    completed:bool
    @field_validator("title")
    @classmethod
    def validate_title(cls,value:str)->str:
        if not value.strip():
            raise ValueError("Title cannot be empty")
        return value

class TaskResponse(BaseModel):
    id:int
    title:str
    description :str | None = None
    completed:bool=False