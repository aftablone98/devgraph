import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


from backend.db import db


USERS = [
    {
        "name": "Aftab Lone",
        "role": "DevOps Engineer",
        "skills": [
            "Python",
            "Docker",
            "Kubernetes"
        ],
        "projects": [
            {
                "name": "Linux Automation",
                "description": "Linux automation and system administration scripts"
            },
            {
                "name": "Docker DevOps",
                "description": "Containerized DevOps application using Docker"
            }
        ]
    },
    {
        "name": "Sarah",
        "role": "Software Engineer",
        "skills": [
            "Python",
            "Docker",
            "Kubernetes"
        ],
        "projects": [
            {
                "name": "Cloud DevOps Platform",
                "description": "Cloud-native application deployment platform"
            }
        ]
    }
]


def seed_database():

    with db.driver.session() as session:

        for user in USERS:

            # Create or update user
            session.run(
                """
                MERGE (u:User {name: $name})
                SET u.role = $role
                """,
                name=user["name"],
                role=user["role"]
            )

            # Add skills
            for skill in user["skills"]:

                session.run(
                    """
                    MATCH (u:User {name: $user_name})

                    MERGE (s:Skill {name: $skill})

                    MERGE (u)-[:KNOWS]->(s)
                    """,
                    user_name=user["name"],
                    skill=skill
                )

            # Add projects
            for project in user["projects"]:

                session.run(
                    """
                    MATCH (u:User {name: $user_name})

                    MERGE (p:Project {name: $project_name})
                    SET p.description = $description

                    MERGE (u)-[:WORKED_ON]->(p)
                    """,
                    user_name=user["name"],
                    project_name=project["name"],
                    description=project["description"]
                )

            print(f"✅ Seeded: {user['name']}")


if __name__ == "__main__":

    try:

        db.verify_connection()

        print("✅ Connected to CognoDB")
        print("🌱 Starting database seed...\n")

        seed_database()

        print("\n✅ Database seeding completed successfully!")

    finally:

        db.close()
