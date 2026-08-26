from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.models import (
    get_user_profile,
    get_user_skills,
    create_user,
    add_skill,
    add_project
)

from backend.db import db


app = FastAPI(
    title="DevGraph API",
    description="Graph-powered Developer Profile API",
    version="1.0.0"
)


# Allow the deployed frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://devgraph-a9cz.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserCreate(BaseModel):
    name: str
    role: str


class SkillCreate(BaseModel):
    user_name: str
    skill_name: str


class ProjectCreate(BaseModel):
    user_name: str
    project_name: str


@app.get("/")
def root():
    return {
        "message": "DevGraph API is running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    try:
        db.verify_connection()
        return {
            "status": "healthy",
            "database": "CognoDB"
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database connection failed: {str(e)}"
        )


@app.get("/users/{user_name}")
def user_profile(user_name: str):
    profile = get_user_profile(user_name)

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "name": profile[0],
        "role": profile[1],
        "skills": profile[2],
        "projects": profile[3]
    }


@app.get("/users/{user_name}/skills")
def user_skills(user_name: str):
    return {
        "user": user_name,
        "skills": get_user_skills(user_name)
    }


@app.post("/users")
def create_user_endpoint(user: UserCreate):
    return create_user(
        user.name,
        user.role
    )


@app.post("/skills")
def add_skill_endpoint(skill: SkillCreate):
    return add_skill(
        skill.user_name,
        skill.skill_name
    )


@app.post("/projects")
def add_project_endpoint(project: ProjectCreate):
    return add_project(
        project.user_name,
        project.project_name
    )


@app.get("/users/{user_name}/profile")
def complete_profile(user_name: str):
    profile = get_user_profile(user_name)

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "name": profile[0],
        "role": profile[1],
        "skills": profile[2],
        "projects": profile[3]
    }
