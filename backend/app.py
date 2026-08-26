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


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------
# Request Models
# -------------------------

class UserCreate(BaseModel):
    name: str
    role: str


class SkillCreate(BaseModel):
    skill: str


class ProjectCreate(BaseModel):
    project: str
    description: str


# -------------------------
# Root Endpoint
# -------------------------

@app.get("/")
def home():
    return {
        "message": "DevGraph API is running"
    }


# -------------------------
# Health Check
# -------------------------

@app.get("/health")
def health():
    try:
        db.verify_connection()

        return {
            "status": "healthy",
            "database": "CognoDB"
        }

    except Exception as error:
        raise HTTPException(
            status_code=503,
            detail=f"Database connection failed: {error}"
        )


# -------------------------
# Get Complete User Profile
# -------------------------

@app.get("/users/{user_name}")
def get_user(user_name: str):

    profile = get_user_profile(user_name)

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "name": profile["name"],
        "role": profile["role"],
        "skills": profile["skills"],
        "projects": profile["projects"]
    }


# -------------------------
# Get User Skills
# -------------------------

@app.get("/users/{user_name}/skills")
def get_skills(user_name: str):

    skills = get_user_skills(user_name)

    if not skills:
        raise HTTPException(
            status_code=404,
            detail="User not found or has no skills"
        )

    return {
        "user": user_name,
        "skills": skills
    }


# -------------------------
# Create User
# -------------------------

@app.post("/users")
def create_user_api(user: UserCreate):

    result = create_user(
        user.name,
        user.role
    )

    return {
        "message": "User created successfully",
        "user": {
            "name": result["name"],
            "role": result["role"]
        }
    }


# -------------------------
# Add Skill to User
# -------------------------

@app.post("/users/{user_name}/skills")
def add_user_skill(
    user_name: str,
    skill_data: SkillCreate
):

    result = add_skill(
        user_name,
        skill_data.skill
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "Skill added successfully",
        "relationship": {
            "user": result["user"],
            "type": "KNOWS",
            "skill": result["skill"]
        }
    }


# -------------------------
# Add Project to User
# -------------------------

@app.post("/users/{user_name}/projects")
def add_user_project(
    user_name: str,
    project_data: ProjectCreate
):

    result = add_project(
        user_name,
        project_data.project,
        project_data.description
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "Project added successfully",
        "relationship": {
            "user": result["user"],
            "type": "WORKED_ON",
            "project": result["project"],
            "description": result["description"]
        }
    }
