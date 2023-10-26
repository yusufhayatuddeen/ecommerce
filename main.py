from fastapi import FastAPI, Path, Query
from typing import Optional, List
from pydantic import BaseModel
from api import users, section, courses
app = FastAPI(
    title="FastAPI Developed By Vision Sphere"
)
app.include_router(users.router)
app.include_router(section.router)
app.include_router(courses.router)
