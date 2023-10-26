from fastapi import FastAPI, Path, Query
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Developed By Vision Sphere"
)
users = []


class User(BaseModel):
    email: str
    name: str
    is_active: str
    address: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The ID of the User you want to retrieve", gt=2),
                   q: str = Query(None, max_length=5)
                   ):
    return {"user": users[id], "query": q}
