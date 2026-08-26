from models import (
    create_user,
    add_skill,
    get_user_skills,
    add_project
)

from db import db


try:
    # Create user
    user = create_user(
        "Aftab Lone",
        "DevOps Engineer"
    )

    print("✅ User:")
    print(
        f"Name: {user['name']} | "
        f"Role: {user['role']}"
    )

    # Add skills
    skills = [
        "Python",
        "Docker",
        "Kubernetes"
    ]

    for skill in skills:
        add_skill("Aftab Lone", skill)

    print("\n✅ Skills:")

    results = get_user_skills("Aftab Lone")

    for record in results:
        print(
            f"{record['user']} → KNOWS → "
            f"{record['skill']}"
        )

    # Add projects
    projects = [
        (
            "Linux Automation",
            "Linux and Bash automation scripts"
        ),
        (
            "Docker DevOps",
            "Containerized DevOps application"
        )
    ]

    print("\n✅ Projects:")

    for project_name, description in projects:
        result = add_project(
            "Aftab Lone",
            project_name,
            description
        )

        print(
            f"{result['user']} → WORKED_ON → "
            f"{result['project']}"
        )

finally:
    db.close()
