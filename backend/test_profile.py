from models import get_user_profile
from db import db


try:
    profile = get_user_profile("Aftab Lone")

    print("📌 User Profile")
    print("-------------------------")

    print("Name:", profile["name"])
    print("Role:", profile["role"])

    print("\nSkills:")

    for skill in profile["skills"]:
        print(f"  • {skill}")

    print("\nProjects:")

    for project in profile["projects"]:
        print(f"  • {project}")

finally:
    db.close()
